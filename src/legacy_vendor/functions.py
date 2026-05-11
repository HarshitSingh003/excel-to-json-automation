import collections
from datetime import datetime
import os
import re
import hashlib
import hmac
import base64
import json
import logging
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import openpyxl
import sys

LOGGER = logging.getLogger("wrapper_api")

from .transform_settings import (
    DATE_FIELDS,
    DATE_FORMATES,
    STRING_FIELDS,
    TRANSFORM_FIELDS,
    SECTION_FIELDS,
    SECTION_MAPPING,
    BOOL_REPLACE_FIELDS,
    INT_FIELDS,
)

# def get_sum(data,val):
#     sum_amt = 0
#     for row in data:
#         if row.get(val) and isinstance(row.get(val), (int, float)):
#             sum_amt = sum_amt + row[val]
#     if sum_amt and isinstance(sum_amt, float):
#         sum_amt = round(sum_amt, 8)
#     return sum_amt

# def get_sum(data, val):
#     sum_amt = 0
#     try:
#         for row in data:
#             if isinstance(row.get(val), (int, float)):
#                 sum_amt += row[val]
#     except Exception as e:
#         LOGGER.error(f"Exception in get sum and exception is {e}", exc_info=True)
        
#     sum_amt = round(sum_amt, 8) if isinstance(sum_amt, float) else sum_amt
#     return sum_amt

def get_sum(data, val):
    sum_amt = 0
    try:
        for row in data:
            if isinstance(row.get(val), (int, float)):
                sum_amt += row[val]
        sum_amt = round(sum_amt, 8) if isinstance(sum_amt, float) else sum_amt
    except Exception as e:
        LOGGER.error(f"Exception in get sum and exception is {e}", exc_info=True)
    return sum_amt
        


def dict_merge(dct, merge_dct, add_keys=True):
    dct = dct.copy()
    if not add_keys:
        merge_dct = {k: merge_dct[k] for k in set(dct) & set(merge_dct)}

    for k, v in merge_dct.items():
        if isinstance(dct.get(k), dict) and isinstance(v, collections.abc.Mapping):
            dct[k] = dict_merge(dct[k], v, add_keys=add_keys)
        else:
            dct[k] = v

    return dct

def create_mapping_node(key_str, sep, value, main_obj, item=None):
    if not key_str or sep not in key_str:
        main_obj[key_str] = str(value) if key_str in STRING_FIELDS else value
        if key_str in INT_FIELDS:
            try:
                main_obj[key_str] = int(value) if (key_str in INT_FIELDS and value) else value
            except Exception:
                pass
        return main_obj
    key, val = key_str.split(sep, 1)
    return {key: create_mapping_node(val, sep, value, main_obj)}

def set_mapping_node_inplace(main_obj, key_str, sep, value):
    """
    Set a dotted mapping path directly into main_obj in-place.
    """
    if not key_str:
        return main_obj

    if sep not in key_str:
        final_value = str(value) if key_str in STRING_FIELDS else value
        if key_str in INT_FIELDS:
            try:
                final_value = int(value) if (key_str in INT_FIELDS and value) else value
            except Exception:
                pass
        main_obj[key_str] = final_value
        return main_obj

    keys = key_str.split(sep)
    curr_obj = main_obj

    for key in keys[:-1]:
        if key not in curr_obj or not isinstance(curr_obj[key], dict):
            curr_obj[key] = {}
        curr_obj = curr_obj[key]

    leaf_key = keys[-1]
    final_value = str(value) if leaf_key in STRING_FIELDS else value
    if leaf_key in INT_FIELDS:
        try:
            final_value = int(value) if (leaf_key in INT_FIELDS and value) else value
        except Exception:
            pass

    curr_obj[leaf_key] = final_value
    return main_obj

def get_path(list):
    new_list = []
    for item in list:
        if isinstance(item, int):
            break
        new_list.append(item)
    return ".".join(new_list)

def fetch_list(value_range, column_range, workbook, definename_value, definename_column):
    
    columns = [row[1].value.split("[0]")[1].replace(".", "", 1) if row[1].value and "[0]" in row[1].value\
              else row[1].value.replace(".", "", 1) if row[1].value else row[1].value for row in workbook[column_range.value.split("!")[0].replace("\'", '')]\
              [list(column_range.destinations)[0][1].replace("$","")]]
    ws_values = value_range.value.split("!")[0].replace("\'", '')
    add_values = list(value_range.destinations)[0][1].replace("$", "")

    if not add_values:
        LOGGER.error(f"Empty address range for {definename_value}, skipping")
        return []

    if definename_value == 'ITR6UD_Table':
        start_index, end_index = map(int, re.findall(r'\d+', add_values))
        start_col, end_col = re.findall(r'([a-zA-Z]+)', add_values)
        add_values = f"{start_col}{start_index + 1}:{end_col}{end_index}"

    ret_lst = []

    for row in workbook[ws_values][add_values]:
        item_obj = {}
        values_list = [x.value for x in row]
        if any([x.value for x in row]):
            index = 0

            if columns == ['OperatingRevenueName', 'OperatingRevenueAmt']:
                values_list = [0, values_list[1], values_list[-1]]
            elif columns == ['IFSCCode', 'BankName', 'BankAccountNo', 'UseForRefund']:
                values_list = [0, values_list[1], values_list[3], values_list[5], values_list[7]]
            elif columns == ['SWIFTCode', 'BankName', 'CountryCode', 'IBAN']:
                values_list = [0, values_list[1], values_list[2], values_list[4], values_list[6]]
            elif definename_value == "ITR6CG_STCG_DTAA_Table":
                values_list.pop(2)
                values_list.pop(10)
            elif definename_value == "ITR6PAG1_Other_Income_Tax_Audit_Table":
                values_list = [values_list[idx] for idx in [0, 2, 7, 10, 12, 19] if idx < len(values_list)]
            elif definename_value == "ITR6MATC_Credit_Utilisation_Table":
                values_list.pop(5)
            elif definename_value == "ITR6115TD_Deposits":
                values_list.pop(1)
                values_list.pop(2)
                values_list.pop(2)
                values_list.insert(0, 0)
            elif definename_value in ["ITR6CG_Exempt_LTCG_Oth_Table", "ITR6CG_STCL_Buyback_Table","ITR6CG_LTCL_Buyback_Table","ITR6OS_Other_SR_Income_Table", "ITR6OS_Other_SR_PTI_Income_Table", "ITR6SI_Table", "ITR6PL_OthExp_Table", "ITR680GGC_Table","ITR680LA_Table", "ITR6CG_LTCG_112C_115AB_115AC_115AD_JsonTable"]:
                values_list.insert(0, 0)
            for value in values_list[1:]:
                # print(value)
                if index >= len(columns):
                    break
                if value == None:
                    value = ""
                elif value and isinstance(value, datetime):
                    value = value.strftime("%d/%m/%Y")
                elif columns[index] in TRANSFORM_FIELDS and isinstance(value, str) and "-" in value:
                    value = value.split("-")[0].strip()
                elif columns[index] in SECTION_FIELDS and isinstance(value, str):
                    if "-" in value:
                        value = value.split("-")[0].strip() 
                    value = SECTION_MAPPING.get(value, value)
                elif columns[index] in BOOL_REPLACE_FIELDS and isinstance(value, str):
                    if value.lower() == "y":
                        value = "true"
                    elif value.lower() == "n":
                        value = "false"

                elif isinstance(value, str):
                    try:
                        value = openpyxl.utils.escape.unescape(value).encode("ascii", "ignore").decode()
                        value = value.replace('\r', '').replace('\n', ' ').replace('\t', '').replace('\b', '')
                    except Exception as ex:
                        # value = value
                        pass
                def IsEmpty(str):
                        return str=="" or str.strip()==""
                try:
                    if isinstance(value,str) and IsEmpty(value):
                        if len(value) > 0 :
                            value = value.strip()
                except Exception as ex:
                    pass        
                if value or isinstance(value, (int, float)):
                    set_mapping_node_inplace(item_obj, columns[index], ".", value)
                index += 1

            ret_lst.append(item_obj)
    return ret_lst

def update_errors(name_range_key, error_list):
    for row in error_list:
        row["name_range"] = ""
        key = re.split(r'\.\d+\.', row["field_name"])[0] if re.findall(r'\.\d+\.', row["field_name"]) else row["field_name"]
        row["name_range"] = name_range_key.get(key, row['field_name'])


# def just_open(filename):
#     xlApp = Dispatch("Excel.Application")
#     xlApp.Visible = False
#     xlBook = xlApp.Workbooks.Open(os.getcwd() + "\\" + filename)
#     xlBook.Save()
#     xlBook.Close()

def transform_date(value):
    for frmt in DATE_FORMATES:
        try:
            value = datetime.strptime(value, frmt).strftime("%Y-%m-%d")
            return value
        except:
            pass
    return value

"""Encryption"""

class Encryption:
    '''
    Encryption class with encrypt and decrypt methods used in NIC Process
    '''

    @staticmethod
    def get_private_key(secret_key, salt):
        '''
        Summery Line
            For Private Key
        Parameters:
            secret_key(str):
            salt
        Return private key
        '''
        return hashlib.pbkdf2_hmac('SHA1', secret_key.encode('UTF-8'), \
                                   salt.encode('UTF-8'), 65536, 16)

    @staticmethod
    def decrypt_with_aes(encoded, secret_key, salt, iv1, bs1):
        '''
        Summery Line
            Decrypting encoded messaged using AES
        Parameters:
            encoded(str): encoded data
            secret_key(str): secret key
            salt(str): salt key
            iv1(str): iv1 key
            bs1(str): bs1 key
        Retrun:
            decrypted data
        '''
        private_key = Encryption.get_private_key(secret_key, salt)
        cipher_text = b64decode(encoded.encode())
        # cipher = AES.new(private_key, AES.MODE_CBC, iv1)
        cipher = AES.new(private_key, AES.MODE_GCM, iv1)
        plain_bytes = unpad(cipher.decrypt(cipher_text), bs1)
        return plain_bytes

    @staticmethod
    def reverse_string_case_manner(s):
        reversed_string = s[::-1]  # Reverse the string
        result = ''.join([reversed_string[i].upper() if s[i].isupper() else reversed_string[i].lower() for i in range(len(s))])
        return result
    
    @staticmethod
    def pwd_decrypt(password):
        '''
        Summery Line.
            Decrypting Password
        Parameters:
            password(str): password
        Return:
            decrypted(str): decrypted password
        '''
        decrypted = ""
        flag = False
        try:
            bs1 = 16
            iv1 = "IV_VALUE_16_BYTE".encode()
            secret_key = Encryption.reverse_string_case_manner("EULAV_DROWSSAP")
            salt = "SALT_VALUE"
            decrypted = Encryption.decrypt_with_aes(password, secret_key, salt, iv1, bs1)
            flag = True
        except Exception as error:
            LOGGER.error(f"GSTIN password decrytion failed and exception is {error}", \
                         exc_info=True)
        return decrypted.decode(), flag


def replace_decrypted_value(data,key):
    if isinstance(data, dict):
        for k, forapp in data.items():
            if k == key:
                data[k]=Encryption.pwd_decrypt(data[k])[0]
            elif isinstance(forapp, (dict, list)):
                replace_decrypted_value(forapp, key)
    elif isinstance(data, list):
        for item in data:
            replace_decrypted_value(item,key)

def isexist_inobject(path,Arr):
    isExist=True
    for i in path:
        if i not in Arr:
            LOGGER.error(f"path not found")
            isExist=False
            break
        else:
            LOGGER.info("Path element found")
            Arr=Arr[i]
    return isExist


def extract(obj, arr, key):
    '''
    extract from array
    '''
    if isinstance(obj, dict):
        for k, forapp in obj.items():
            if k == key:
                arr.append(forapp)
            elif isinstance(forapp, (dict, list)):
                extract(forapp, arr, key)
    elif isinstance(obj, list):
        for item in obj:
            extract(item, arr, key)
    return arr

def add_sch80locordesccode(parent, child, value, itr6):
    '''
    Set value in Sch80LocOrDescCode.
    '''
    # if itr6.get(parent, {}).get(child, {}).get("Sch80LocOrDescCode"):
    #     itr6[parent][child]["Sch80LocOrDescCode"] = value
    if itr6.get(parent, {}):
        if itr6[parent].get(child, {}):
            itr6[parent][child]["Sch80LocOrDescCode"] = value
        else:
            itr6[parent][child] = {"Sch80LocOrDescCode": value}
    else:
        itr6[parent] = {child: {"Sch80LocOrDescCode": value}}

def add_sch80locordesccode_child(parent, child, s_child, value, itr6):
    '''
    Set value in Sch80LocOrDescCode for a child and sub-child.
    '''
    # if itr6.get(parent, {}).get(child, {}).get(s_child, {}).get("Sch80LocOrDescCode"):
    #     itr6[parent][child][s_child]["Sch80LocOrDescCode"] = value
    if itr6.get(parent, {}).get(child, {}).get(s_child, {}):
        itr6[parent][child][s_child]["Sch80LocOrDescCode"] = value
    else:
        if not itr6.get(parent):
            itr6[parent] = {}
        if not itr6[parent].get(child):
            itr6[parent][child] = {}
        itr6[parent][child][s_child] = {"Sch80LocOrDescCode": value}


def split_and_set_countrycodeexcludingindia(validate_val,itr6):
    '''
    Here we set value in CountryCodeExcludingIndia
    '''
    if itr6.get("ScheduleFA") and itr6["ScheduleFA"].get(validate_val):
        code = itr6["ScheduleFA"].get(validate_val)
        if isinstance(code,list):
            for _code in code:
                if "CountryCodeExcludingIndia" in _code:
                    if "-" in _code["CountryCodeExcludingIndia"]:
                        val_1 = _code["CountryCodeExcludingIndia"].split("-")[0]
                        val_2 = _code["CountryCodeExcludingIndia"].split("-")[1]
                        _code["CountryCodeExcludingIndia"] = val_1.replace(" ", "")
                        _code["CountryName"] = val_1+"-"+val_2

# def generate_digest(itr6_obj):
#     '''
#     Here we generate digest key
#     '''
#     creation_info = itr6_obj.get("ITR", {}).get("ITR6", {}).get("CreationInfo", {})

#     if "Digest" in creation_info:
#         key = sSharedSecretKey.encode('utf-8')
#         # f = open(r"D:\Backup\10-08 test\6966\6966.json", 'r')
#         # message = f.read().replace("\n","\r\n").encode('utf-8')
#         f = json.dumps(itr6_obj)
#         message = f.replace("\n","").replace(" ","").encode('utf-8')
#         iteration_v=iteration
#         # Generate the hash.
#         i=1
#         signature = hmac.new(
#                 key,
#                 message,
#                 hashlib.sha256
#             ).digest()
#         while i<=iteration_v:
#             signature = hmac.new(
#                 key,
#                 signature,
#                 hashlib.sha256
#             ).digest()
#             i+=1
#         digest_sign = base64.b64encode(signature)
#         creation_info["Digest"] = digest_sign.decode('utf-8')