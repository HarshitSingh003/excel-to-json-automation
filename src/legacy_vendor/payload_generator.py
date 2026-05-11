'''
Summery Line
    generate payload
'''
import datetime
import copy
from os import stat
from .payload_config import MANDATORY_NODE_STRUCTURE
from .transformation import DataTypeTransformation
from .transform_settings import CHECK_DEF_AND_SET, VALIDATE_VALUE, Schedule80_IA_config,Schedule80_IB_config,Schedule80_IC_config,Schedule80_IC_DeductInNorthEast_config
from .business_configuration import PRIORITY_DICT, METHOD_DICT, METHOD_DICT_FOR_FILE_DATA
from .functions import dict_merge, get_sum, add_sch80locordesccode, add_sch80locordesccode_child, split_and_set_countrycodeexcludingindia
from .lists import source_range
import logging
LOGGER = logging.getLogger("wrapper_api")
import json

class GeneratePayload:
    '''
    Summery Line
        Generate Payload
    '''
    def __str__(self) -> str:
        '''
        Summery Line
            GeneratePayload presentation
        '''
        return "GeneratePayload object"

    @staticmethod
    def parent_gen_payload(source_payload):
        '''
        '''
        final_node = {}
        for key, value in  MANDATORY_NODE_STRUCTURE.items():
            if source_payload.get(key):
                node = GeneratePayload.gen_payload(value, key, source_payload.get(key))
                if node:
                    final_node[key] = node
        return final_node
    
    @staticmethod
    def process_nodes(payload, data, node_type):
        result = {}
        for key, value in payload.get(node_type, {}).items():
            if data.get(key):
                child_node = GeneratePayload.gen_payload(value, key, data[key])
                if child_node:
                    result[key] = child_node
        return result

    @staticmethod
    def gen_payload(value, key, source_payload):
      
        node = {}
        source_data = source_payload

        if value.get("field_required"):
            for field_req in value.get("field_required"):
                field_name = field_req[0]
                field_obj = field_req[1]
                field_trans = field_req[2]
                field_blank_insert = field_req[3]
                transform_func = field_req[4]


                if field_name in source_data:
                    key_source_data = source_data[field_name]

                    if key_source_data:
                        if not isinstance(key_source_data, field_obj):
                            key_source_data = field_trans(key_source_data)

                        if transform_func:
                            key_source_data = transform_func(key_source_data)

                        node[field_name] = key_source_data
                        
                    elif field_blank_insert:
                        node[field_name] = key_source_data

        if value.get("field_optional"):

            for field_opt in value.get("field_optional"):
                field_name = field_opt[0]
                field_obj = field_opt[1]
                field_trans = field_opt[2]
                field_blank_insert = field_opt[3]
                transform_func = field_opt[4]
                default_trans = field_opt[5]
                default_val = field_opt[6]
                if field_name in source_data:
                    key_source_data = source_data[field_name]
                    if key_source_data:
                        if not isinstance(key_source_data, field_obj):
                            key_source_data = field_trans(key_source_data)
                        if transform_func:
                            key_source_data = transform_func(key_source_data)
                        node[field_name] = key_source_data
                    elif field_blank_insert:
                        node[field_name] = key_source_data
                    elif default_trans:
                        node[field_name] = default_val
    
        def process_nodes(payload, data, node_type):
            result = {}
            for key, value in payload.get(node_type, {}).items():
                if not isinstance(data, str) and data.get(key):
                    child_node = GeneratePayload.gen_payload(value, key, data[key])
                    if child_node:
                        result[key] = child_node
            return result

        node.update(process_nodes(value, source_payload, "node_required"))
        node.update(process_nodes(value, source_payload, "node_optional"))

        if value.get("array_required"):
            for array_required_key, array_required_value in value.get("array_required").items():
                array_req_key = source_payload.get(array_required_key)
                if array_req_key:
                    array_list = []
                    for array_dict in array_req_key:
                        array_node = GeneratePayload.gen_payload(array_required_value, array_required_key,
                            array_dict)
                        if array_node:
                            array_list.append(array_node)
                    if array_list:
                        node[array_required_key] = array_list

        if value.get("array_optional"):
            for array_optional_key, array_optional_value in value.get("array_optional").items():
                arr_opt_key = source_payload.get(array_optional_key)
                if arr_opt_key:
                    array_list = []
                    for array_dict in arr_opt_key:
                        array_node = GeneratePayload.gen_payload(array_optional_value, array_optional_key,
                            array_dict)
                        if array_node:
                            array_list.append(array_node)
                    if array_list:
                        node[array_optional_key] = array_list

        if value.get("cm_field_map") and node:
            for cm_field in value.get("cm_field_map"):
                field_name = cm_field[0]
                field_obj = cm_field[1]
                field_trans = cm_field[2]
                field_blank_insert = cm_field[3]
                default_trans = cm_field[5]
                default_val = cm_field[6]
                if field_name not in node and field_name in source_data:
                    key_source_data = source_data[field_name]
                    if key_source_data:
                        if not isinstance(key_source_data, field_obj):
                            key_source_data = field_trans(key_source_data)
                        node[field_name] = key_source_data
                    elif field_blank_insert:
                        node[field_name] = key_source_data
                    elif default_trans:
                        node[field_name] = default_val
                elif field_name in CHECK_DEF_AND_SET and field_name not in node and field_name not in source_data and default_trans:
                    node[field_name] = default_val

        if value.get("cm_node_map") and node:
            for cm_node_key, cm_node_value in value.get("cm_node_map").items():
                if cm_node_key not in node and cm_node_key in source_data:
                    cm_node = GeneratePayload.gen_payload(cm_node_value, cm_node_key,source_data[cm_node_key])
                    if cm_node:
                        node[cm_node_key] = cm_node
        return node

    @staticmethod
    def get_name_range_data(workbook, named_range, is_int=False):
        '''
        Summery Line
            Here we are getting the name range
        '''
        value_range_data = workbook.defined_names[named_range]
        sales_destinations = list(value_range_data.destinations)
        sales_ws, sales_reg = sales_destinations[0]
        if isinstance(sales_ws, str):
            # reading obj from wb object
            sales_ws = workbook[sales_ws]
        sales_region = sales_ws[sales_reg]
        value = sales_region.value
        if is_int and isinstance(value, str):
            value = int(value)
        return value
    
    @staticmethod
    def MAT_modification(workbook, itr6_obj):
        '''
        Here we are doing modification of MAT
        '''
        mat = False
        matc = False
        val_1 = None
        val_2 = None
        try:
            val_1 = GeneratePayload.get_name_range_data(workbook,"Opt_115BA_BAA_BAB_CY_IRL",is_int=False)
            val_2 = GeneratePayload.get_name_range_data(workbook,"Opt_115BA_BAA_BAB_IRL",is_int=False)

            if (val_1 == "115BA - Section 115BA" or val_1 == "115BAA - Section 115BAA" or val_1 == "115BAB - Section 115BAB") or (val_2 == "115BA - Section 115BA" or val_2 == "115BAA - Section 115BAA" or val_2 == "115BAB - Section 115BAB"):
                if "ScheduleMAT" in itr6_obj["ITR"]["ITR6"]:
                    del itr6_obj["ITR"]["ITR6"]["ScheduleMAT"]
                    mat = True
                if "ScheduleMATC" in itr6_obj["ITR"]["ITR6"]:
                    del itr6_obj["ITR"]["ITR6"]["ScheduleMATC"]
                    matc = True
            # return mat, matc
        except Exception as ex:
            pass
            print("Exception", ex)
        # finally:
            # return mat, matc
        return mat, matc
    @staticmethod
    def generate_scheduleHP(payload,workbook):
        '''
        Summery Line
            Here we are modifying the scheduleHP
        Parameters:
            payload(dict): payload
        Return:
            None
        '''
        if "ScheduleHP" not in payload["ITR"]["ITR6"]:
                list1 = ["ITR6HP1_Addr","ITR6HP1_City","ITR6HP1_State","ITR6HP1_Country","ITR6HP1_PIN","ITR6HP1_ZIP"]
                list1_ch = ["AddrDetail","CityOrTownOrDistrict","StateCode","CountryCode","PinCode","ZipCode"]

                list2 = ["ITR6HP1_Gross_Rent","ITR6HP1_Rent_unrealised","ITR6HP1_Tax_Local_Auth","ITR6HP1_Unrealised_Tax_Tot","ITR6HP1_Annual_Value","ITR6HP1_Annual_Value_Share","ITR6HP1_30_Prec","ITR6HP1_Dedn_Tot","ITR6HP1_Income_HP","ITR6HP1_Int_Borr_Cap","ITR6HP1_Net_Arr_Unr_Rent"]
                list2_ch = ["AnnualLetableValue","RentNotRealized","LocalTaxes","TotalUnrealizedAndTax","BalanceALV","AnnualOfPropOwned","ThirtyPercentOfBalance","TotalDeduct","IncomeOfHP","IntOnBorwCap","ArrearsUnrealizedRentRcvd"]

                list3 = ["ITR6HP1_SlNo","ITR6HP1_Self_Deem","ITR6HP1_If_Cown","ITR6HP1_Perc_Share","ITR6HP1_Type"]
                list3_ch = ["HPSNo","PropertyOwner","PropCoOwnedFlg","AssessePercentShareProp","ifLetOut"]

                list4 = ["ITR6HP1_Income_HP_PTI","ITR6HP1_Income_HP_Tot"]
                list4_ch = ["PassThroghIncome","TotalIncomeChargeableUnHP"]

                list11 = ["ITR6HP2_Addr","ITR6HP2_City","ITR6HP2_State","ITR6HP2_Country","ITR6HP2_PIN","ITR6HP2_ZIP"]
                list11_ch = ["AddrDetail","CityOrTownOrDistrict","StateCode","CountryCode","PinCode","ZipCode"]

                list12 = ["ITR6HP2_Gross_Rent","ITR6HP2_Rent_unrealised","ITR6HP2_Tax_Local_Auth","ITR6HP2_Unrealised_Tax_Tot","ITR6HP2_Annual_Value","ITR6HP2_Annual_Value_Share","ITR6HP2_30_Prec","ITR6HP2_Dedn_Tot","ITR6HP2_Income_HP","ITR6HP2_Int_Borr_Cap","ITR6HP2_Net_Arr_Unr_Rent"]
                list12_ch = ["AnnualLetableValue","RentNotRealized","LocalTaxes","TotalUnrealizedAndTax","BalanceALV","AnnualOfPropOwned","ThirtyPercentOfBalance","TotalDeduct","IncomeOfHP","IntOnBorwCap","ArrearsUnrealizedRentRcvd"]

                list13 = ["ITR6HP2_SlNo","ITR6HP2_Self_Deem","ITR6HP2_If_Cown","ITR6HP2_Perc_Share","ITR6HP2_Type"]
                list13_ch = ["HPSNo","PropertyOwner","PropCoOwnedFlg","AssessePercentShareProp","ifLetOut"]

                list33 = ["ITR6HP_Addr_3","ITR6HP_City_3","ITR6HP_State_3","ITR6HP3_Country","ITR6HP3_PIN","ITR6HP3_ZIP"]
                list33_ch = ["AddrDetail","CityOrTownOrDistrict","StateCode","CountryCode","PinCode","ZipCode"]
 
                list331 = ["ITR6HP3_Gross_Rent","ITR6HP3_Rent_unrealised","ITR6HP3_Tax_Local_Auth","ITR6HP3_Unrealised_Tax_Tot","ITR6HP3_Annual_Value","ITR6HP3_Annual_Value_Share","ITR6HP3_30_Prec","ITR6HP3_Dedn_Tot","ITR6HP3_Income_HP","ITR6HP3_Int_Borr_Cap","ITR6HP3_Net_Arr_Unr_Rent"]
                list331_ch = ["AnnualLetableValue","RentNotRealized","LocalTaxes","TotalUnrealizedAndTax","BalanceALV","AnnualOfPropOwned","ThirtyPercentOfBalance","TotalDeduct","IncomeOfHP","IntOnBorwCap","ArrearsUnrealizedRentRcvd"]
 
                list332 = ["ITR6HP3_SlNo","ITR6HP3_Self_Deem","ITR6HP3_If_Cown","ITR6HP3_Perc_Share","ITR6HP3_Type"]
                list332_ch = ["HPSNo","PropertyOwner","PropCoOwnedFlg","AssessePercentShareProp","ifLetOut"]

                list34 = ["ITR6HP_Addr_4","ITR6HP_City_4","ITR6HP_State_4","ITR6HP4_Country","ITR6HP4_PIN","ITR6HP4_ZIP"]
                list34_ch = ["AddrDetail","CityOrTownOrDistrict","StateCode","CountryCode","PinCode","ZipCode"]
 
                list341 = ["ITR6HP4_Gross_Rent","ITR6HP4_Rent_unrealised","ITR6HP4_Tax_Local_Auth","ITR6HP4_Unrealised_Tax_Tot","ITR6HP4_Annual_Value","ITR6HP4_Annual_Value_Share","ITR6HP4_30_Prec","ITR6HP4_Dedn_Tot","ITR6HP4_Income_HP","ITR6HP4_Int_Borr_Cap","ITR6HP4_Net_Arr_Unr_Rent"]
                list341_ch = ["AnnualLetableValue","RentNotRealized","LocalTaxes","TotalUnrealizedAndTax","BalanceALV","AnnualOfPropOwned","ThirtyPercentOfBalance","TotalDeduct","IncomeOfHP","IntOnBorwCap","ArrearsUnrealizedRentRcvd"]
 
                list342 = ["ITR6HP4_SlNo","ITR6HP4_Self_Deem","ITR6HP4_If_Cown","ITR6HP4_Perc_Share","ITR6HP4_Type"]
                list342_ch = ["HPSNo","PropertyOwner","PropCoOwnedFlg","AssessePercentShareProp","ifLetOut"]

                list5= ["CoOwnersSNo","NameCoOwner","PAN_CoOwner","Aadhaar_CoOwner","PercentShareProperty"]
                list6 = ["TenantSNo","NameofTenant","PANofTenant","AadhaarofTenant","PANTANofTenant"]
                list7 = ["LoanTknFrom","BankOrInstnName","LoanAccNoOfBankOrInstnRefNo","DateofLoan","TotalLoanAmt", "LoanOutstndngAmt", "InterestUs24B"]
                list71 = ["ITR6HP_24B_TotAmt1","ITR6HP_24B_TotAmt2","ITR6HP_24B_TotAmt3","ITR6HP_24B_TotAmt4"]
                main = {}
                def find_acc_range(lists,workbook):
                    retList=[]
                    for i in lists:
                            try :
                                value_range_data = workbook.defined_names[i]
                                sales_destinations = list(value_range_data.destinations)
                                sales_ws, sales_reg = sales_destinations[0]
                                if isinstance(sales_ws, str):
                                    sales_ws = workbook[sales_ws]
                                sales_region = sales_ws[sales_reg]
                                value = sales_region.value
                                if isinstance(value,str) and "-" in value:
                                    value = value.split("-")[0].replace(" ", "")
                                if value == None:
                                    value = 0
                                retList.append(value)
                            except Exception as ex:
                                pass
                    return retList


                def merge_val(list1_ch,val):
                    res = {}
                    for key in list1_ch:
                        for value in val:
                            if(value!=''):
                                res[key] = value
                            val.remove(value)
                            break
                    return res

                AddressDetailWithZipCode = find_acc_range(list1,workbook)
                Rentdetails = find_acc_range(list2,workbook)
                HPS_No = find_acc_range(list3,workbook)
                Main = find_acc_range(list4,workbook)

                address_DetailWithZipCode = merge_val(list1_ch,AddressDetailWithZipCode)
                Rent_details = merge_val(list2_ch,Rentdetails)
                hp_sno = merge_val(list3_ch,HPS_No)
                ma_in = merge_val(list4_ch,Main)

                AddressDetailWithZipCode1 = find_acc_range(list11,workbook)
                Rentdetails1 = find_acc_range(list12,workbook)
                HPS_No1 = find_acc_range(list13,workbook)

                address_DetailWithZipCode1 = merge_val(list11_ch,AddressDetailWithZipCode1)
                Rent_details1 = merge_val(list12_ch,Rentdetails1)
                hp_sno1 = merge_val(list13_ch,HPS_No1)

                AddressDetailWithZipCode2 = find_acc_range(list33,workbook)
                Rentdetails2 = find_acc_range(list331,workbook)
                HPS_No2 = find_acc_range(list332,workbook)

                address_DetailWithZipCode2 = merge_val(list33_ch,AddressDetailWithZipCode2)
                Rent_details2 = merge_val(list331_ch,Rentdetails2)
                hp_sno2 = merge_val(list332_ch,HPS_No2)

                AddressDetailWithZipCode3 = find_acc_range(list34,workbook)
                Rentdetails3 = find_acc_range(list341,workbook)
                HPS_No3 = find_acc_range(list342,workbook)

                address_DetailWithZipCode3 = merge_val(list34_ch,AddressDetailWithZipCode3)
                Rent_details3 = merge_val(list341_ch,Rentdetails3)
                hp_sno3 = merge_val(list342_ch,HPS_No3)

                def find_table(name_r, workbook):
                    try:
                        re = []
                        address = list(workbook.defined_names[name_r].destinations)
                        #removing the $ from the address
                        for sheetname, cellAddress in address:
                            cellAddress = cellAddress.replace('$','')
                        #looping through each cell address, extracting it from the tuple and printing it out     
                        worksheet = workbook[sheetname]
                        for i in range(0,len(worksheet[cellAddress])):
                            for item in worksheet[cellAddress][i]:
                                re.append(item.value)
                    except Exception as ex:
                        pass
                    return re

                ddd = find_table("ITR6HP1_Cown_Table",workbook)
                vall = find_table("ITR6HP1_Tent_Table",workbook)

                ddd1 = find_table("ITR6HP2_Cown_Table",workbook)
                vall1 = find_table("ITR6HP2_Tent_Table",workbook)

                ddd2 = find_table("ITR6HP3_Cown_Table",workbook)
                vall2 = find_table("ITR6HP3_Tent_Table",workbook)

                ddd3 = find_table("ITR6HP4_Cown_Table",workbook)
                vall3 = find_table("ITR6HP4_Tent_Table",workbook)

                Section24B_1 = find_table("ITR6HP_24B_Table1",workbook)
                Section24B_2 = find_table("ITR6HP_24B_Table2",workbook)
                Section24B_3 = find_table("ITR6HP_24B_Table3",workbook)
                Section24B_4 = find_table("ITR6HP_24B_Table4",workbook)

                def val(v):
                    return "" if v==None else v

                def tab_val2(tab_val):
                    try:
                        ar = []
                        i=0
                        while i<len(tab_val)/7:
                            isValid = False
                            if(tab_val[(7*i)+0]!=None or tab_val[(7*i)+1]!=None or tab_val[(7*i)+2]!=None or tab_val[(7*i)+3]!=None or tab_val[(7*i)+4]!=None or tab_val[(7*i)+5]!=None):
                                isValid = True
                            if isValid:
                                arr=[]
                                arr.append(val(tab_val[(7*i)+0]))
                                arr.append(val(tab_val[(7*i)+1]))
                                arr.append(val(tab_val[(7*i)+2]))
                                v3 = val(tab_val[(7*i)+3])
                                if isinstance(v3, datetime.datetime):
                                    arr.append(v3.strftime("%Y-%m-%d"))
                                else:
                                    arr.append(str.upper(val(v3)))
                                arr.append(val(tab_val[(7*i)+4]))
                                arr.append(val(tab_val[(7*i)+5]))
                                arr.append(val(tab_val[(7*i)+6]))
                                ar.append(arr)
                            i+=1
                    except Exception as ex:
                        pass
                    return ar
                
                def tab_val(tab_val):
                    try:
                        ar = []
                        i=0
                        while i<len(tab_val)/6:
                            isValid = False
                            if(tab_val[(6*i)+0]!=None or tab_val[(6*i)+1]!=None or tab_val[(6*i)+2]!=None or tab_val[(6*i)+3]!=None or tab_val[(6*i)+4]!=None or tab_val[(6*i)+5]!=None):
                                isValid = True
                            if isValid:
                                arr=[]
                                arr.append(val(tab_val[(6*i)+0]))
                                arr.append(val("" if tab_val[(6*i)+1]==None else tab_val[(6*i)+1] if tab_val[(6*i)+2]==None else tab_val[(6*i)+2]))
                                arr.append(str.upper(val(tab_val[(6*i)+3])))
                                arr.append(val(tab_val[(6*i)+4]))
                                arr.append(val(tab_val[(6*i)+5]))
                                ar.append(arr)
                            i+=1
                    except Exception as ex:
                        pass
                    return ar

                arrr = tab_val(ddd)
                fff = tab_val(vall)

                arrr1 = tab_val(ddd1)
                fff1 = tab_val(vall1)

                arrr33 = tab_val(ddd2)
                fff33 = tab_val(vall2)

                arrr34 = tab_val(ddd3)
                fff34 = tab_val(vall3)
                S_24B_1 = tab_val2(Section24B_1)
                S_24B_2 = tab_val2(Section24B_2)
                S_24B_3 = tab_val2(Section24B_3)
                S_24B_4 = tab_val2(Section24B_4)

                new_ar = []
                new_ar2=[]
                for i in arrr:
                    new_ar.append(merge_val(list5,i))
                for d in fff:
                    new_ar2.append(merge_val(list6,d))

                new_ar1 = []
                new_ar21=[]
                for i in arrr1:
                    new_ar1.append(merge_val(list5,i))
                for d in fff1:
                    new_ar21.append(merge_val(list6,d))

                new_ar33 = []
                new_ar331=[]
                for i in arrr33:
                    new_ar33.append(merge_val(list5,i))
                for d in fff33:
                    new_ar331.append(merge_val(list6,d))

                new_ar34=[]
                new_ar341=[]
                new_ar24_1 = []
                new_ar24_2 = []
                new_ar24_3 = []
                new_ar24_4 = []
                for i in arrr34:
                    new_ar34.append(merge_val(list5,i))
                for d in fff34:
                    new_ar341.append(merge_val(list6,d))
                
                for d in S_24B_1:
                    new_ar24_1.append(merge_val(list7,d))
                for d in S_24B_2:
                    new_ar24_2.append(merge_val(list7,d))
                for d in S_24B_3:
                    new_ar24_3.append(merge_val(list7,d))
                for d in S_24B_4:
                    new_ar24_4.append(merge_val(list7,d))
                
                Total_24B = []

                if new_ar24_1:
                    new_ar24_1[0]['LoanTknFrom'] = new_ar24_1[0].get('LoanTknFrom', '').split("-")[0].strip()
                if new_ar24_2:
                    new_ar24_2[0]['LoanTknFrom'] = new_ar24_2[0].get('LoanTknFrom', '').split("-")[0].strip()
                if new_ar24_3:
                    new_ar24_3[0]['LoanTknFrom'] = new_ar24_3[0].get('LoanTknFrom', '').split("-")[0].strip()
                if new_ar24_4:
                    new_ar24_4[0]['LoanTknFrom'] = new_ar24_4[0].get('LoanTknFrom', '').split("-")[0].strip()

                Total_24B = find_acc_range(list71,workbook)
                
                Total_24B_1, Total_24B_2, Total_24B_3, Total_24B_4 = [
                    val if val else "" for val in (Total_24B + [""]*4)[:4]
                ]

                Rent_details['Section24B'] = {"Section24BDtls": new_ar24_1, "TotalInterestUs24B": Total_24B_1}
                Rent_details1['Section24B'] = {"Section24BDtls": new_ar24_2, "TotalInterestUs24B": Total_24B_2}
                Rent_details2['Section24B'] = {"Section24BDtls": new_ar24_3, "TotalInterestUs24B": Total_24B_3}
                Rent_details3['Section24B'] = {"Section24BDtls": new_ar24_4, "TotalInterestUs24B": Total_24B_4}


                o={"CoOwners":new_ar,"TenantDetails":new_ar2,"AddressDetailWithZipCode":address_DetailWithZipCode,"Rentdetails":Rent_details}
                oo={"CoOwners":new_ar1,"TenantDetails":new_ar21,"AddressDetailWithZipCode":address_DetailWithZipCode1,"Rentdetails":Rent_details1}
                ooo={"CoOwners":new_ar33,"TenantDetails":new_ar331,"AddressDetailWithZipCode":address_DetailWithZipCode2,"Rentdetails":Rent_details2}
                oooo={"CoOwners":new_ar34,"TenantDetails":new_ar341,"AddressDetailWithZipCode":address_DetailWithZipCode3,"Rentdetails":Rent_details3}

                for i in hp_sno.keys():
                    o[i]=hp_sno[i]
                m={}
                for f in ma_in.keys():
                    m[f]=ma_in[f]

                for i in hp_sno1.keys():
                    oo[i]=hp_sno1[i]

                for i in hp_sno2.keys():
                    ooo[i]=hp_sno2[i]

                for i in hp_sno3.keys():
                    oooo[i]=hp_sno3[i]

                # m={}
                # for f in ma_in1.keys():
                #     m[f]=ma_in1[f]

                main["ScheduleHP"]=m
                main["ScheduleHP"]["PropertyDetails"]=[o,oo,ooo,oooo]
                payload["ITR"]["ITR6"]["ScheduleHP"] = main["ScheduleHP"]

    @staticmethod
    def transform_nri_json(input_json: dict) -> dict:
        """
        Transform separate BE and AE arrays into schema-compliant format.
        """
        be_list = input_json.get("NRIOnSec112and115Dtls_BE", [])
        ae_list = input_json.get("NRIOnSec112and115Dtls_AE", [])
        dtls_list = input_json.get("NRIOnSec115ADDtls", [])
        total = input_json.get("TotalNRIOnSec112and115", [])

        # Index AE list by SectionCode for fast lookup
        ae_dict = {item["SectionCode"]: item for item in ae_list}

        combined = []
        for be_item in be_list:
            sec_code = be_item["SectionCode"]

            # remove SectionCode from inner blocks (schema requires it only at root level)
            be_data = {k: v for k, v in be_item.items() if k != "SectionCode"}
            ae_data = {k: v for k, v in ae_dict.get(sec_code, {}).items() if k != "SectionCode"}

            combined.append({
                "SectionCode": sec_code,
                "NRIOnSec112and115Dtls_BE": be_data,
                "NRIOnSec112and115Dtls_AE": ae_data
            })

        return {"NRIOnSec112and115Dtls": combined, "NRIOnSec115ADDtls" : dtls_list, "TotalNRIOnSec112and115" : total}

    @staticmethod
    def modify_payload(payload):
        '''
        Summery Line
            Here we are modifying the payload
        Parameters:
            payload(dict): payload
        Return:
            None
        '''
        if payload.get("ITR") and payload["ITR"].get("ITR6"):
            itr6 = payload["ITR"]["ITR6"]

            # Safely access SchedulePTI
            schedule_pti = itr6.get("SchedulePTI", {})
            schedule_pti_keys = [
                key for key in schedule_pti.keys() if isinstance(key, str) and key.startswith("SchedulePTIDtls")
            ]
            
            # Safely access ScheduleFSI
            schedule_fsi = itr6.get("ScheduleFSI", {})
            schedule_fsi_keys = [
                key for key in schedule_fsi.keys() if isinstance(key, str) and key.startswith("ScheduleFSIDtls")
            ]

            try:
                if (schedule_pti_keys and len(schedule_pti_keys) > 0) or (schedule_fsi_keys and len(schedule_fsi_keys) > 0):
                    if schedule_pti_keys or schedule_fsi_keys:
                        from collections import defaultdict

                        def remove_indices_and_group(source_payload):
                            if isinstance(source_payload, dict):  # If the current data is a dictionary
                                grouped_data = defaultdict(list)
                                for key, value in source_payload.items():
                                    base_key = key.split('[')[0]  # Remove index part
                                    grouped_data[base_key].append(remove_indices_and_group(value))  # Recurse
                                # Flatten single-item lists into the dictionary
                                return {k: v if len(v) > 1 else v[0] for k, v in grouped_data.items()}
                            elif isinstance(source_payload, list):  # If the current data is a list
                                return [remove_indices_and_group(item) for item in source_payload]
                            else:
                                return source_payload  # If the current data is not a dictionary or list, return as-is

                        itr6["ScheduleFSI"] = remove_indices_and_group(schedule_fsi)
                        itr6["SchedulePTI"] = remove_indices_and_group(schedule_pti)
                        if len(schedule_fsi_keys) == 1:
                            itr6["ScheduleFSI"]["ScheduleFSIDtls"] = [itr6["ScheduleFSI"]["ScheduleFSIDtls"]]
                        if len(schedule_pti_keys) == 1:
                            itr6["SchedulePTI"]["SchedulePTIDtls"] = [itr6["SchedulePTI"]["SchedulePTIDtls"]]
            except Exception as e:
                pass
            # if payload["ITR"]["ITR6"].get("ScheduleHP"):
            #     key = "PropertyDetails"
            #     payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails"] = []
            #     schedule_hp = payload["ITR"]["ITR6"]["ScheduleHP"]
            #     for index in range(4):
            #         new_key = f"{key}[{index}]"
            #         if schedule_hp.get(new_key):
            #             schedule_hp["PropertyDetails"].append(schedule_hp.get(new_key))
            if itr6.get("PartB_TTI") and itr6["PartB_TTI"].get("Refund") and itr6["PartB_TTI"]["Refund"].get("BankAccountDtls") :
                flag_check = itr6["PartB_TTI"]["Refund"].get("BankAccountDtls")
                if "BankDtlsFlag" in flag_check:
                    if flag_check["BankDtlsFlag"] == "Y":
                        if "ForeignBankDetails" in flag_check:
                            del flag_check["ForeignBankDetails"]
                    elif flag_check["BankDtlsFlag"] == "N":
                        if "AddtnlBankDetails" in flag_check:
                            del flag_check["AddtnlBankDetails"]

            if itr6.get("ScheduleCG") and itr6["ScheduleCG"].get("LongTermCapGain"):
                longterm = itr6["ScheduleCG"].get("LongTermCapGain")
                if longterm.get("SaleofLandBuild"):
                    if longterm["SaleofLandBuild"].get("SaleofLandBuildDtls") and isinstance(\
                        longterm["SaleofLandBuild"].get("SaleofLandBuildDtls"), dict):
                        if "ExemptionOrDednUs54Dtls" in longterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"] and isinstance(longterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionOrDednUs54Dtls"],list):
                            temp = get_sum(longterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionOrDednUs54Dtls"],"ExemptionAmount")
                            longterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionGrandTotal"]=temp
                        longterm["SaleofLandBuild"]["SaleofLandBuildDtls"] = [longterm["SaleofLandBuild"]["SaleofLandBuildDtls"]]
                        if longterm["SaleofLandBuild"].get("SaleofLandBuildDtls[0]"):
                            longterm["SaleofLandBuild"]["SaleofLandBuildDtls"] = [dict_merge(\
                                longterm["SaleofLandBuild"]["SaleofLandBuildDtls"][0], \
                                longterm["SaleofLandBuild"].get("SaleofLandBuildDtls[0]"), add_keys=True)]
                            # longterm["SaleofLandBuild"] = [longterm["SaleofLandBuild"]]
                if longterm["SaleofLandBuild"].get("SaleofLandBuildDtls[0]").get("CapgainonAssets", 0) == 0:
                            del longterm["SaleofLandBuild"]
                if longterm.get("NRIOnSec112and115", {}).get("NRIOnSec112and115Dtls[0]",{}):
                    dict_data = longterm.get("NRIOnSec112and115", {}).get("NRIOnSec112and115Dtls[0]",{})
                    if dict_data:
                        longterm["NRIOnSec112and115"]["NRIOnSec112and115Dtls"] = [dict_data]

            if itr6.get("ScheduleCG") and itr6["ScheduleCG"].get("ShortTermCapGain"):
                shortterm = itr6["ScheduleCG"].get("ShortTermCapGain")
                if "EquityMFonSTT[0]" in shortterm:
                    # Rename the key from 'EquityMFonSTT[0]' to 'EquityMFonSTT'
                    shortterm["EquityMFonSTT"] = [shortterm.pop("EquityMFonSTT[0]")]
                if shortterm.get("SaleofLandBuild"):
                    if shortterm["SaleofLandBuild"].get("SaleofLandBuildDtls") and isinstance(\
                        shortterm["SaleofLandBuild"].get("SaleofLandBuildDtls"), dict):
                        if "ExemptionOrDednUs54Dtls" in shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"] and isinstance(shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionOrDednUs54Dtls"],list):
                            _temp = get_sum(shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionOrDednUs54Dtls"],"ExemptionAmount")
                            shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionGrandTotal"]=_temp
                        shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"] = [shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"]]
                        if shortterm["SaleofLandBuild"].get("SaleofLandBuildDtls[0]"):
                            shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"] = [dict_merge(\
                                shortterm["SaleofLandBuild"]["SaleofLandBuildDtls"][0], \
                                shortterm["SaleofLandBuild"].get("SaleofLandBuildDtls[0]"), add_keys=True)]
            
        #     # Refund Details
        #     refund_details = itr6.get("PartB_TTI", {}).get("Refund", {}).get("BankAccountDtls")
        #     if refund_details and "BankDtlsFlag" in refund_details:
        #         if refund_details["BankDtlsFlag"] == "Y" and "ForeignBankDetails" in refund_details:
        #             del refund_details["ForeignBankDetails"]
        #         elif refund_details["BankDtlsFlag"] == "N" and "AddtnlBankDetails" in refund_details:
        #             del refund_details["AddtnlBankDetails"]
                    
        #     # Process Capital Gains
        #     if itr6.get("ScheduleCG"):
        #         schedule_cg = itr6["ScheduleCG"]
        #         sale_of_land_build_lt = schedule_cg.get("LongTermCapGain", {}).get("SaleofLandBuild")
        #         if sale_of_land_build_lt and sale_of_land_build_lt.get("SaleofLandBuildDtls") and isinstance(
        #             sale_of_land_build_lt["SaleofLandBuildDtls"], dict):
        #             exemption_details_lt = sale_of_land_build_lt["SaleofLandBuildDtls"].get("ExemptionOrDednUs54Dtls")
        #             if exemption_details_lt and isinstance(exemption_details_lt, list):
        #                 total_exemption_amount_lt = sum(item.get("ExemptionAmount", 0) for item in exemption_details_lt)
        #                 sale_of_land_build_lt["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionGrandTotal"] = total_exemption_amount_lt
        #             sale_of_land_build_lt["SaleofLandBuildDtls"] = [sale_of_land_build_lt["SaleofLandBuildDtls"]]
        #             if sale_of_land_build_lt.get("SaleofLandBuildDtls[0]"):
        #                 sale_of_land_build_lt["SaleofLandBuildDtls"] = [dict_merge(
        #                     sale_of_land_build_lt["SaleofLandBuildDtls"][0],
        #                     sale_of_land_build_lt.get("SaleofLandBuildDtls[0]"), add_keys=True)]
                            
        # # Process Short Term Capital Gain
        # sale_of_land_build_st = schedule_cg.get("ShortTermCapGain", {}).get("SaleofLandBuild")
        # if sale_of_land_build_st and sale_of_land_build_st.get("SaleofLandBuildDtls") and isinstance(
        #     sale_of_land_build_st["SaleofLandBuildDtls"], dict):
        #     exemption_details_st = sale_of_land_build_st["SaleofLandBuildDtls"].get("ExemptionOrDednUs54Dtls")
        #     if exemption_details_st and isinstance(exemption_details_st, list):
        #         total_exemption_amount_st = sum(item.get("ExemptionAmount", 0) for item in exemption_details_st)
        #         sale_of_land_build_st["SaleofLandBuildDtls"]["ExemptionOrDednUs54"]["ExemptionGrandTotal"] = total_exemption_amount_st
        #     sale_of_land_build_st["SaleofLandBuildDtls"] = [sale_of_land_build_st["SaleofLandBuildDtls"]]
        #     if sale_of_land_build_st.get("SaleofLandBuildDtls[0]"):
        #         sale_of_land_build_st["SaleofLandBuildDtls"] = [dict_merge(
        #             sale_of_land_build_st["SaleofLandBuildDtls"][0],
        #             sale_of_land_build_st.get("SaleofLandBuildDtls[0]"), add_keys=True)]

            # if itr6.get("ScheduleTR1") and "ScheduleTR" in itr6["ScheduleTR1"]:
            #     if isinstance(itr6["ScheduleTR1"]["ScheduleTR"],list):
            #         for i in itr6["ScheduleTR1"]["ScheduleTR"]:
            #             if "CountryCodeExcludingIndia" in i and "CountryName" in i:
            #                 if "-" in i["CountryCodeExcludingIndia"]:
            #                     val_1 = i["CountryCodeExcludingIndia"].split("-")[0].replace(" ","")
            #                     val_2 = i["CountryCodeExcludingIndia"].split("-")[1].replace(" ","")
            #                     i["CountryCodeExcludingIndia"] = val_1
            #                     i["CountryName"] = val_2.upper()
            # if itr6.get("ScheduleBBS") and itr6["ScheduleBBS"].get("BBS"):
            #     data = itr6["ScheduleBBS"].get("BBS")
            #     for e in data:
            #         if "Slno" in e and "DateOfDeclareDividProfDomesComp" in e:
            #             formatted_val = datetime.datetime.strptime(e["DateOfDeclareDividProfDomesComp"],"%d/%m/%Y")\
            #                 .strftime(str(e["Slno"])+"-"+"%d-%b-%Y")
            #             if itr6.get("ScheduleBBS") and itr6["ScheduleBBS"].get("BBS1"):
            #                 check_v = itr6["ScheduleBBS"].get("BBS1")
            #                 if "TaxPaymentOnDDTndBBS" in check_v:
            #                     for ei in itr6["ScheduleBBS"]["BBS1"]["TaxPaymentOnDDTndBBS"]:
            #                         if "Slno" in ei:
            #                             if formatted_val==ei["Slno"]:
            #                                 _temp = copy.deepcopy(ei)
            #                                 if "TaxPaymentOnDDTndBBS" in e :
            #                                     e["TaxPaymentOnDDTndBBS"].append(_temp)
            #                                 else:
            #                                     e["TaxPaymentOnDDTndBBS"] = [_temp]

            def safe_int(value):
                try:
                    return int(value)
                except ValueError:
                    return 0

            if (safe_int(itr6.get("Schedule80_IC", {}).get("TotSchedule80_IC", 0)) > 0
                or safe_int(itr6.get("Schedule80_IA", {}).get("TotSchedule80_IA", 0)) > 0
                or safe_int(itr6.get("Schedule80_IB", {}).get("TotSchedule80_IB", 0)) > 0):
                
                for _obj in Schedule80_IA_config:
                    add_sch80locordesccode(_obj["parent"], _obj["child"], _obj["value"], itr6)
                
                for _obj in Schedule80_IB_config:
                    add_sch80locordesccode(_obj["parent"], _obj["child"], _obj["value"], itr6)
                
                for _obj in Schedule80_IC_config:
                    add_sch80locordesccode(_obj["parent"], _obj["child"], _obj["value"], itr6)
                
                for _obj in Schedule80_IC_DeductInNorthEast_config:
                    add_sch80locordesccode_child(_obj["parent"], _obj["child"], _obj["s_child"], _obj["value"], itr6)
            else:
                if (safe_int(itr6.get("Schedule80_IC", {}).get("TotSchedule80_IC", 0)) == 0
                    and safe_int(itr6.get("Schedule80_IA", {}).get("TotSchedule80_IA", 0)) == 0
                    and safe_int(itr6.get("Schedule80_IB", {}).get("TotSchedule80_IB", 0)) == 0):
                    
                    if "Schedule80_IC" in itr6:
                        del itr6["Schedule80_IC"]
                    
                    if "Schedule80_IB" in itr6:
                        del itr6["Schedule80_IB"]
                    
                    if "Schedule80_IA" in itr6:
                        del itr6["Schedule80_IA"]


            for validate_val in VALIDATE_VALUE:
                split_and_set_countrycodeexcludingindia(validate_val,itr6)
                

            if itr6.get("ScheduleTR1") and "ScheduleTR" in itr6["ScheduleTR1"]:
                if isinstance(itr6["ScheduleTR1"]["ScheduleTR"],list):
                    for i in itr6["ScheduleTR1"]["ScheduleTR"]:
                        if "CountryCodeExcludingIndia" in i and "CountryName" in i:
                            if "-" in i["CountryCodeExcludingIndia"]:
                                val_1 = i["CountryCodeExcludingIndia"].split("-")[0].replace(" ","")
                                val_2 = i["CountryCodeExcludingIndia"].split("-")[1].replace(" ","")
                                i["CountryCodeExcludingIndia"] = val_1
                                i["CountryName"] = val_2.upper()

            if itr6.get("ScheduleBBS") and itr6["ScheduleBBS"].get("BBS"):
                data = itr6["ScheduleBBS"].get("BBS")
                if itr6.get("ScheduleBBS1") and itr6["ScheduleBBS1"].get("BBS"):
                    val =  itr6["ScheduleBBS1"].get("BBS")
                    if isinstance(val,list):
                        for dd in data:
                            dd["TaxPaymentOnDDTndBBS"] = val
                if isinstance(data,list):
                    for i in data:
                        if "TaxPaymentOnDDTndBBS" in i:
                            i["TotalOfBBS"]=get_sum(i.get("TaxPaymentOnDDTndBBS"),"Amt")
                        else:
                            i["TotalOfBBS"]=0
    
            if itr6.get("ScheduleBBS") and itr6["ScheduleBBS"].get("BBS"):
                data = itr6["ScheduleBBS"]["BBS"]
                for e in data:
                    if "Slno" in e and "DateOfDeclareDividProfDomesComp" in e:
                        formatted_val = datetime.datetime.strptime(e["DateOfDeclareDividProfDomesComp"],"%d/%m/%Y")\
                            .strftime(str(e["Slno"])+"-"+"%d-%b-%Y")
                        if itr6.get("ScheduleBBS") and itr6["ScheduleBBS"].get("BBS1"):
                            check_v = itr6["ScheduleBBS"].get("BBS1")
                            if "TaxPaymentOnDDTndBBS" in check_v:
                                for ei in itr6["ScheduleBBS"]["BBS1"]["TaxPaymentOnDDTndBBS"]:
                                    if "Slno" in ei:
                                        if formatted_val==ei["Slno"]:
                                            _temp = copy.deepcopy(ei)
                                            if "TaxPaymentOnDDTndBBS" in e :
                                                e["TaxPaymentOnDDTndBBS"].append(_temp)
                                            else:
                                                e["TaxPaymentOnDDTndBBS"] = [_temp]

                        

    @staticmethod
    def priority_validation(payload, response, workbook):
        '''
        Summery Line
            Here we are validating the business validation on excel data
        Parameters:
            payload(dict): json payload
            response(dict): response body
            workbook: workbook
        Response:
            None
        '''
        error_list = []
        IsValid=True
        for key, method in PRIORITY_DICT.items():
            method(payload, error_list, workbook)
        if error_list:
            if "business_errors" not in response["json_error"]:
                response["json_error"]["business_errors"] = error_list
                response["status"] = False
                IsValid=False
            else:
                response["json_error"]["business_errors"].extend(error_list)
        return IsValid

    @staticmethod
    def buinsess_error_gen(payload, response):
        '''
        Summery Line
            business validation
        Parameters:
            payload(dict): business validation
            response(dict): response body
        Return:
            Generated Error list
        '''
        error_list = []
        for key, method in METHOD_DICT.items():
            method(payload, error_list)
        # if error_list:
        #     response["json_error"]["business_errors"] = error_list
        #     response["status"] = False
        return error_list


    @staticmethod
    def business_error_on_file(payload, response, workbook):
        '''
        Summery Line
            Here we are validating the business validation on excel data
        Parameters:
            payload(dict): json payload
            response(dict): response body
            workbook: workbook
        Return:
            Generated Error list
        '''
        error_list = []
        for key, method in METHOD_DICT_FOR_FILE_DATA.items():
            method(payload, error_list, workbook)
        # if error_list:
        #     if "business_errors" not in response["json_error"]:
        #         response["json_error"]["business_errors"] = error_list
        #         response["status"] = False
        #     else:
        #         response["json_error"]["business_errors"].extend(error_list)
        # with open("business_error.json",'w') as f1:
        #     json.dump(error_list,f1,indent = 4)
        return error_list

    @staticmethod
    def priority_validation_first(response,from_payload, from_file):
        '''
        Summery Line
            business validation
            Display first priority validation 
        Parameters:
            response(dict): response body
            from_payload(dict): buinsess_error_gen
            from_file(dict): business_error_on_file
        Return:
            None
        '''
        error_list = from_payload + from_file

        for error in error_list:
            if error['name_range'] in source_range:
                error["name_range"] = source_range[error['name_range']]

        error_list.sort(key=lambda x: int(x.get("error_code", 0)))

        if error_list:
            response["json_error"]["business_errors"] = error_list
            response["status"] = False
    