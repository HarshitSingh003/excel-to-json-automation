'''
Summery Line
    Here we are validating the business validation for payload
'''


from os import stat
import copy
import datetime
try:
    from dateutil.relativedelta import relativedelta
except Exception:
    class relativedelta:
        """
        Minimal fallback used when python-dateutil is unavailable.
        Supports datetime +/- relativedelta(months=...).
        """

        def __init__(self, months=0, **_kwargs):
            self.months = int(months or 0)

        def __radd__(self, other):
            if not isinstance(other, datetime.datetime):
                return other
            total_months = (other.year * 12 + (other.month - 1)) + self.months
            year = total_months // 12
            month = total_months % 12 + 1
            # Preserve valid day for target month.
            if month == 2:
                leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
                max_day = 29 if leap else 28
            elif month in (4, 6, 9, 11):
                max_day = 30
            else:
                max_day = 31
            day = min(other.day, max_day)
            return other.replace(year=year, month=month, day=day)

        __add__ = __radd__
from .lists import list1, list2, list5, list7, list4_1, list4_2

class BusinessValidation:
    '''
    Summery Line
        Business validation
    '''

    def __init__(self):
        '''
        Summery Line
            object reperesentation
        '''
        pass
        # return "BusinessValidation object"

    @staticmethod
    def rule_654(payload,error_list,workbook):
        '''
        Summery Line
        ITR.ITR6.PartB-TI.CapGain.TotalCapGains
        ITR.ITR6.PartB-TI.IncomeFromHP
        ITR.ITR6.PartB-TI.IncFromOS.TotIncFromOS
        Value of ITR6PB_PGBP_Tot should match with Net_PGBP_Bef_Set_off
        ITR.ITR6.PartB-TI.ProfBusGain.TotProfBusGain
        '''
        try:
            value_range_data = workbook.defined_names["ITR6PB_PGBP_Tot"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            parb_totprof = sales_region.value
    

            value_range_data = workbook.defined_names["Net_PGBP_Bef_Set_off"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value_parb_totprof = sales_region.value
            if value_parb_totprof > 0 and parb_totprof != value_parb_totprof: #rule_654
                val_4 = parb_totprof - value_parb_totprof
                error_dict = {
                    "remark": f"There is a difference of INR {val_4} in the PGBP income reported in the ITR and Computation",
                    "validation_status": "Error",
                    "field_value": parb_totprof,
                    "field_name": "ITR.ITR6.PartB-TI.ProfBusGain.TotProfBusGain",
                    "error_code": "654",
                    "name_range": "ITR6PB_PGBP_Tot"
                }
                error_list.insert(0,error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_655(payload,error_list,workbook):
        '''
        Summery Line
        ITR.ITR6.PartB-TI.IncFromOS.TotIncFromOS
        Value of ITR6PB_IFOS_Tot should match with Computation_OS
        '''
        try:
            sheet = workbook["Income from Other Sources"]
            incformos = sheet['F64'].value

            value_range_data = workbook.defined_names["Computation_OS"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str): #rule_655
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value_incformos = sales_region.value
            if incformos != value_incformos:
                val_2 = incformos - value_incformos
                error_dict = {
                    "remark": f"There is a difference of INR {val_2} in the IFOS income reported in the ITR and Computation",
                    "validation_status": "Error",
                    "field_value": value_incformos,
                    "field_name":  f"",
                    "error_code": "655",
                    "name_range": "Computation_OS"
                }
                error_list.insert(0,error_dict)
        except Exception:
            pass
            
    @staticmethod
    def rule_656(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6PB_CG_Tot should match with Computation_CG
        ITR.ITR6.PartB-TI.CapGain.TotalCapGains
        '''
        try:
            value_range_data = workbook.defined_names["ITR6PB_CG_Tot"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            parb_totcap = sales_region.value

            value_range_data = workbook.defined_names["Computation_CG"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value_parb_totcap = sales_region.value
            if parb_totcap != value_parb_totcap: #rule_656
                val_3 = parb_totcap - value_parb_totcap
                error_dict = {
                    "remark": f"There is a difference of INR {val_3} in the PGBP income reported in the ITR and Computation",
                    "validation_status": "Error",
                    "field_value": value_parb_totcap,
                    "field_name": f"",
                    "error_code": "656",
                    "name_range": "Computation_CG"
                }
                error_list.insert(0,error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_657(payload,error_list,workbook):
        '''
        Summery Line
        ITR.ITR6.PartB-TI.IncomeFromHP
        Value of ITR6PB_IFHP should match with Computation_HP
        Computation_HP
        '''
        try:
            value_range_data = workbook.defined_names["ITR6PB_IFHP"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            income_from_hp = sales_region.value

            value_range_data = workbook.defined_names["Computation_HP"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value_income_from_hp = sales_region.value
            if income_from_hp != value_income_from_hp: #rule_657
                val_1 = income_from_hp - value_income_from_hp
                error_dict = {
                    "remark": f"There is a difference of INR {val_1} in the PGBP income reported in the ITR and Computation",
                    "validation_status": "Error",
                    "field_value": value_income_from_hp,
                    "field_name": f"",
                    "error_code": "657",
                    "name_range": "Computation_HP"
                }
                error_list.insert(0,error_dict)
        except Exception:
            pass

    
    @staticmethod
    def rule_1(payload, error_list):
        '''
        Summery Line
            "Assessee mentioned country as India in the ""Personal
            Information"" then user should not quote mobile number less
            than or more than 10 digits"
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["Address"]["CountryCode"] == "91" and \
                len(str(payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["Address"]["MobileNo"])) != 10:
                error_dict = {
                    "remark": "Length of mobile number should be equal to 10 digits",
                    "field_name": "ITR.ITR6.PartA_GEN1.OrgFirmInfo.Address.MobileNo",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["Address"]["MobileNo"],
                    "error_code": "1",
                    "name_range": "ITR6PAG1_Mobile_1"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2(payload, error_list):
        '''
        Summery Line
            "If Assessee is liable for audit u/s 44AB and the flag is Y for
            accounts have been audited by an accountant, information
            relating to auditor and audit report should be furnished"
        '''
        error_dict = {
            "remark": "If assessee is liable for audit u/s 44AB and the flag is 'Y' for "\
                "accounts have been audited by an accountant, information relating to "\
                "auditor and audit report should be furnished",
            "field_name": "",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2",
            "name_range": ""
        }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["LiableSec44ABflg"] == "Y":
                audit_fields = [
                ("AuditorName", "ITR6PAG1_Auditor_TAR"),
                ("AuditorMemNo", "ITR6PAG1_Auditor_Mem"),
                ("AudFrmName", "ITR6PAG1_Auditor_Firm"),
                ("AudFrmRegNo", "ITR6PAG1_Firm_Mem"),
                ("AudFrmPAN", "ITR6PAG1_Aud_Firm_PAN"),
                ("AudFrmAadhaar", "ITR6PAG1_Aadh_Auditor"),
                ("AuditDate", "ITR6PAG1_Date_of_TAR"),
            ]

            for field, name_range in audit_fields:
                if not payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditInfo"][field]:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = f"ITR.ITR6.PartA_GEN2For6.AuditInfo.{field}"
                    copy_error["name_range"] = name_range
                    error_list.append(copy_error)

        except Exception:
            pass

    @staticmethod
    def rule_3(payload, error_list):
        '''
        Summery Line
            "Field Whether assessee is declaring income only under section 44AE/44B/44BB/44BBA/44BBB/44BBC cannot be blank"
        '''
        try:
            if not payload["ITR"]["ITR6"]["PartA_GEN2For6"].get("IncDclrdUs", None):
                error_dict = {
                    "remark": "Field Whether assessee is declaring income only under section 44AE/44B/44BB/44BBA/44BBB/44BBC cannot be blank",
                    "field_name": "ITR.ITR6.PartA_GEN2For6.IncDclrdUs",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "3",
                    "name_range": "ITR6PAG1_Pres_Inc"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    # @staticmethod
    # def rule_4(payload, error_list):
    #     '''
    #     Summery Line
    #         "If Assessee selects field Whether assessee is declaring income
    #             only under section 44AE/44B/44BB/44BBA/44BBB as no, then
    #             a2i, a2ii and a2iii cannot be left blank"
    #     '''
    #     error_dict = {
    #         "remark": "If assessee selects field Whether assessee is declaring income "\
    #             "only under section 44AE/44B/44BB/44BBA/44BBB/44BBC as no, then"\
    #             "a2i, a2ii and a2iii cannot be left blank",
    #         "field_name": "",
    #         "validation_status": "Error",
    #         "field_value": "",
    #         "error_code": "4",
    #         "name_range": ""
    #     }
    #     try:
    #         if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["LiableSec44AAflg"] == "Y":
    #             if "IncDclrdUs" in payload["ITR"]["ITR6"]["PartA_GEN2For6"] and payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"] == "Y":
    #                 cash_fields = [
    #                         ("AgrOFAllAmtsRcvd", "ITR6PAG1_Cash_recpt_ex_5perc"),
    #                         ("AgrOFAllPayMade", "ITR6PAG1_Cash_pay_ex_5perc"),
    #                     ]

    #         for field, name_range in cash_fields:
    #             if not field in payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
    #                 copy_error = copy.deepcopy(error_dict)
    #                 copy_error["field_name"] = f"ITR.ITR6.PartA_GEN2For6.{field}"
    #                 copy_error["name_range"] = name_range
    #                 error_list.append(copy_error)

    #             if "IncDclrdUs" in payload["ITR"]["ITR6"]["PartA_GEN2For6"] and payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"] == "N":
    #                 if not "TotalSalesExcOneCr" in payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
    #                     copy_error = copy.deepcopy(error_dict)
    #                     copy_error["field_name"] = "ITR.ITR6.PartA_GEN2For6.TotalSalesExcOneCr"
    #                     copy_error["name_range"] = "ITR6PAG1_Sal_1_10_Cr"
    #                     error_list.append(copy_error)
                
    #     except Exception:
    #         pass
    
    @staticmethod
    def rule_4(payload, error_list):
        '''
        Summery Line
        If ITR6PAG1_Pres_Inc (ITR.ITR6.PartA_GEN2For6.IncDclrdUs) is 'Y'
        "Then
        ITR6PAG1_Sal_1_10_Cr, (ITR.ITR6.PartA_GEN2For6.TotalSalesExcOneCr) 
        ITR6PAG1_Cash_recpt_ex_5perc,  (ITR.ITR6.PartA_GEN2For6.AgrOFAllAmtsRcvd)
        ITR6PAG1_Cash_pay_ex_5perc (ITR.ITR6.PartA_GEN2For6.AgrOFAllPayMade) 
        cannot be blank"
        '''
        error_dict = {
            "remark": "If assessee selects field Whether assessee is declaring income only under section 44AE/44B/44BB/44BBA/44BBB/44BBC as no, then a2i, a2ii and a2iii cannot be left blank",
            "field_name": "",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "5",
            "name_range": "ITR6PAG1_Pres_Inc"
        }
        try:
            partA = payload["ITR"]["ITR6"].get("PartA_GEN2For6", {})

            pres_inc = partA.get("IncDclrdUs", "").strip()

            if pres_inc == "Y":
                total_sales = partA.get("TotalSalesExcOneCr", "")
                cash_receipt = partA.get("AgrOFAllAmtsRcvd", "")
                cash_payment = partA.get("AgrOFAllPayMade", "")

                if not total_sales or not cash_receipt or not cash_payment:
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_5(payload, error_list):
        '''
        Summery Line
            "If Assessee selects field, whether during the year total
                sales/turnover/gross receipts of business exceeds 1 Crore Rupees
                but does not exceed 10 Crore Rupees as Yes, a2ii & a2iii cannot
                be left blank"
        '''
        error_dict = {
            "remark": "If assessee selects field, whether during the year total "\
                "sales/turnover/gross receipts of business exceeds 1 Crore Rupees "\
                "but does not exceed 10 Crore Rupees as Yes, a2ii & a2iii cannot be left blank",
            "field_name": "",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "5",
            "name_range": ""
        }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["TotalSalesExcOneCr"] == "Y":
               cash_fields = [
                ("AgrOFAllAmtsRcvd", "ITR6PAG1_Cash_recpt_ex_5perc"),
                ("AgrOFAllPayMade", "ITR6PAG1_Cash_pay_ex_5perc"),
            ]

            for field, name_range in cash_fields:
                if field not in payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = f"ITR.ITR6.PartA_GEN2For6.{field}"
                    copy_error["name_range"] = name_range
                    error_list.append(copy_error)
                    # error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_6(payload, error_list):
        '''
        Summery Line
            "In part A general, Date of audit report cannot be greater than
            system date"
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditInfo"]["AuditDate"]:
                current_date = datetime.datetime.now().date()
                date_obj = datetime.datetime.strptime(
                    payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditInfo"]["AuditDate"], "%Y-%m-%d").date()
                if date_obj > current_date:
                    error_dict = {
                        "remark": "In Part A general, date of audit report cannot be greater than today's date",
                        "field_name": "ITR.ITR6.PartA_GEN2For6.AuditInfo.AuditDate",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditInfo"]["AuditDate"],
                        "error_code": "6",
                        "name_range": "ITR6PAG1_Date_of_TAR"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_7(payload, error_list):
        '''
        Summery Line
            "Type of company is selected as foreign company then Section
                115BA/115BAA/115BAB is not applicable."

        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["DomesticCompFlg"] == "N":
                if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115BA"):
                    error_dict = {
                        "remark": "Type of company is selected as foreign company then "\
                            "Section 115BA/115BAA/115BAB is not applicable",
                        "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.Section115BA",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115BA"),
                        "error_code": "7",
                        "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_9(payload, error_list):
        '''
        Summery Line
            "Domestic company cannot be a non-resident"

        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["DomesticCompFlg"] == "Y" and \
                payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("ResidentialStatus") and \
                payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("ResidentialStatus").upper() == "NRI":
                error_dict = {
                    "remark": "Domestic company cannot be a Non-resident",
                    "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.ResidentialStatus",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("ResidentialStatus"),
                    "error_code": "9",
                    "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    # @staticmethod
    # def rule_375(payload, error_list):
    #     '''
    #     Summery Line
    #         "In Schedule OS, Sl. No. 10 the quarterly break up of Dividend
    #         Income should be equal to amount in Sl. No. 1a(i) i.e, normal
    #         dividend – DTAA for Dividend subject to TRC -Adj Expenditure u/s
    #         57(i)
    #         Adj Expenditure u/s 57(i) = Max (0, exp u/s 57(1) at Sl. No. 3c –
    #         Deemed dividend u/s 2(22e) at sl.no.1a(ii) )"

    #     '''
    #     try:
    #         if payload["ITR"]["ITR6"]["ScheduleOS"].get("IncOthThanOwnRaceHorse") and \
    #             isinstance(payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("DividendGross", 0), (int, float)) and \
    #             payload["ITR"]["ITR6"]["ScheduleOS"]["DividendIncUs115BBDA"].get("DateRange"):
    #             upto15of6 = payload["ITR"]["ITR6"]["ScheduleOS"]["DividendIncUs115BBDA"]["DateRange"].get("Upto15Of6", 0)
    #             up16of6to15of9 = payload["ITR"]["ITR6"]["ScheduleOS"]["DividendIncUs115BBDA"]["DateRange"].get("Up16Of6To15Of9", 0)
    #             up16of9to15of12 = payload["ITR"]["ITR6"]["ScheduleOS"]["DividendIncUs115BBDA"]["DateRange"].get("Up16Of9To15Of12", 0)
    #             up16of12to15of3 = payload["ITR"]["ITR6"]["ScheduleOS"]["DividendIncUs115BBDA"]["DateRange"].get("Up16Of12To15Of3", 0)
    #             up16of3to31of3 = payload["ITR"]["ITR6"]["ScheduleOS"]["DividendIncUs115BBDA"]["DateRange"].get("Up16Of3To31Of3", 0)
    #             if isinstance(upto15of6, (int, float)) and isinstance(up16of9to15of12, (int, float)) and \
    #                 isinstance(up16of6to15of9, (int, float)) and isinstance(up16of12to15of3, (int, float)) and \
    #                 isinstance(up16of3to31of3, (int, float)):
    #                 sum_amount = int(round(upto15of6 + up16of6to15of9 + up16of9to15of12 + up16of12to15of3 + up16of3to31of3, 2))
    #                 dividendgross = payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("DividendGross", 0)
    #                 if dividendgross != sum_amount:
    #                     error_dict = {
    #                         "remark": "In Schedule OS : Quarterly break is matching with the amount of income reported",
    #                         "field_name": "ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.DividendGross",
    #                         "validation_status": "Error",
    #                         "field_value": payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("DividendGross", 0),
    #                         "error_code": "375",
    #                         "name_range": "ITR6OS_Lott"
    #                     }
    #                     error_list.append(error_dict)
    #     except Exception:
    #         pass

    @staticmethod
    def rule_376(payload, error_list):
        '''
        Summery Line
            "In Schedule OS, Sl. No. 10 the quarterly break up of Income by
            way of winnings from lotteries, crossword puzzles, races, games,
            gambling, betting etc. referred to in section 2(24)(ix) should be
            equal to Sl. No. 2a Winnings from lotteries, crossword puzzles etc.
            chargeable u/s 115BB"
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleOS"].get("IncOthThanOwnRaceHorse") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("LtryPzzlChrgblUs115BB", 0), (int, float)) and \
                payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmLottery"].get("DateRange"):
                upto15of6 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmLottery"]["DateRange"].get("Upto15Of6", 0)
                up16of6to15of9 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmLottery"]["DateRange"].get("Up16Of6To15Of9", 0)
                up16of9to15of12 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmLottery"]["DateRange"].get("Up16Of9To15Of12", 0)
                up16of12to15of3 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmLottery"]["DateRange"].get("Up16Of12To15Of3", 0)
                up16of3to31of3 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmLottery"]["DateRange"].get("Up16Of3To31Of3", 0)
                if isinstance(upto15of6, (int, float)) and isinstance(up16of9to15of12, (int, float)) and \
                    isinstance(up16of6to15of9, (int, float)) and isinstance(up16of12to15of3, (int, float)) and \
                    isinstance(up16of3to31of3, (int, float)):
                    sum_amount = int(round(upto15of6 + up16of6to15of9 + up16of9to15of12 + up16of12to15of3 + up16of3to31of3, 2))
                    ltrypzzlchrgblus115bb = payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("LtryPzzlChrgblUs115BB", 0)
                    if ltrypzzlchrgblus115bb != sum_amount:
                        error_dict = {
                            "remark": "In Schedule OS : Quarterly break is matching with the amount of income reported",
                            "field_name": "ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.LtryPzzlChrgblUs115BB",
                            "validation_status": "Error",
                            "field_value": payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("LtryPzzlChrgblUs115BB", 0),
                            "error_code": "376",
                            "name_range": "ITR6OS_Lott"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_593(payload, error_list):
        '''
        Summery Line
            "In Schedule TDS -1 or TDS-2, Unclaimed TDS brought forward &
            details of TDS of current FY should be provided in different rows"
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleTDS2"].get("TDS3onOthThanSalDtls") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"], list):
                for index, row in enumerate(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"]):
                    if row.get("BroughtFwdTDSAmt") and row.get("TaxDeductCreditDtls", {}).get("TaxDeductedOwnHands"):
                        error_dict = {
                            "remark": "In ITR6_Part_A2_Details if Col 6 [Amount b/f] has values, "\
                                "then Col 7 [Deducted in own hands] should be blank",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDS3onOthThanSalDtls[{index+1}].TaxDeductCreditDtls.TaxDeductedOwnHands",
                            "validation_status": "Error",
                            "field_value": row.get("TaxDeductCreditDtls", {}).get("TaxDeductedOwnHands"),
                            "error_code": "593",
                            "name_range": "ITR6_Part_A2_Details"
                        }
                        error_list.append(error_dict)
                    elif row.get("TaxDeductCreditDtls", {}).get("TaxDeductedOwnHands") and row.get("BroughtFwdTDSAmt"):
                        error_dict = {
                            "remark": "In ITR6_Part_A2_Details if Col 7 [Deducted in own hands] has values, "\
                                "then Col 6 [Amount b/f] should be blank",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDS3onOthThanSalDtls[{index+1}].BroughtFwdTDSAmt",
                            "validation_status": "Error",
                            "field_value": row.get("BroughtFwdTDSAmt"),
                            "error_code": "1",
                            "name_range": "ITR6_Part_A2_Details"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_595(payload, error_list):
        '''
        Summery Line
            "In Schedule TDS, 15B2, Details of TDS on Income (As per
            16B/16C/16D furnished by Deductor), if TDS is claimed then
            Corresponding Income offered – “Gross Amount “ and “Head of
            Income” is to be mandatorily filled."
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleTDS2"].get("TDSOthThanSalaryDtls") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDSOthThanSalaryDtls"], list):
                for index, row in enumerate(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDSOthThanSalaryDtls"]):
                    if row.get("TaxDeductCreditDtls") and row["TaxDeductCreditDtls"].get("TaxClaimedOwnHands") and \
                        row["TaxDeductCreditDtls"].get("TaxClaimedOwnHands") > 0 and not row.get("GrossAmount") and \
                        not row.get("HeadOfIncome"):
                        error_dict = {
                            "remark": "In Schedule TDS : details of TDS on income if TDS is claimed then Corresponding "\
                                "Income offered – “Gross Amount “ and “Head of Income” is to be mandatorily filled.",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDSOthThanSalaryDtls[{index + 1}].GrossAmount",
                            "validation_status": "Error",
                            "field_value": row.get("GrossAmount"),
                            "error_code": "595",
                            "name_range": "ITR6_Part_A_Details"
                        }
                        error_list.append(error_dict)
                        error_dict = {
                            "remark": "In Schedule TDS : details of TDS on income if TDS is claimed then Corresponding "\
                                "Income offered – “Gross Amount “ and “Head of Income” is to be mandatorily filled.",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDSOthThanSalaryDtls[{index + 1}].HeadOfIncome",
                            "validation_status": "Error",
                            "field_value": row.get("HeadOfIncome"),
                            "error_code": "595",
                            "name_range": "ITR6_Part_A_Details"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_596(payload, error_list):
        '''
        Summery Line
            "In Schedule TDS, 15B2, Details of TDS on Income (As per
            16B/16C/16D furnished by Deductor), if TDS is claimed then
            Corresponding Income offered – “Gross Amount “ and “Head of
            Income” is to be mandatorily filled."
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleTDS2"].get("TDS3onOthThanSalDtls") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"], list):
                for index, row in enumerate(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"]):
                    if row.get("TaxDeductCreditDtls") and row["TaxDeductCreditDtls"].get("TaxClaimedOwnHands") and \
                        row["TaxDeductCreditDtls"].get("TaxClaimedOwnHands") > 0 and not row.get("GrossAmount") and \
                        not row.get("HeadOfIncome"):
                        error_dict = {
                            "remark": "In Schedule TDS : details of TDS on income if TDS is claimed then Corresponding "\
                                "Income offered – “Gross Amount “ and “Head of Income” is to be mandatorily filled.",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDS3onOthThanSalDtls[{index + 1}].GrossAmount",
                            "validation_status": "Error",
                            "field_value": row.get("GrossAmount"),
                            "error_code": "596",
                            "name_range": "ITR6_Part_A2_Details"
                        }
                        error_list.append(error_dict)
                        error_dict = {
                            "remark": "In Schedule TDS : details of TDS on income if TDS is claimed then Corresponding "\
                                "Income offered – “Gross Amount “ and “Head of Income” is to be mandatorily filled.",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDS3onOthThanSalDtls[{index + 1}].HeadOfIncome",
                            "validation_status": "Error",
                            "field_value": row.get("HeadOfIncome"),
                            "error_code": "596",
                            "name_range": "ITR6_Part_A2_Details"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_599(payload, error_list):
        '''
        Summery Line
            "In Schedule TDS 1 or TDS-2, if TDS credit relating to other person
            is selected the PAN of other person shall be provided mandatorily"
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleTDS2"].get("TDSOthThanSalaryDtls") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDSOthThanSalaryDtls"], list):
                for index, row in enumerate(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDSOthThanSalaryDtls"]):
                    if row.get("TDSCreditName") and row.get("TDSCreditName") == "O" and not row.get("PANofOtherPerson"):
                        error_dict = {
                            "remark": "In Schedule TDS 1 or TDS-2, if TDS credit relating to other person is "\
                                "selected the PAN of other person shall be provided mandatorily",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDSOthThanSalaryDtls[{index + 1}].PANofOtherPerson",
                            "validation_status": "Error",
                            "field_value": row.get("PANofOtherPerson"),
                            "error_code": "599",
                            "name_range": "ITR6_Part_A_Details"
                        }
                        error_list.append(error_dict)
            if payload["ITR"]["ITR6"]["ScheduleTDS2"].get("TDS3onOthThanSalDtls") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"], list):
                for index, row in enumerate(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"]):
                    if row.get("TDSCreditName") and row.get("TDSCreditName") == "O" and not row.get("PANofOtherPerson"):
                        error_dict = {
                            "remark": "In Schedule TDS 1 or TDS-2, if TDS credit relating to other person is "\
                                "selected the PAN of other person shall be provided mandatorily",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDS3onOthThanSalDtls[{index + 1}].PANofOtherPerson",
                            "validation_status": "Error",
                            "field_value": row.get("PANofOtherPerson"),
                            "error_code": "599",
                            "name_range": "ITR6_Part_A_Details"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_600(payload, error_list):
        '''
        Summery Line
            "In Schedule TDS, 15B1, Details of TDS on Income (As per 16A
            furnished by Deductor) or Schedule TDS, 15B2, Details of TDS on
            Income (As per 16B/16C/16D furnished by Deductor), if TDS
            credit relating to other person is selected then TAN of the
            Deductor/ PAN of Tenant/ Buyer should be filled"
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleTDS2"].get("TDSOthThanSalaryDtls") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDSOthThanSalaryDtls"], list):
                for index, row in enumerate(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDSOthThanSalaryDtls"]):
                    if row.get("TaxDeductCreditDtls", {}).get("TaxDeductedOwnHands") and \
                        row.get("TaxDeductCreditDtls", {}).get("TaxDeductedOwnHands") > 0 and \
                        not row.get("TANOfDeductor"):
                        error_dict = {
                            "remark": "In Schedule TDS, TDS credit claimed this year in Col. No. 9 cannot be "\
                                "more than Gross amount disclosed in Col. No. 11",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDSOthThanSalaryDtls[{index + 1}].TANOfDeductor",
                            "validation_status": "Error",
                            "field_value": row.get("TANOfDeductor"),
                            "error_code": "600",
                            "name_range": "ITR6_Part_A_Details"
                        }
                        error_list.append(error_dict)
            if payload["ITR"]["ITR6"]["ScheduleTDS2"].get("TDS3onOthThanSalDtls") and \
                isinstance(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"], list):
                for index, row in enumerate(payload["ITR"]["ITR6"]["ScheduleTDS2"]["TDS3onOthThanSalDtls"]):
                    if row.get("TaxDeductCreditDtls", {}).get("TaxDeductedOwnHands") and \
                        row.get("TaxDeductCreditDtls", {}).get("TaxDeductedOwnHands") > 0 and \
                        not row.get("PANOfBuyerTenant"):
                        error_dict = {
                            "remark": "Then Col 4 [Tax Deduction Account Number (TAN) of the Deductor] cannot be blank",
                            "field_name": f"ITR.ITR6.ScheduleTDS2.TDS3onOthThanSalDtls[{index + 1}].PANOfBuyerTenant",
                            "validation_status": "Error",
                            "field_value": row.get("PANOfBuyerTenant"),
                            "error_code": "600",
                            "name_range": "ITR6_Part_A_Details"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_644(payload,error_list):
        '''
        Summery Line
            If ITR6ChVIA_Dedn_80PA_SC is greater than 0 then 2nd column of ITR6_NatureOfBusiness should have 1001 to 
            ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80PA
            ITR.ITR6.PartA_GEN2For6.NatOfBus.NatureOfBusiness[0]
        '''
        try:
            if payload["ITR"]["ITR6"].get("ScheduleVIA") and payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                if "Section80PA" in payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                    val = payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]["Section80PA"]
                    if val > 0 :
                        if payload["ITR"]["ITR6"]["ITR"]["ITR6"].get("PartA_GEN2For6") and payload["ITR"]["ITR6"]["PartA_GEN2For6"].get("NatOfBus"):
                            if "NatureOfBusiness" in payload["ITR"]["ITR6"]["PartA_GEN2For6"].get("NatOfBus"):
                                check = payload["ITR"]["ITR6"]["PartA_GEN2For6"]["NatOfBus"]["NatureOfBusiness"]
                                for i in check:
                                    if "Code" in i:
                                        if i["Code"] < "1001" or i["Code"] > "1018":
                                            error_dict = {
                                                "remark": "Deduction u/s 80PA shall not be allowed if the nature of business code is selected other than 1001 to 1018 from schedule nature of business",
                                                "validation_status": "Error",
                                                "field_value": val,
                                                "field_name": f"",
                                                "error_code": "644",
                                                "name_range": "ITR6ChVIA_Dedn_80PA_SC"
                                            }
                                            error_list.append(error_dict)
            if payload["ITR"]["ITR6"].get("PartA_GEN1") and payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus"):
                if "IsIfsc" in payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus"):
                    if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("IsIfsc") == "Y":
                        if payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA") and payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                            if "Section80LA" in payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                                val = payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA").get("Section80LA")
                                if val != 0:
                                    error_dict = {
                                        "remark": "Deduciton u/s 80LA(1) can be claimed only if response to the question “Whether assessee is located in an International "\
                                        "Financial Services Centre and derives income solely in convertible foreign exchange?” is selected as 'N'",
                                        "validation_status": "Error",
                                        "field_value": payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"].get("Section80LA"),
                                        "field_name": "ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80LA",
                                        "error_code": "644",
                                        "name_range": "ITR6ChVIA_Dedn_80LA_1_SC"
                                    }
                                    error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_645(payload,error_list):
        '''
        Summery Line
            If ITR6ChVIA_Dedn_80PA_SC is greater than 0 then 2nd column of ITR6_NatureOfBusiness should have 1001 to 
            ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80PA
            ITR.ITR6.PartA_GEN2For6.NatOfBus.NatureOfBusiness[0]
        '''
        error_dict = {
            "remark": "",
            "validation_status": "Error",
            "field_value": "",
            "field_name": "",
            "error_code": "645",
            "name_range": ""
        }
        try:
            # ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80M
            if payload["ITR"]["ITR6"].get("ScheduleVIA") and payload["ITR"]["ITR6"]["ScheduleVIA"].get("UsrDeductUndChapVIA"):
                if "Section80MDtls" in payload["ITR"]["ITR6"]["ScheduleVIA"].get("UsrDeductUndChapVIA"):
                    val = payload["ITR"]["ITR6"]["ScheduleVIA"].get("UsrDeductUndChapVIA").get("Section80MDtls")
                    for i in val:
                        if ("Section80MDate" in i and i["Section80MDate"] != None) or ("Section80MAmnt" in i and i["Section80MDate"] != None) or ("Section80MType" in i and i["Section80MType"] != None):
                            if (i["Section80MDate"] == None or  i["Section80MDate"] == "") or (i["Section80MAmnt"] == None or  i["Section80MAmnt"] == "") or (i["Section80MType"] == None or  i["Section80MType"] == ""):
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["remark"] = "Deduction claimed u/s 80M cannot exceed dividend income offered in Schedule OS and Schedule BP subject to maximum of balance income under Schedule BFLA"
                                copy_error["field_value"] = val
                                copy_error["field_name"] = f""
                                copy_error["name_range"] = "ITR680M_Table"
                                error_list.append(copy_error)
            if payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]["Section80M"]:
                val_1 = payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]["Section80M"]
            else: 
                val_1 = 0
            if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncRecCredPLOthHeadDtls"]["Dividend"]:
                val_2 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncRecCredPLOthHeadDtls"]["Dividend"]
            else:
                val_2 = 0
            if payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"]["DividendGross"]:
                val_3 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"]["DividendGross"]
            else: 
                val_3 = 0
            if payload["ITR"]["ITR6"]["ScheduleBFLA"]["OthSrcExclRaceHorse"]["IncBFLA"]["IncOfCurYrAfterSetOffBFLosses"]:
                val_4 = payload["ITR"]["ITR6"]["ScheduleBFLA"]["OthSrcExclRaceHorse"]["IncBFLA"]["IncOfCurYrAfterSetOffBFLosses"]
            else:
                val_4 = 0
            comparisons = [
                (val_1, val_2),
                (val_1, val_3),
                (val_1, val_4),
            ]

            for v1, v2 in comparisons:
                if v1 > v2:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["remark"] = "Deduction claimed u/s 80M cannot exceed dividend income offered in Schedule OS and Schedule BP subject to maximum of balance income under Schedule BFLA"
                    copy_error["field_value"] = v1
                    copy_error["field_name"] = "ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80M"
                    copy_error["name_range"] = "ITR6ChVIA_Dedn_80M_SC"
                    error_list.append(copy_error)

        except Exception:
            pass

    @staticmethod
    def rule_646(payload, error_list):
        '''
        Summery Line
            "In Part A General “Name of the representative, Capacity of the
            representative, Address of the representative and Permanent
            Account Number (PAN)/ Aadhaar of the representative” is
            mandatory if in schedule “Verification” Verification capacity is
            selected as “Representative” from drop down"
        '''
        try:
            if payload["ITR"]["ITR6"]["Verification"].get("Declaration") and \
                payload["ITR"]["ITR6"]["Verification"]["Declaration"].get("Capacity") and \
                payload["ITR"]["ITR6"]["Verification"]["Declaration"].get("Capacity") == "RA":
                flag_filling_status = isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus"), dict) and \
                    payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus").get("AssesseeRep")
                if flag_filling_status:
                    if not flag_filling_status.get("RepName"):
                        error_dict = {
                            "remark": "In Part A General “Name of the representative, Capacity of the representative, "\
                                "Address of the representative and Permanent Account Number (PAN)/ Aadhaar of the representative” "\
                                    "is mandatory if in schedule “Verification” Verification capacity is selected as "\
                                    "“Representative” from drop down",
                            "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.AssesseeRep.RepName",
                            "validation_status": "Error",
                            "field_value": flag_filling_status.get("RepName"),
                            "error_code": "646",
                            "name_range": "ITR6PAG1_Name_Rep_Assessee"
                        }
                        error_list.append(error_dict)
                    if not flag_filling_status.get("RepCapacity"):
                        error_dict = {
                            "remark": "In Part A General “Name of the representative, Capacity of the representative, "\
                                "Address of the representative and Permanent Account Number (PAN)/ Aadhaar of the representative” "\
                                    "is mandatory if in schedule “Verification” Verification capacity is selected as "\
                                    "“Representative” from drop down",
                            "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.AssesseeRep.RepCapacity",
                            "validation_status": "Error",
                            "field_value": flag_filling_status.get("RepCapacity"),
                            "error_code": "646",
                            "name_range": "ITR6PAG1_Cap_Rep_Assessee"
                        }
                        error_list.append(error_dict)
                    if not flag_filling_status.get("RepAddress"):
                        required_fields = [
                ("RepAddress", "ITR6PAG1_Add_Rep_Assessee"),
                ("RepPAN", "ITR6PAG1_PAN_Rep_Assessee"),
                ("RepAadhaar", "ITR6PAG1_Aadh_Rep_Assessee"),
            ]

            for field, name_range in required_fields:
                if not flag_filling_status.get(field):
                    error_dict = {
                        "remark": "In Part A General “Name of the representative, Capacity of the representative, "\
                                "Address of the representative and Permanent Account Number (PAN)/ Aadhaar of the representative” "\
                                "is mandatory if in schedule “Verification” Verification capacity is selected as "\
                                "“Representative” from drop down",
                        "field_name": f"ITR.ITR6.PartA_GEN1.FilingStatus.AssesseeRep.{field}",
                        "validation_status": "Error",
                        "field_value": flag_filling_status.get(field),
                        "error_code": "646",
                        "name_range": name_range,
                    }
                    error_list.append(error_dict)

        except Exception:
            pass

    @staticmethod
    def rule_647(payload, error_list):
        '''
        Summery Line
            "In case of domestic company, PAN entered at “Verification”
            should match with any of the PAN entered at ""Key persons"""
        '''
        try:
            if payload["ITR"]["ITR6"]["Verification"].get("Declaration") and \
                payload["ITR"]["ITR6"]["Verification"]["Declaration"].get("AssesseeVerPAN"):
                keyperpan_flag = isinstance(payload["ITR"]["ITR6"]["PartA_GEN2For6"].get("KeyPersons"), list) and \
                    payload["ITR"]["ITR6"]["PartA_GEN1"].get("PartA_GEN2For6").get("KeyPersons")
                if keyperpan_flag:
                    pan = payload["ITR"]["ITR6"]["Verification"]["Declaration"].get("AssesseeVerPAN")
                    for index, row in enumerate(keyperpan_flag):
                        if row.get("KeyPerPAN") and row.get("KeyPerPAN") != pan:
                            error_dict = {
                            "remark": "In case of domestic company, PAN entered at “Verification” should "\
                                "match with any of the PAN entered at ""Key persons""",
                            "field_name": f"ITR.ITR6.PartA_GEN2For6.KeyPersons[{index+1}].KeyPerPAN",
                            "validation_status": "Error",
                            "field_value": row.get("KeyPerPAN"),
                            "error_code": "647",
                            "name_range": "KeyPersons"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_69(payload, error_list):
        '''
        Summery Line
            If ITR6PL_Paid_NR_Y_N is 'Y' then ITR6PL_Paid_NR_Amt cannot be Zero or null or blank
        '''
        try:
            if payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AnyCompPaidToNonRes"] == "Y" and \
                (payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AmtPaidToNonRes"] == None or \
                payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AmtPaidToNonRes"] == 0 or \
                payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AmtPaidToNonRes"] == "") :
                error_dict = {
                    "remark": "Part A P&L, If SI. No. 22xiia is yes then SI. No. 22xiib cannot be Zero or null or blank",
                    "field_name": "ITR.ITR6.PARTA_PL.DebitsToPL.DebitPlAcnt.EmployeeComp.AnyCompPaidToNonRes",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AnyCompPaidToNonRes"],
                    "error_code": "69",
                    "name_range": "ITR6PL_Paid_NR_Y_N"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_86(payload, error_list):
        '''
        Summery Line
            "In 'Schedule Profit & Loss A/c' in table 61(i) of 44AE, total of"\
                "column 4 'Number of months for which goods carriage was"\
                "owned / leased / hired by assessee' shall not exceed 120.",
        '''
        try:
            if payload["ITR"]["ITR6"]["PARTA_PL"]["TotalNumOfMonths"] > 120 :
                error_dict = {
                    "remark": "In 'Schedule Profit & Loss A/c' in table 61(i) of 44AE, total of"\
                                "column 4 'Number of months for which goods carriage was"\
                                "owned / leased / hired by assessee' shall not exceed 120.",
                    "field_name": "ITR.ITR6.PARTA_PL.TotalNumOfMonths",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["PARTA_PL"]["TotalNumOfMonths"],
                    "error_code": "86",
                    "name_range": "ITR6PL_PremInc_Month_Tot"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_92(payload, error_list):
        '''
        Summery Line
            If ITR6PL_PremInc_44AE_Tot_2 is greater than zero, then ITR6PL_PremInc_44AE_Table_1 cannot be blank
        '''
        try:
            if payload["ITR"]["ITR6"]["PARTA_PL"]["TotalPrsumptvIncUs44E"] > 0 and \
                len(payload["ITR"]["ITR6"]["PARTA_PL"]["GoodsDtlsUs44AE"])==0 :
                error_dict = {
                    "remark": "Part A P&L, the value at filed '61(ii)' is greater than zero then it"\
                                "is mandatory to fill details in table at Sl. No. 61",
                    "field_name": "ITR.ITR6.PARTA_PL.TotalPrsumptvIncUs44E",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["PARTA_PL"]["TotalPrsumptvIncUs44E"],
                    "error_code": "92",
                    "name_range": "ITR6PL_PremInc_44AE_Tot_2"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_104(payload, error_list):
        '''
        Summery Line
            "If ITR6PAG1_Pres_Inc is 'Y, then ITR6PL_No_Acc_NP_Sec44B cannot be les than 7.5% of ITR6PL_No_Acc_Exp_Sec44B"
        '''
        try:
            if payload["ITR"]["ITR6"]["PARTA_PLIndAS"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AnyCompPaidToNonRes"] == "Y" and\
                (payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AmtPaidToNonRes"] == None or \
                payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AmtPaidToNonRes"] == 0 or \
                payload["ITR"]["ITR6"]["PARTA_PL"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AmtPaidToNonRes"] == "") :
                error_dict = {
                    "remark": "Part A P&L, the value at filed '61(ii)' is greater than zero then it"\
                                " is mandatory to fill details in table at Sl. No. 61",
                    "field_name": "ITR.ITR6.PARTA_PLIndAS.DebitsToPL.DebitPlAcnt.EmployeeComp.AnyCompPaidToNonRes",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["PARTA_PLIndAS"]["DebitsToPL"]["DebitPlAcnt"]["EmployeeComp"]["AnyCompPaidToNonRes"],
                    "error_code": "104",
                    "name_range": "ITR6PLIndAS_Paid_NR_Y_N"
                }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_135(payload, error_list):
        '''
        Summery Line
            The value of ITR6HP1_Perc_Share should be 100
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["AssessePercentShareProp"] != 100 :
                error_dict = {
                    "remark": "In case of Co-owned property, the total of assessee’s share and"\
                                "co-owner's share should be equal to 100%"
                                "and In schedule HP, Assessee PAN & Co-Owner's PAN cannot be same.",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["AssessePercentShareProp"],
                    "field_name": f"",
                    "error_code": "135",
                    "name_range": "ITR6HP1_Perc_Share"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_138(payload, error_list):
        '''
        Summery Line
           If ITR6HP1_Gross_Rent is zero/ blank then ITR6HP1_Tax_Local_Auth cannot be more than zero
            ITR.ITR6.ScheduleHP.PropertyDetails[0].Rentdetails.LocalTaxes
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["Rentdetails"]["AnnualLetableValue"] != 0 and\
               payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["Rentdetails"]["AnnualLetableValue"] != "" and\
                payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["Rentdetails"]["LocalTaxes"] > 0:
                error_dict = {
                    "remark": "In Schedule HP, if annual value lettable value is zero or null then"\
                                "assessee cannot claim municipal tax.",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["Rentdetails"]["AnnualLetableValue"],
                    "field_name": f"",
                    "error_code": "138",
                    "name_range": "ITR6HP1_Gross_Rent"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_139(payload, error_list):
        '''
        Summery Line
           If ITR6HP1_Type is 'N - Self Occupied', then ITR6HP1_Int_Borr_Cap cannot be greater than 200,000
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["ifLetOut"] == "N - Self Occupied" and\
               payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["Rentdetails"]["IntOnBorwCap"] > 200000 :
                error_dict = {
                    "remark": "If the property is self occupied, the interest in borrowed capital cannot exceed 200,000",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["ifLetOut"],
                    "field_name": f"",
                    "error_code": "139",
                    "name_range": "ITR6HP1_Type"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_148(payload, error_list):
        '''
        Summery Line
           If ITR6PAG1_Opt_115BA_BAA_BAB_CY is '115BAB - Section 115BAB' then ITR6HP1_30_Prec cannot be greater than zero
           ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY
           ITR.ITR6.ScheduleHP.PropertyDetails[0].Rentdetails.ThirtyPercentOfBalance
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115CurrAY"] == "115BAB" and\
               payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["Rentdetails"]["ThirtyPercentOfBalance"] > 0 :
                error_dict = {
                    "remark": "In Schedule HP Standard deduction u/s 24(a) will not be allowed"\
                                "in case in assessee has opted for taxation u/s 115BAB",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["ifLetOut"],
                    "field_name": f"",
                    "error_code": "148",
                    "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_149(payload, error_list):
        '''
        Summery Line
           If ITR6PAG1_Opt_115BA_BAA_BAB_CY is '115BAB - Section 115BAB' then ITR6HP1_Int_Borr_Cap cannot be greater than zero
           ITR.ITR6.ScheduleHP.PropertyDetails[0].Rentdetails.IntOnBorwCap
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115CurrAY"] == "115BAB" and\
               payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["Rentdetails"]["IntOnBorwCap"] > 0 :
                error_dict = {
                    "remark": "In Schedule HP Interest payable on borrowed capital u/s 24(b)"
                            "will not be allowed in case in assessee has opted for taxation u/s 115BAB",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["ScheduleHP"]["PropertyDetails[0]"]["ifLetOut"],
                    "field_name": f"",
                    "error_code": "149",
                    "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_157(payload, error_list):
        '''
        Summery Line
           ITR6PGBP_Oth_OS_Div should not be more that sum(ITR6PL_Div_Inc, ITR6PLIndAS_Div_Inc)
           ITR.ITR6.CorpScheduleBP.BusinessIncOthThanSpec.IncRecCredPLOthHeadDtls.Dividend == 0
           ITR.ITR6.PARTA_PL.CreditsToPL.OthIncome.Dividends + ITR.ITR6.PARTA_PLIndAS.CreditsToPL.OthIncome.Dividends
        '''
        try:
            if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("IncRecCredPLOthHeadDtls") and \
                isinstance(payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncRecCredPLOthHeadDtls"].get("Dividend", 0), (int, float)) and \
                payload["ITR"]["ITR6"]["PARTA_PL"]["CreditsToPL"].get("OthIncome"):
                ITR6PL_Div_Inc = payload["ITR"]["ITR6"]["PARTA_PL"]["CreditsToPL"]["OthIncome"].get("Dividends",0)
                ITR6PLIndAS_Div_Inc = payload["ITR"]["ITR6"]["PARTA_PLIndAS"]["CreditsToPL"]["OthIncome"].get("Dividends",0)

                if isinstance(ITR6PL_Div_Inc, (int, float)) and isinstance(ITR6PLIndAS_Div_Inc, (int, float)):
                    sum_amount = int(round(ITR6PL_Div_Inc + ITR6PLIndAS_Div_Inc, 2))
                    ITR6PGBP_Oth_OS_Div = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncRecCredPLOthHeadDtls"].get("Dividend")
                    if sum_amount != ITR6PGBP_Oth_OS_Div:
                        error_dict = {
                            "remark": "In Schedule BP, Income reduced from Row no A3c (i) 'Dividend Income to be offered under Schedule OS'" \
                                "should not be more than Dividend income offered in Sl. No. 14(iii) Of P & L /P & L Ind As",
                            "field_name": "ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.DividendGross",
                            "validation_status": "Error",
                            "field_value": payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncRecCredPLOthHeadDtls"].get("Dividend"),
                            "error_code": "157",
                            "name_range": "ITR6PGBP_Oth_OS_Div"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_187(payload, error_list):
        '''
        Summery Line
        Value of ITR6PGBP_Oth_Exmpt_Tot cannot be less than ITR6EI_Amt_Tot 
        ITR.ITR6.CorpScheduleBP.BusinessIncOthThanSpec.IncCredPL.OthExempInc
        ITR.ITR6.ScheduleEI.Others
        '''
        
        try:
            if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("IncCredPL") and \
                isinstance(payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncCredPL"].get("OthExempInc", 0), (int, float)):
                ITR6PGBP_Oth_Exmpt_Tot = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncCredPL"].get("OthExempInc", 0)
                ITR6EI_Amt_Tot = 0
                if payload["ITR"]["ITR6"].get("ScheduleEI"):
                    ITR6EI_Amt_Tot = payload["ITR"]["ITR6"]["ScheduleEI"].get("Others")
                if ITR6PGBP_Oth_Exmpt_Tot < ITR6EI_Amt_Tot:
                    error_dict = {
                        "remark": "In Schedule BP, Income reduced from Row no A5 to be offered under Schedule EI should not be less than amount reduced from Schedule BP A5",
                        "field_name": "ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.DividendGross",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["IncRecCredPLOthHeadDtls"].get("Dividend"),
                        "error_code": "187",
                        "name_range": "ITR6PGBP_Oth_Exmpt_Tot"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_222(payload, error_list):
        '''
        Summery Line
           If ITR6PAG1_Opt_115BA_BAA_BAB_CY or ITR6PAG1_Opt_115BA_BAA_BAB_CY is not 'NA - None of above', then sum(ITR6DPM_AddlnDepn_15_4,
           ITR6DPM_AddlnDepn_30_4, ITR6DPM_AddlnDepn_40_4, ITR6DPM_AddlnDepn_45_4, ITR6DPM_AddlnDepn_15_7, ITR6DPM_AddlnDepn_30_7, ITR6DPM_AddlnDepn_40_7, 
           ITR6DPM_AddlnDepn_45_7, ITR6DPM_AddlnDepn_15_PY, ITR6DPM_AddlnDepn_30_PY, ITR6DPM_AddlnDepn_40_PY, ITR6DPM_AddlnDepn_45_PY) should be zero
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY", 0), (int, float)) and \
                payload["ITR"]["ITR6"]["ScheduleDPM"].get("PlantMachinery"):
                itr6pag1_opt_115ba_baa_bab_cy = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY")
                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions"):
                    itr6dpm_addlndepn_15_4 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_15_4 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions"):
                    itr6dpm_addlndepn_30_4 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_30_4 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions"):
                    itr6dpm_addlndepn_40_4 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_40_4 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions"):
                    itr6dpm_addlndepn_45_4 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_45_4 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions"):
                    itr6dpm_addlndepn_15_7 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("AddlnDeprOnGT180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_15_7 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("AddlnDeprDuringYearAdditions"):
                    itr6dpm_addlndepn_30_7 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("AddlnDeprDuringYearAdditions",0)
                else:
                    itr6dpm_addlndepn_30_7 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("AddlnDeprDuringYearAdditions"):
                    itr6dpm_addlndepn_40_7 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("AddlnDeprDuringYearAdditions",0)
                else:
                    itr6dpm_addlndepn_40_7 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("AddlnDeprDuringYearAdditions"):
                    itr6dpm_addlndepn_45_7 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("AddlnDeprDuringYearAdditions",0)
                else:
                    itr6dpm_addlndepn_45_7 = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions"):
                    itr6dpm_addlndepn_15_PY = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions",0)
                else: 
                    itr6dpm_addlndepn_15_PY = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions"):
                    itr6dpm_addlndepn_30_PY = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_30_PY = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions"):
                    itr6dpm_addlndepn_40_PY = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_40_PY = 0

                if payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions"):
                    itr6dpm_addlndepn_45_PY = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("AddlnDeprOnLessThan180DayAdditions",0)
                else:
                    itr6dpm_addlndepn_45_PY = 0

                if isinstance(itr6dpm_addlndepn_15_4, (int, float)) and isinstance(itr6dpm_addlndepn_30_4, (int, float)) and \
                    isinstance(itr6dpm_addlndepn_40_4, (int, float)) and isinstance(itr6dpm_addlndepn_45_4, (int, float)) and \
                    isinstance(itr6dpm_addlndepn_15_7, (int, float)) and isinstance(itr6dpm_addlndepn_30_7, (int, float)) and \
                    isinstance(itr6dpm_addlndepn_40_7, (int, float)) and isinstance(itr6dpm_addlndepn_45_7, (int, float)) and \
                    isinstance(itr6dpm_addlndepn_15_PY, (int, float)) and isinstance(itr6dpm_addlndepn_30_PY, (int, float)) and \
                    isinstance(itr6dpm_addlndepn_40_PY, (int, float)) and isinstance(itr6dpm_addlndepn_45_PY, (int, float)):
                    sum_amount = int(round(itr6dpm_addlndepn_15_4 + itr6dpm_addlndepn_30_4 + itr6dpm_addlndepn_40_4 + 
                                    itr6dpm_addlndepn_45_4 + itr6dpm_addlndepn_15_7 + itr6dpm_addlndepn_30_7 + 
                                    itr6dpm_addlndepn_40_7 + itr6dpm_addlndepn_45_7 + itr6dpm_addlndepn_15_PY + 
                                    itr6dpm_addlndepn_30_PY + itr6dpm_addlndepn_40_PY + itr6dpm_addlndepn_45_PY , 2))
                    
                    if itr6pag1_opt_115ba_baa_bab_cy == "NA" and sum_amount != 0:
                        error_dict = {
                            "remark": "In schedule DPM, additional depreciation is not allowed, if opted for lower taxation u/s 115BA or 115BAA or 115BAB",
                            "field_name": "ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.DividendGross",
                            "validation_status": "Error",
                            "field_value": payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY"),
                            "error_code": "222",
                            "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_223(payload, error_list):
        '''
        Summery Line
        ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY
        ITR.ITR6.PartA_GEN1.FilingStatus.SectionCurrAY
        If ITR6PAG1_Opt_115BA_BAA_BAB_CY or ITR6PAG1_Opt_115BA_BAA_BAB_Sec is not 'NA - None of above', then following should be less than 40%
        ITR6DPM_Depn_15_Tot/ (ITR6DPM_AmtDepn_15_Full_rate + ITR6DPM_AmtDepn_15_Half_rate) 
        ITR.ITR6.ScheduleDPM.PlantMachinery.Rate15.DepreciationDetail.TotalDepreciation / ITR.ITR6.ScheduleDPM.PlantMachinery.Rate15.DepreciationDetail.FullRateDeprAmt + ITR.ITR6.ScheduleDPM.PlantMachinery.Rate15.DepreciationDetail.HalfRateDeprAmt
        ITR6DPM_Depn_30_Tot/ (ITR6DPM_AmtDepn_30_Full_rate + ITR6DPM_AmtDepn_30_Half_rate)
        ITR6DPM_Depn_40_Tot/ (ITR6DPM_AmtDepn_40_Full_rate + ITR6DPM_AmtDepn_40_Half_rate)
        ITR6DPM_Depn_45_Tot/ (ITR6DPM_AmtDepn_45_Full_rate + ITR6DPM_AmtDepn_45_Half_rate)
        '''
        error_dict = {
            "remark": "In schedule DPM, depreciation claimed cannot be more than '40%' if opted for lower taxation u/s 115BA or 115BAA or 115BAB",
            "field_name": "",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "223",
            "name_range": ""
        }
        try:
            if (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY", 0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") != "N") or (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY",0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") != "NA - None of above"):
                    if "ScheduleDPM" in payload["ITR"]["ITR6"] and payload["ITR"]["ITR6"] and "PlantMachinery" in payload["ITR"]["ITR6"]["ScheduleDPM"]:
                        if "Rate15" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]:
                            if "DepreciationDetail" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]:
                                if "TotalDepreciation" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"] and \
                                    isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("TotalDepreciation") ,(int,float)):
                                    m_val = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("TotalDepreciation")
                                    if (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("FullRateDeprAmt") and \
                                        isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("FullRateDeprAmt"), (int,float))) or (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("HalfRateDeprAmt") and \
                                        isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("HalfRateDeprAmt"), (int,float))):
                                            s_val = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("FullRateDeprAmt") + payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate15"]["DepreciationDetail"].get("HalfRateDeprAmt")
                                            if round(m_val / s_val) > 40:
                                                copy_error = copy.deepcopy(error_dict)
                                                copy_error["field_value"] = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY")
                                                copy_error["field_name"] = "ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY"
                                                copy_error["name_range"] = "ITR6PAG1_Opt_115BA_BAA_BAB"
                                                error_list.append(copy_error)

            if (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY", 0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") != "N") or (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY",0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") != "NA - None of above"):
                    if "ScheduleDPM" in payload["ITR"]["ITR6"] and payload["ITR"]["ITR6"] and "PlantMachinery" in payload["ITR"]["ITR6"]["ScheduleDPM"]:
                        if "Rate30" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]:
                            if "DepreciationDetail" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]:
                                if "TotalDepreciation" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"] and \
                                    isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("TotalDepreciation") ,(int,float)):
                                        m_val_1 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("TotalDepreciation")
                                        if (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("FullRateDeprAmt") and\
                                            isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("FullRateDeprAmt"), (int,float))) or (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("HalfRateDeprAmt") and\
                                            isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("HalfRateDeprAmt"), (int,float))):
                                                s_val_1 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("FullRateDeprAmt") + payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate30"]["DepreciationDetail"].get("HalfRateDeprAmt")
                                                if round(m_val_1 / s_val_1) > 40:
                                                    copy_error = copy.deepcopy(error_dict)
                                                    copy_error["field_value"] = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY")
                                                    copy_error["field_name"] = "ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY"
                                                    copy_error["name_range"] = "ITR6PAG1_Opt_115BA_BAA_BAB"
                                                    error_list.append(copy_error)

            if (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY", 0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") != "N") or (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY",0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") != "NA - None of above"):
                if "ScheduleDPM" in payload["ITR"]["ITR6"] and payload["ITR"]["ITR6"] and "PlantMachinery" in payload["ITR"]["ITR6"]["ScheduleDPM"]:
                        if "Rate40" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]:
                            if "DepreciationDetail" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]:
                                if "TotalDepreciation" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"] and \
                                    isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("TotalDepreciation") ,(int,float)):
                                        m_val_2 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("TotalDepreciation")
                                        if (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("FullRateDeprAmt") and\
                                            isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("FullRateDeprAmt"), (int,float))) or (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("HalfRateDeprAmt") and\
                                            isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("HalfRateDeprAmt"), (int,float))):
                                                s_val_2 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("FullRateDeprAmt") + payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate40"]["DepreciationDetail"].get("HalfRateDeprAmt")
                                                if round(m_val_2 / s_val_2) > 40:
                                                    copy_error = copy.deepcopy(error_dict)
                                                    copy_error["field_value"] = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY")
                                                    copy_error["field_name"] = "ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY"
                                                    copy_error["name_range"] = "ITR6PAG1_Opt_115BA_BAA_BAB"
                                                    error_list.append(copy_error)

            if (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY", 0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY") != "N") or (payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") and \
                isinstance(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY",0), str) and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") != "NA - None of above"):
                    if "Rate45" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]:
                            if "DepreciationDetail" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]:
                                if "TotalDepreciation" in payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"] and \
                                    isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("TotalDepreciation") ,(int,float)):
                                        m_val_3 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("TotalDepreciation")
                                        if (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("FullRateDeprAmt") and\
                                            isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("FullRateDeprAmt"), (int,float))) or (payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("HalfRateDeprAmt") and\
                                            isinstance(payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("HalfRateDeprAmt"), (int,float))):
                                                s_val_3 = payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("FullRateDeprAmt") + payload["ITR"]["ITR6"]["ScheduleDPM"]["PlantMachinery"]["Rate45"]["DepreciationDetail"].get("FullRateDeprAmt")
                                                if round(m_val_3 / s_val_3) > 40:
                                                    copy_error = copy.deepcopy(error_dict)
                                                    copy_error["field_value"] = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115CurrAY")
                                                    copy_error["field_name"] = "ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY"
                                                    copy_error["name_range"] = "ITR6PAG1_Opt_115BA_BAA_BAB"
                                                    error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_211(payload, error_list):
        '''
        Summery Line

        Value of ITR6OI_Deem_33AB should be equal to ITR6PGBP_Deem_Inc_33AB
        ITR.ITR6.PARTA_OI.DeemedProfUs33AB == ITR.ITR6.CorpScheduleBP.BusinessIncOthThanSpec.DeemIncUs33AB

        ITR6OI_Deem_33ABA should be equal to ITR6PGBP_Deem_Inc_33ABA
        ITR.ITR6.PARTA_OI.DeemedProfUs33ABA == ITR.ITR6.CorpScheduleBP.BusinessIncOthThanSpec.DeemIncUs33ABA

        ITR6OI_Deem_33AC should be equal to ITR6PGBP_Deem_Inc_33AC
        ITR.ITR6.PARTA_OI.DeemedProfUs33AC == ITR.ITR6.CorpScheduleBP.BusinessIncOthThanSpec.DeemIncUs33AC

        Values at field 33AB, 33ABA and 33AC at Schedule OI at SI. No. 13 should match with respective values in Schedule BP at SI. No. 21
        '''
        error_dict = {
            "remark": "Values at field 33AB, 33ABA and 33AC at Schedule OI at SI. No. 13 should match with respective values in Schedule BP at SI. No. 21",
            "field_name": "",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "211",
            "name_range": ""
        }
        try:
            deemed_prof_fields = [
                ("DeemedProfUs33AB", "ITR6OI_Deem_33AB"),
                ("DeemedProfUs33ABA", "ITR6OI_Deem_33ABA"),
                ("DeemedProfUs33AC", "ITR6OI_Deem_33AC"),
            ]

            for field, name_range in deemed_prof_fields:
                if (
                    payload["ITR"]["ITR6"]["PARTA_OI"].get(field)
                    and payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get(f"DeemInc{field}")
                ):
                    val_1 = payload["ITR"]["ITR6"]["PARTA_OI"].get(field)
                    val_2 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get(f"DeemInc{field}")
                    if val_1 != val_2:
                        copy_error = copy.deepcopy(error_dict)
                        copy_error["field_name"] = f"ITR.ITR6.PARTA_OI.{field}"
                        copy_error["name_range"] = name_range
                        error_list.append(copy_error)

        except Exception:
            pass
    
    @staticmethod
    def rule_531(payload,error_list):
        '''
        Summery Line
        Value of ITR6MAT_IndAS_Y_N is "N", then ITR6MAT_Addn_BP_Tot and ITR6MAT_Dedn_BP_Tot should be zero
        '''
        try:
            if payload["ITR"]["ITR6"]["ScheduleMAT"]["FinancialStamentFlag"] == "N" :
                if payload["ITR"]["ITR6"]["ScheduleMAT"]["AdditionsProfUs115JB"]["TotalAdditions"] != 0 and \
                payload["ITR"]["ITR6"]["ScheduleMAT"]["DeductionsProfUs115JB"]["TotalAdditions"] != 0:
                    error_dict = {
                        "remark": "Details in schedule MAT 8(A) and 8(B) should not be filled. Since 'N' is selected at Whether the financial statements of the company are drawn up in compliance to the Indian Accounting Standards specified in Annexure to the companies (Indian Accounting Standards) Rules, 2015.",
                        "field_name": "ITR.ITR6.ScheduleMAT.FinancialStamentFlag",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["ScheduleMAT"]["FinancialStamentFlag"],
                        "error_code": "531",
                        "name_range": "ITR6MAT_IndAS_Y_N"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_702(payload,error_list):
        '''
        Summery Line
        Value of ITR6ChVIA_Dedn_80PA is greater than zero, then ITR6PAG1_If_Prod_Co should be "Y"
        '''
        try:
            
            if payload["ITR"]["ITR6"]["ScheduleVIA"]["UsrDeductUndChapVIA"]["Section80PA"] > 0 :
                if payload["ITR"]["ITR6"]['PartA_GEN1']["FillingStatus"]["Sec581AFlag"] != "Y" :
                    error_dict = {
                        "remark": 'Please select "Yes" in the field  "Whether   the   company  is   a  producer company as defined in Sec.581A of Companies Act, 1956?" in PartA-General to claim Deduction u/s 80PA',
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["ScheduleVIA"]["UsrDeductUndChapVIA"]["Section80PA"] ,
                        "field_name": "ITR.ITR6.ScheduleVIA.UsrDeductUndChapVIA.Section80PA",
                        "error_code": "702",
                        "name_range": "ITR6ChVIA_Dedn_80PA"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_358(payload,error_list):
        '''
        Summery Line
        ITR.ITR6.ScheduleCG.LongTermCapGain.SaleofAssetNA.DeductSec48.TotalDedn
        ITR.ITR6.ScheduleCG.LongTermCapGain.SaleofAssetNA.FullConsideration
        Value of ITR6CG_LTCG_Oth_Dedn_Tot is greater than zero, then ITR6CG_LTCG_Oth_Tot should be greater than zero
        '''
        try:
            val_1 = 0
            val_2 = 0
            if payload['ITR']["ITR6"]["ScheduleCG"]["LongTermCapGain"]["SaleofAssetNA"]["DeductSec48"]["TotalDedn"]:
                val_1 = payload['ITR']["ITR6"]["ScheduleCG"]["LongTermCapGain"]["SaleofAssetNA"]["DeductSec48"]["TotalDedn"]
            if payload['ITR']["ITR6"]["ScheduleCG"]["LongTermCapGain"]["SaleofAssetNA"]["FullConsideration"]:
                val_2 = payload['ITR']["ITR6"]["ScheduleCG"]["LongTermCapGain"]["SaleofAssetNA"]["FullConsideration"]
            if val_1 > 0 :
                if val_2 < 0:
                    error_dict = {
                        "remark": "Since Full value consideraion (Sl.No.B9aiii)  is zero then Expense u/s 48 (Sl.No.B9b(iv)  cannot be claimed",
                        "validation_status": "Error",
                        "field_value": val_1,
                        "field_name": f"",
                        "error_code": "358",
                        "name_range": "ITR6CG_LTCG_Oth_Dedn_Tot"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_703(payload,error_list):
        '''
        Summery Line
        Value of ITR6PAG1_Domestic is "N", then ITR6ChVIA_Dedn_80GGB should be zero
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["DomesticCompFlg"] =="N" :
                if payload["ITR"]["ITR6"]['ScheduleVIA']["UsrDeductUndChapVIA"]["Section80GGB"] != 0:
                    error_dict = {
                        "remark": "Deduction u/s 80GGB cannot be claimed by foreign company",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["DomesticCompFlg"],
                        "field_name": "ITR.ITR6.PartA_GEN1.OrgFirmInfo.DomesticCompFlg",
                        "error_code": "703",
                        "name_range": "ITR6PAG1_Domestic"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_453(payload,error_list):
        '''
        Summery Line
        In ITR6UD_Table, value of Amount of depreciation set-off against the current year income (4) cannot be greater than column 3 - 3a
        # "AmtBFUD": 5000 - # "AmtAdjOptTaxUs115BAA": 10 > # "AmtDeprSOCY": 500,
        # ITR.ITR6.ITRScheduleUD.ScheduleUD[0]
        '''
        error_dict = {
            "remark": "In ITR6UD_Table, value of Amount of depreciation set-off against the current year income (4) cannot be greater than column 3 - 3a",
            "validation_status": "Error",
            "field_value": "",
            "field_name": "",
            "error_code": "453",
            "name_range": "ITR6UD_Table"
        }
        try:
            if "ITRScheduleUD" in payload["ITR"]["ITR6"] and payload["ITR"]["ITR6"].get("ITRScheduleUD"):
                if "ScheduleUD" in payload["ITR"]["ITR6"].get("ITRScheduleUD"):
                    val = payload["ITR"]["ITR6"]["ITRScheduleUD"]["ScheduleUD"]
                    for i,io in enumerate(val):
                        if "AmtBFUD" in io and "AmtAdjOptTaxUs115BAA" in io and "AmtDeprSOCY" in io:
                            if io["AmtBFUD"]- io["AmtAdjOptTaxUs115BAA"] > io["AmtDeprSOCY"]:
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["field_value"] = io["AmtDeprSOCY"]
                                copy_error["field_name"] = f"ITR.ITR6.ITRScheduleUD.ScheduleUD[{i+1}].AmtDeprSOCY"
                                error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_365(payload ,error_list,workbook):
        '''
        Summery Line
            The value of ITR6OS_Dep cannot exceed value of ITR6OS_Rent
        '''
        try:
            itr6os_dep = BusinessValidation.get_name_range_data(workbook,"ITR6OS_Dep",is_int=True)
            itr6os_rent = BusinessValidation.get_name_range_data(workbook,"ITR6OS_Rent",is_int=True)
            if itr6os_dep > itr6os_rent:
                error_dict = {
                    "remark": "In Schedule OS, deduction at Sl. No. 3b 'Depreciation' will not be"\
                        "allowed/ restricted to the extent of amount at Sl. No.1c 'Rental"\
                        "income from machinery, plants, building, etc'",
                    "validation_status": "Error",
                    "field_value": itr6os_dep,
                    "field_name": f"",
                    "error_code": "365",
                    "name_range": "ITR6OS_Dep"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_353(payload, error_list):
        '''
        Summery Line
        Value of ITR6PGBP_Oth_Addn_28_44DA should be greater than ITR6OI_Amt_Not_Cr_Tot
        In Schedule BP, Sl No 23 should be minimum of sum of amounts entered at Sl No 5a to 5d of Part A OI
        '''
        try:
            if payload["ITR"]["ITR6"].get("Schedule112A") and payload["ITR"]["ITR6"]["Schedule112A"].get("Schedule112ADtls"):
                m_val = payload["ITR"]["ITR6"]["Schedule112A"].get("Schedule112ADtls")
                for i in m_val:
                    if "ShareOnOrBefore" in i:
                        if i["ShareOnOrBefore"] == "AE - After 31st January 2018":
                            if "NumSharesUnits" in i and "SalePricePerShareUnit" in i and "TotFairMktValueCapAst" in i and "ExpExclCnctTransfer" in i:
                                if i["NumSharesUnits"] != 0 and i["SalePricePerShareUnit"] != 0 and i["TotFairMktValueCapAst"] != 0 and i["ExpExclCnctTransfer"] != 0:
                                    error_dict = {
                                        "remark": "In Schedule 112A, value of Columns 4, 5, 10 & 11 cannot be greater than zero in case drop down is selected as “After 31st January 2018”",
                                        "validation_status": "Error",
                                        "field_name" : "ITR.ITR6.Schedule112A.Schedule112ADtls[0]",
                                        "field_value": i["ShareOnOrBefore"],
                                        "error_code": "353",
                                        "name_range": "ITR6112A_Table"
                                    }
                                    error_list.append(error_dict)
        except Exception:
            pass

    
    @staticmethod
    def rule_421(payload, error_list,workbook):
        '''
        Summery Line
            The value of ITR6OS_Dep cannot exceed value of ITR6OS_Rent
        '''
        try:
            itr6bfla_tot_col_4 = BusinessValidation.get_name_range_data(workbook,"ITR6BFLA_Tot_Col_4",is_int=True)
            itr6ud_tot_setoff_2 = BusinessValidation.get_name_range_data(workbook,"ITR6UD_Tot_Setoff_2",is_int=True)
            if itr6bfla_tot_col_4 != itr6ud_tot_setoff_2:
                error_dict = {
                    "remark": "In Schedule BFLA, the total value in Column no 4xvi Brought forward allowance under section 35(4)" \
                    " set off should be equal to total of Column 7 of Schedule UD",
                    "validation_status": "Error",
                    "field_value": itr6bfla_tot_col_4,
                    "field_name": f"",
                    "error_code": "421",
                    "name_range": "ITR6BFLA_Tot_Col_4"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_422(payload, error_list,workbook):
        '''
        Summery Line
            Value of ITR6BFLA_Tot_Col_3 should be equal to ITR6UD_Tot_Setoff
        '''
        try:
            itr6bfla_tot_col_3 = BusinessValidation.get_name_range_data(workbook,"ITR6BFLA_Tot_Col_3",is_int=True)
            itr6ud_tot_setoff = BusinessValidation.get_name_range_data(workbook,"ITR6UD_Tot_Setoff",is_int=True)
            if itr6bfla_tot_col_3 != itr6ud_tot_setoff:
                error_dict = {
                    "remark": "In Schedule BFLA, the total value in Column no 3xvi Brought forward depreciation set off Should be equal to total of Column 4 of Schedule UD",
                    "validation_status": "Error",
                    "field_value": itr6bfla_tot_col_3,
                    "field_name": f"",
                    "error_code": "422",
                    "name_range": "ITR6BFLA_Tot_Col_3"
                }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_442(payload,error_list,workbook):
        '''
        Summery Line
            Value of ITR6CFL_SpecLoss_CY should match with ITR6PGBP_Loss_Spec_Set_Remain
        '''
        try:
            itr6cfl_specloss_cy = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_SpecLoss_CY",is_int=True)
            itr6pgbp_loss_spec_set_remain = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_Loss_Spec_Set_Remain",is_int=True)
            if itr6cfl_specloss_cy != itr6pgbp_loss_spec_set_remain:
                error_dict = {
                    "remark": "Current year Speculative loss in CFL should be equal to amount mentioned in field “Speculative Loss” of Schedule BP",
                    "validation_status": "Error",
                    "field_value": itr6cfl_specloss_cy,
                    "field_name": f"",
                    "error_code": "442",
                    "name_range": "ITR6CFL_SpecLoss_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_443(payload,error_list,workbook):
        '''
        Summery Line
            Value of ITR6CFL_SpecBusns_CY should match with ITR6PGBP_Loss_SpeBI_Remain
        '''
        try:
            itr6cfl_specbusns_cy = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_SpecBusns_CY",is_int=True)
            itr6pgbp_loss_spebi_remain = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_Loss_SpeBI_Remain",is_int=True)
            if itr6cfl_specbusns_cy != itr6pgbp_loss_spebi_remain:
                error_dict = {
                    "remark": "Current year loss from Specified Business in Schedule CFL should be equal to amount mentioned in field Income from specified business of Schedule BP",
                    "validation_status": "Error",
                    "field_value": itr6cfl_specbusns_cy,
                    "field_name": f"",
                    "error_code": "443",
                    "name_range": "ITR6CFL_SpecBusns_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_444(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6CFL_STCG_CY should match with Sum(ITR6CG_STCG_Loss_Remain_15,ITR6CG_STCG_Loss_Remain_30,ITR6CG_STCG_Loss_Remain_AR,ITR6CG_STCG_Loss_Remain_DTAA)
        '''
        try:
            itr6cg_stcg_loss_remain_15 = 0
            itr6cg_stcg_loss_remain_30 = 0
            itr6cg_stcg_loss_remain_ar = 0
            itr6cg_stcg_loss_remain_dtaa = 0
            itr6cfl_stcg_cy = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_STCG_CY",is_int=True)
            itr6cg_stcg_loss_remain_15 = BusinessValidation.get_name_range_data(workbook,"ITR6CG_STCG_Loss_Remain_15",is_int=True)
            itr6cg_stcg_loss_remain_30 = BusinessValidation.get_name_range_data(workbook,"ITR6CG_STCG_Loss_Remain_30",is_int=True)
            itr6cg_stcg_loss_remain_ar = BusinessValidation.get_name_range_data(workbook,"ITR6CG_STCG_Loss_Remain_AR",is_int=True)
            itr6cg_stcg_loss_remain_dtaa = BusinessValidation.get_name_range_data(workbook,"ITR6CG_STCG_Loss_Remain_DTAA",is_int=True)

            sum_val = (itr6cg_stcg_loss_remain_15 +itr6cg_stcg_loss_remain_30 + itr6cg_stcg_loss_remain_ar +itr6cg_stcg_loss_remain_dtaa)
            if itr6cfl_stcg_cy != sum_val:
                error_dict = {
                    "remark": "Current year STCG loss in Schedule CFL should be equal to Table E (2x+3x+4x+5x) of Schedule CG",
                    "validation_status": "Error",
                    "field_value": itr6cfl_stcg_cy,
                    "field_name": f"",
                    "error_code": "444",
                    "name_range": "ITR6CFL_STCG_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_445(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6CFL_LTCG_CY should match with Sum(ITR6CG_LTCG_Loss_Set_off_10,ITR6CG_LTCG_Loss_Set_off_20,ITR6CG_LTCG_Loss_Set_off_DTAA)
        '''
        try:
            itr6cg_ltcg_loss_set_off_10 = 0
            itr6cg_ltcg_loss_set_off_20 = 0
            itr6cg_ltcg_loss_set_off_dtaa = 0
            itr6cfl_ltcg_cy = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_LTCG_CY",is_int=True)
            itr6cg_ltcg_loss_set_off_10 = BusinessValidation.get_name_range_data(workbook,"ITR6CG_LTCG_Loss_Set_off_10",is_int=True)
            itr6cg_ltcg_loss_set_off_20 = BusinessValidation.get_name_range_data(workbook,"ITR6CG_LTCG_Loss_Set_off_20",is_int=True)
            itr6cg_ltcg_loss_set_off_dtaa = BusinessValidation.get_name_range_data(workbook,"ITR6CG_LTCG_Loss_Set_off_DTAA",is_int=True)

            sum_val = (itr6cg_ltcg_loss_set_off_10 +itr6cg_ltcg_loss_set_off_20 + itr6cg_ltcg_loss_set_off_dtaa)
            if itr6cfl_ltcg_cy != sum_val:
                error_dict = {
                    "remark": "Current year LTCG loss in Schedule CFL should be equal to Table E (6x+7x+8x) of Schedule CG",
                    "validation_status": "Error",
                    "field_value": itr6cfl_ltcg_cy,
                    "field_name": f"",
                    "error_code": "445",
                    "name_range": "ITR6CFL_LTCG_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_446(payload,error_list,workbook):
        '''
        Summery Line
            Value of ITR6CFL_HPL_CY should match with ITR6HP_Rest_2_Lac
        '''
        try:
            itr6cfl_hpl_cy = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_HPL_CY",is_int=True)
            itr6hp_rest_2_lac = BusinessValidation.get_name_range_data(workbook,"ITR6HP_Rest_2_Lac",is_int=True)
            if itr6cfl_hpl_cy != itr6hp_rest_2_lac:
                error_dict = {
                    "remark": "Current year HP loss in Schedule CFL should be equal to permissible loss under the head IFHP",
                    "validation_status": "Error",
                    "field_value": itr6cfl_hpl_cy,
                    "field_name": f"",
                    "error_code": "446",
                    "name_range": "ITR6CFL_HPL_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_447(payload,error_list,workbook):
        '''
        Summery Line
            Value of ITR6CFL_RacHor_CY should match with ITR6OS_RH_Tot
        '''
        try:
            itr6cfl_rachor_cy = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_RacHor_CY",is_int=True)
            itr6os_rh_tot = BusinessValidation.get_name_range_data(workbook,"ITR6OS_RH_Tot",is_int=True)
            if itr6cfl_rachor_cy != itr6os_rh_tot:
                error_dict = {
                    "remark": "Current year loss from owning & maintaining race horses in Schedule CFL should be equal to Sl No 8e of Schedule OS",
                    "validation_status": "Error",
                    "field_value": itr6cfl_rachor_cy,
                    "field_name": f"",
                    "error_code": "447",
                    "name_range": "ITR6CFL_RacHor_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_448(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6CFL_InsBusns_CY should match with ITR6PGBP_Loss_Ins_Remain
        '''
        try:
            itr6cfl_insbusns_cy = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_InsBusns_CY",is_int=True)
            itr6pgbp_loss_ins_remain = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_Loss_Ins_Remain",is_int=True)
            if itr6cfl_insbusns_cy != itr6pgbp_loss_ins_remain:
                error_dict = {
                    "remark": "Current Year Loss from life insurance business u/s 115B in CFL should be equal to Sl No E(iv) of Schedule BP",
                    "validation_status": "Error",
                    "field_value": itr6cfl_insbusns_cy,
                    "field_name": f"",
                    "error_code": "448",
                    "name_range": "ITR6CFL_InsBusns_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_449(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6CFL_BFBL_CY should match with ITR6CYLA_Loss_Rem_Col_3
        updated condition as discussed with chandni 11/10
        '''
        try:
            # ITR6CFL_BFBL_CY_CF 
            # ITR6UD_CY_Bal
            # val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_BFBL_CY",is_int=True)
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_BFBL_CY_CF",is_int=True)
            # val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6UD_CY_Bal",is_int=True)
            val_3 = BusinessValidation.get_name_range_data(workbook,"ITR6CYLA_Loss_Rem_Col_3",is_int=True)
            # sum_val = val_1 + val_2
            # if sum_val != val_3:
            if val_1 != val_3:
                error_dict = {
                    "remark": "Current year Loss from Business & Profession (other than loss from Insurance business u/s 115B, loss from speculative business and specified business) in CFL should be equal to 3xviii of Schedule CYLA",
                    "validation_status": "Error",
                    "field_value": val_1,
                    "field_name": f"",
                    "error_code": "449",
                    "name_range": "ITR6CFL_BFBL_CY"
                }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_452(payload,error_list,workbook):
        '''
        Summery Line
            If ITR6PAG1_Opt_115BA_BAA_BAB or ITR6PAG1_Opt_115BA_BAA_BAB_Sec is not '115BAA - Section 115BAA' then ITR6UD_Tot_115BAA should be zero
        '''
        try:
            itr6pag1_opt_115ba_baa_bab = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_Opt_115BA_BAA_BAB")
            itr6pag1_opt_115ba_baa_bab_sec = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_Opt_115BA_BAA_BAB_Sec")
            itr6ud_tot_115baa = BusinessValidation.get_name_range_data(workbook,"ITR6UD_Tot_115BAA")
            
            if (itr6pag1_opt_115ba_baa_bab == "115BAA - Section 115BAA" or itr6pag1_opt_115ba_baa_bab_sec == "115BAA - Section 115BAA"):
                if itr6ud_tot_115baa != 0 :
                    error_dict = {
                        "remark": "In schedule UD, amount at Sl. No. 3a can be entered only if, assessee is opting for taxation u/s 115BAA",
                        "validation_status": "Error",
                        "field_value": itr6ud_tot_115baa,
                        "field_name": f"",
                        "error_code": "452",
                        "name_range": "ITR6UD_Tot_115BAA"
                    }
                    error_list.append(error_dict)
            if (itr6pag1_opt_115ba_baa_bab == "115BA - Section 115BA" or itr6pag1_opt_115ba_baa_bab_sec == "115BA - Section 115BA"):
                val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PB_Ded_10AA")
                val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IA_SC")
                val_3 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IAB_SC")
                val_4 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IAC_SC")
                val_5 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IBA_SC")
                val_6 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IC_SC")
                val_7 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_ParC_Tot_SC")
                val_8 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80JJA_2_SC")
                if val_1 != 0 and val_2 != 0 and val_3 != 0 and val_4 != 0 and val_5 != 0 and val_6 != 0 and val_7 - val_8 != 0 : 
                    error_dict = {
                        "remark": "If opting for lower taxation under Section 115BA, "\
                            "deductions under Schedule 10AA or Schedule 80 or Part C deductions under Chapter VI-A (other than 80JJAA) cannot be claimed",
                        "validation_status": "Error",
                        "field_value": itr6pag1_opt_115ba_baa_bab,
                        "field_name": f"",
                        "error_code": "623",
                        "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB"
                    }
                    error_list.append(error_dict)

            if (itr6pag1_opt_115ba_baa_bab == "115BAB - Section 115BAB" or itr6pag1_opt_115ba_baa_bab_sec == "115BAB - Section 115BAB"):
                val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PB_Ded_10AA")
                val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IA_SC")
                val_3 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IAB_SC")
                val_4 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IAC_SC")
                val_5 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IBA_SC")
                val_6 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IC_SC")
                val_7 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_ParC_Tot_SC")
                val_8 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80JJA_2_SC")
                val_9 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80M_SC")
                if val_1 != 0 and val_2 != 0 and val_3 != 0 and val_4 != 0 and val_5 != 0 and val_6 != 0 and val_7 - val_8 + val_9 != 0 : 
                    error_dict = {
                        "remark": "If opting for lower taxation under Section 115BAB, "
                            "deductions under Schedule 10AA or Schedule 80 or Part C deductions under chapter VI-A (other than 80JJAA or 80M) cannot be claimed",
                        "validation_status": "Error",
                        "field_value": itr6pag1_opt_115ba_baa_bab,
                        "field_name": f"",
                        "error_code": "624",
                        "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB"
                    }
                    error_list.append(error_dict)

            if (itr6pag1_opt_115ba_baa_bab == "115BAA - Section 115BAA" or itr6pag1_opt_115ba_baa_bab_sec == "115BAA - Section 115BAA"):
                val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PB_Ded_10AA")
                val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IA_SC")
                val_3 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IAB_SC")
                val_4 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IAC_SC")
                val_5 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IBA_SC")
                val_6 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IC_SC")
                val_7 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_ParC_Tot_SC")
                val_8 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80JJA_2_SC")
                val_9 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80M_SC")
                val_10 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80LA_1A_SC")
                if val_1 != 0 and val_2 != 0 and val_3 != 0 and val_4 != 0 and val_5 != 0 and val_6 != 0 and val_7 - (val_8 + val_9 + val_10) != 0 : 
                    error_dict = {
                        "remark": "If opting for lower taxation under Section 115BA, "\
                            "deductions under Schedule 10AA or Schedule 80 or Part C deductions under Chapter VI-A (other than 80JJAA) cannot be claimed",
                        "validation_status": "Error",
                        "field_value": itr6pag1_opt_115ba_baa_bab,
                        "field_name": f"",
                        "error_code": "625",
                        "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_626(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6ChVIA_Dedn_80IA cannot be more than vale of ITR6_80_IA4_Tot 
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IA",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6_80_IA4_Tot",is_int=True)
            if val_1 > val_2 :
                error_dict = {
                    "remark": "Value claimed in 80-IA field in Schedule VI-A at Sl No 2e cannot be higher than the value in Schedule 80-IA at Sl No 2f",
                    "validation_status": "Error",
                    "field_value": val_2,
                    "field_name": f"",
                    "error_code": "626",
                    "name_range": "ITR6_80_IA4_Tot"
                }
                error_list.append(error_dict)
            if val_1 != val_2:
                error_dict = {
                        "remark": "Assessee cannot claim deduction u/s 80IA in Sl. No. 2e of Schedule VI-A without filling Schedule 80IA",
                        "validation_status": "Error",
                        "field_value": val_2,
                        "field_name": f"",
                        "error_code": "627",
                        "name_range": "ITR6_80_IA4_Tot"
                    }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_629(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6ChVIA_Dedn_80IB cannot be more than vale of ITR6_80_IB_Tot
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IB",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6_80_IB_Tot",is_int=True)
            if val_1 > val_2 :
                error_dict = {
                    "remark": "Value claimed in 80-IB at Sl No 2h of Schedule VI-A cannot be higher than the value in Schedule 80-IB at Sl No K",
                    "validation_status": "Error",
                    "field_value": val_2,
                    "field_name": f"",
                    "error_code": "629",
                    "name_range": "ITR6_80_IB_Tot"
                }
                error_list.append(error_dict)
            if val_1 != val_2:
                error_dict = {
                    "remark": "Value claimed in 80-IB at Sl No 2h of Schedule VI-A cannot be higher than the value in Schedule 80-IB at Sl No K",
                    "validation_status": "Error",
                    "field_value": val_1,
                    "field_name": f"",
                    "error_code": "630",
                    "name_range": "ITR6ChVIA_Dedn_80IB"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_631(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6ChVIA_Dedn_80IC cannot be more than vale of ITR6_80_IC_IE_Tot
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80IC",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6_80_IC_IE_Tot",is_int=True)
            if val_1 > val_2 :
                error_dict = {
                    "remark": "Value claimed in 80-IC or 80IE at Sl No 2j in Schedule VI-A cannot be higher than the value in Schedule 80-IC/ 80IE (Sl No e)",
                    "validation_status": "Error",
                    "field_value": val_2,
                    "field_name": f"",
                    "error_code": "631",
                    "name_range": "ITR6_80_IC_IE_Tot"
                }
                error_list.append(error_dict)
            if val_1 != val_2:
                error_dict = {
                    "remark": "In schedule VI-A, Sl. No. 2j, Deduction u/s 80-IC/IE cannot beclaimed unless schedule 80-IC/IE is filled.",
                    "validation_status": "Error",
                    "field_value": val_1,
                    "field_name": f"",
                    "error_code": "632",
                    "name_range": "ITR6ChVIA_Dedn_80IC"
                }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_643(payload,error_list,workbook):
        '''
        Summery Line
        If ITR6PAG1_Domestic is N, then ITR6ChVIA_Dedn_80M_SC should be zero
        Value of c should be zero if ITR6PAG1_Loc_IFSC is N
        Value of ITR6ChVIA_Dedn_80LA_1A_SC should be zero if ITR6PAG1_Loc_IFSC is N
        ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80LA_1A
        Value of ITR6ChVIA_Dedn_80LA_1_SC should be zero if ITR6PAG1_Loc_IFSC is Y
        ITR.ITR6.PartA_GEN1.FilingStatus.IsIfsc
        '''
        try:
            if payload["ITR"]["ITR6"].get("PartA_GEN1") and payload["ITR"]["ITR6"]["PartA_GEN1"].get("OrgFirmInfo"):
                if "DomesticCompFlg" in payload["ITR"]["ITR6"]["PartA_GEN1"].get("OrgFirmInfo"):
                    val_1 = payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"].get("DomesticCompFlg")
                    # ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80M
                    if val_1 == "N" and payload["ITR"]["ITR6"].get("ScheduleVIA") and payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                        if "Section80M" in payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                            val_2 = payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"].get("Section80M")
                            if val_2 != 0 :
                                error_dict = {
                                    "remark": "Foreign company cannot claim deduction u/s 80M",
                                    "validation_status": "Error",
                                    "field_value": val_2,
                                    "field_name": f"",
                                    "error_code": "643",
                                    "name_range": "ITR6_80_IC_IE_Tot"
                                }
                                error_list.append(error_dict)

            if payload["ITR"]["ITR6"].get("PartA_GEN1") and payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus"):
                if "IsIfsc" in payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus"):
                    if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("IsIfsc") == "N":
                        if payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA") and payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                            if "Section80LA_1A" in payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA"):
                                val = payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA").get("Section80LA_1A")
                                if val != 0:
                                    error_dict = {
                                        "remark": "Deduciton u/s 80LA(1A) can be claimed only if response to the question “Whether assessee is located in an International Financial Services Centre and derives income solely in convertible foreign exchange?” is selected as 'Y'",
                                        "validation_status": "Error",
                                        "field_value": payload["ITR"]["ITR6"]["ScheduleVIA"].get("DeductUndChapVIA").get("Section80LA_1A"),
                                        "field_name": "ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80LA_1A",
                                        "error_code": "643",
                                        "name_range": "ITR6ChVIA_Dedn_80LA_1A_SC"
                                    }
                                    error_list.append(error_dict)
        except Exception:
            pass



    @staticmethod
    def rule_482(payload,error_list,workbook):
        '''
        Summery Line
        If ITR6PAG1_FinStat_Ind_AS is 'Y', then ITR6MAT_Addn_BP_Item_reclass, ITR6MAT_Addn_BP_Deb_non_Cash, ITR6MAT_Addn_BP_trans_115JB and ITR6MAT_Addn_BP_Oth cannot be blank
        '''
        try:
            itr6pag1_finstat_ind_as = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_FinStat_Ind_AS")
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6MAT_Addn_BP_Item_reclass")
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6MAT_Addn_BP_Deb_non_Cash")
            val_3 = BusinessValidation.get_name_range_data(workbook,"ITR6MAT_Addn_BP_trans_115JB")
            val_4 = BusinessValidation.get_name_range_data(workbook,"ITR6MAT_Addn_BP_Oth")
            if itr6pag1_finstat_ind_as == "Y" and val_1!=None and val_2 != None and val_3 != None and val_4 != None:
                error_dict = {
                    "remark": "If financials is prepared as per Ind-AS, then Sl No 8 of Schedule MAT is mandatory",
                    "validation_status": "Error",
                    "field_value": itr6pag1_finstat_ind_as,
                    "field_name": f"",
                    "error_code": "482",
                    "name_range": "ITR6PAG1_FinStat_Ind_AS"
                }
                error_list.append(error_dict)
            itr6pag1_finstat_ind_as = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_FinStat_Ind_AS")
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6MAT_Addn_BP_Tot")
            if itr6pag1_finstat_ind_as == "N" and val_1!=0:
                error_dict = {
                    "remark": "If financials is not prepared as per Ind-AS, then Sl No 8 of Schedule MAT should not be filled",
                    "validation_status": "Error",
                    "field_value": itr6pag1_finstat_ind_as,
                    "field_name": f"",
                    "error_code": "482",
                    "name_range": "ITR6PAG1_FinStat_Ind_AS"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_487(payload, error_list,workbook):
        '''
        Summery Line
        If MAT is present  at ITR6_MAT_Appl, then only run this rule - added as discussed with Chandni
        Value of ITR6MAT_IncTax_Paid should be greater than sum(ITR6PL_ProvCurTax,ITR6PL_ProvDefTax,ITR6PLIndAS_ProvCurTax,ITR6PLIndAS_ProvDefTax)
        '''
        try:
            main_val = BusinessValidation.get_name_range_data(workbook,"ITR6_MAT_Appl")
            if main_val:
                itr6mat_inctax_paid = BusinessValidation.get_name_range_data(workbook,"ITR6MAT_IncTax_Paid",is_int=True)
                val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PL_ProvCurTax",is_int=True)
                val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6PL_ProvDefTax",is_int=True)
                val_3 = BusinessValidation.get_name_range_data(workbook,"ITR6PLIndAS_ProvCurTax",is_int=True)
                val_4 = BusinessValidation.get_name_range_data(workbook,"ITR6PLIndAS_ProvDefTax",is_int=True)
                sum_amt = (val_1 + val_2 +val_3 +val_4)
                if itr6mat_inctax_paid > sum_amt:
                    error_dict = {
                        "remark": "In Schedule MAT, Sl. No. 5a should be minimum of Sl. No. 54 & 55 of Schedule P&L (Ind AS or IGAAP) as the case may be",
                        "validation_status": "Error",
                        "field_value": itr6mat_inctax_paid,
                        "field_name": f"",
                        "error_code": "487",
                        "name_range": "ITR6MAT_IncTax_Paid"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_492(payload,error_list,workbook):
        '''
        Summery Line
            Value of ITR6MATC_MAT should be equal to ITR6PB_MAT_Tot
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6MATC_MAT",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6PB_MAT_Tot",is_int=True)
            if val_1 != val_2:
                error_dict = {
                    "remark": "In Schedule MATC, Sl No 1 (Tax under section 115JB) should be equal to Sl No 1d of PART B-TTI",
                    "validation_status": "Error",
                    "field_value": val_1,
                    "field_name": f"",
                    "error_code": "492",
                    "name_range": "ITR6MATC_MAT"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_493(payload,error_list,workbook):
        '''
        Summery Line
            Value of ITR6MATC_Tax_Norm_Prov should be equal to ITR6PB_Gross_Tax_liab
        '''
        try:
            # val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6MATC_Tax_Norm_Prov",is_int=True)
            # val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6PB_Gross_Tax_liab",is_int=True)
            val_1=0
            val_2=0
            if "ScheduleMATC" in payload['ITR']['ITR6'] and "TaxOthProvCurrAssYr" in payload['ITR']['ITR6']['ScheduleMATC']:
                val_1 = payload['ITR']['ITR6']['ScheduleMATC'].get('TaxOthProvCurrAssYr')
            
            if "PartB_TTI" in payload['ITR']['ITR6'] and "ComputationOfTaxLiability" in payload['ITR']['ITR6']['PartB_TTI']\
                and "TaxPayableOnTI" in payload['ITR']['ITR6']['PartB_TTI']['ComputationOfTaxLiability']\
                    and "GrossTaxLiability" in payload['ITR']['ITR6']['PartB_TTI']['ComputationOfTaxLiability']['TaxPayableOnTI']:
                    val_2 = payload['ITR']['ITR6']['PartB_TTI']['ComputationOfTaxLiability']['TaxPayableOnTI'].get('GrossTaxLiability')

            if val_1 != val_2:
                error_dict = {
                    "remark": "In Schedule MATC, Sl. No. 2 should be equal to Sl No 2f of Part B-TTI",
                    "validation_status": "Error",
                    "field_value": val_1,
                    "field_name": f"",
                    "error_code": "493",
                    "name_range": "ITR6MATC_Tax_Norm_Prov"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_494(payload,error_list,workbook):
        '''
        Summery Line
        If ITR6MATC_Tax_Norm_Prov is greater than ITR6MATC_MAT, then ITR6MATC_Cred_Avbl should be ITR6MATC_Tax_Norm_Prov - ITR6MATC_MAT.  Else, ITR6MATC_Cred_Avbl should be zero
        If ITR6MATC_MAT is greater than ITR6MATC_Tax_Norm_Prov, then ITR6MATC_Cred_Avbl should be ITR6MATC_MAT - ITR6MATC_Tax_Norm_Prov.  Else, ITR6MATC_Cred_Avbl should be zero
        ITR.ITR6.ScheduleMATC.TaxUs115JBCurrAssYr ITR6MATC_MAT
        ITR.ITR6.ScheduleMATC.TaxOthProvCurrAssYr ITR6MATC_Tax_Norm_Prov
        ITR.ITR6.ScheduleMATC.AmtOfTaxWithCred  ITR6MATC_Cred_Avbl
        '''
        try:
            if payload["ITR"]["ITR6"].get("ScheduleMATC") and payload["ITR"]["ITR6"]["ScheduleMATC"].get("TaxUs115JBCurrAssYr") :
                val_1 = payload["ITR"]["ITR6"]["ScheduleMATC"].get("TaxUs115JBCurrAssYr")
            if payload["ITR"]["ITR6"].get("ScheduleMATC") and payload["ITR"]["ITR6"]["ScheduleMATC"].get("TaxOthProvCurrAssYr") :
                val_2 = payload["ITR"]["ITR6"]["ScheduleMATC"].get("TaxOthProvCurrAssYr") 
            if payload["ITR"]["ITR6"].get("ScheduleMATC") and payload["ITR"]["ITR6"]["ScheduleMATC"].get("AmtOfTaxWithCred") :
                val_3 = payload["ITR"]["ITR6"]["ScheduleMATC"].get("AmtOfTaxWithCred")

            if val_2 > val_1:
                match_val = val_2 - val_1
                if val_3 != match_val:
                    error_dict = {
                        "remark": "In Schedule MATC, Sl. No. 3 should be equal to Sl No 2-1. This rule is applicable only if 2 is greater than 1, otherwise Sl No 3 = 0",
                        "validation_status": "Error",
                        "field_value": val_3,
                        "field_name": f"",
                        "error_code": "494",
                        "name_range": "ITR6MATC_Cred_Avbl"
                    }
                    error_list.append(error_dict)
            elif val_3 != 0:
                error_dict = {
                    "remark": "In Schedule MATC, Sl. No. 3 should be equal to Sl No 2-1. This rule is applicable only if 2 is greater than 1, otherwise Sl No 3 = 0",
                    "validation_status": "Error",
                    "field_value": val_3,
                    "field_name": f"",
                    "error_code": "494",
                    "name_range": "ITR6MATC_Cred_Avbl"
                }
                error_list.append(error_dict)
            # if ITR6MATC_MAT < ITR6MATC_Tax_Norm_Prov:
            #     if ITR6MATC_Cred_Avbl != 0:
            #         error_dict = {
            #             "remark": "In Schedule MATC, Sl No 3 should be equal to zero when Sl No 2 is less than or equal to 1",
            #             "validation_status": "Error",
            #             "field_value": ITR6MATC_Cred_Avbl,
            #             "field_name": f"",
            #             "error_code": "495",
            #             "name_range": "ITR6MATC_Cred_Avbl"
            #         }
            #         error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_498(payload,error_list):
        '''
        Summery Line
        ITR.ITR6.PartA_GEN1.FilingStatus.Section115BA = "NA - None of above"
        ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY = "N"
        # ITR6MATC_MAT	ITR.ITR6.ScheduleMATC.TaxUs115JBCurrAssYr
        # ITR6MATC_CY	ITR.ITR6.ScheduleMATC.CurAssYr
        # ITR6MATC_Gross_Tot	ITR.ITR6.ScheduleMATC.TotMatCredGross
        # ITR6MATC_Setoff_Tot	ITR.ITR6.ScheduleMATC.TotMatCredSetOff
        # ITR6MATC_Cred_Tot	ITR.ITR6.ScheduleMATC.TotMatCredBF
        # ITR6MATC_Utls_Tot	ITR.ITR6.ScheduleMATC.TotMatCredUtilCurrYr
        # ITR6MATC_Bal_Tot	ITR.ITR6.ScheduleMATC.TotBalMATCredCF
        # ITR6MATC_Tax_Norm_Prov	ITR.ITR6.ScheduleMATC.TaxOthProvCurrAssYr
        # ITR6MATC_Cred_Avbl	ITR.ITR6.ScheduleMATC.AmtOfTaxWithCred
        # ITR6MATC_Crd_115JAA	ITR.ITR6.ScheduleMATC.AmtTaxCredUs115JAA
        # ITR6MATC_Crd_CarFwd	ITR.ITR6.ScheduleMATC.AmtMATLiabAllAssYrAvailSubseqYr

        # ITR6MATC_Credit_Utilisation_Table
        # ITR.ITR6.ScheduleMATC.UtilMATCredAvl[0]
        '''
        error_dict = {
                        "remark": "In Schedule MATC, Sl. No. 3 should be equal to Sl No 2-1. This rule is applicable only if 2 is greater than 1, otherwise Sl No 3 = 0",
                        "validation_status": "Error",
                        "field_value": f"",
                        "field_name": f"",
                        "error_code": "498",
                        "name_range": f""
                    }
        try:
            if payload["ITR"]["ITR6"].get("PartA_GEN1") and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115BA"]:
                val_1 = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115BA"]
            if payload["ITR"]["ITR6"].get("PartA_GEN1") and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115CurrAY"]:
                val_2 = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115CurrAY"]
            
            if val_1 == "NA - None of above" or val_2 == "N":
                matc_fields = [
                ("TaxUs115JBCurrAssYr", "ITR6MATC_MAT"),
                ("CurAssYr", "ITR6MATC_CY"),
                ("TotMatCredGross", "ITR6MATC_Gross_Tot"),
                ("TotMatCredSetOff", "ITR6MATC_Setoff_Tot"),
                ("TotMatCredBF", "ITR6MATC_Cred_Tot"),
                ("TotMatCredUtilCurrYr", "ITR6MATC_Utls_Tot"),
                ("TotBalMATCredCF", "ITR6MATC_Bal_Tot"),
                ("TaxOthProvCurrAssYr", "ITR6MATC_Tax_Norm_Prov"),
                ("AmtOfTaxWithCred", "ITR6MATC_Cred_Avbl"),
                ("AmtTaxCredUs115JAA", "ITR6MATC_Crd_115JAA"),
                ("AmtMATLiabAllAssYrAvailSubseqYr", "ITR6MATC_Crd_CarFwd"),
            ]

            for field, name_range in matc_fields:
                if (
                    payload["ITR"]["ITR6"]["ScheduleMATC"][field] != 0
                    or payload["ITR"]["ITR6"]["ScheduleMATC"][field] != ""
                    or payload["ITR"]["ITR6"]["ScheduleMATC"][field] is not None
                ):
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_value"] = payload["ITR"]["ITR6"]["ScheduleMATC"][field]
                    copy_error["field_name"] = f"ITR.ITR6.ScheduleMATC.{field}"
                    copy_error["name_range"] = name_range
                    error_list.append(copy_error)

                if payload["ITR"]["ITR6"]["ScheduleMATC"]:
                    if "UtilMATCredAvl" in payload["ITR"]["ITR6"]["ScheduleMATC"]:
                        if len(payload["ITR"]["ITR6"]["ScheduleMATC"]["UtilMATCredAvl"])==0:
                            pass
                        else:
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = payload["ITR"]["ITR6"]["ScheduleMATC"]["UtilMATCredAvl"]
                            copy_error["name_range"] = "ITR.ITR6.ScheduleMATC.UtilMATCredAvl"
                            error_list.append(copy_error)
        except Exception:
            pass
    
    @staticmethod
    def rule_512(payload, error_list, workbook):
        '''
        Summery Line
        ITR6TPSA_Tax_Paid_Table
        In ITR6TPSA_Tax_Paid_Table, the date in column Date of Deposit should be not be greater than today's date (i.e. current date)
        '''
        error_dict = {
                        "remark": "In Schedule MATC, Sl. No. 3 should be equal to Sl No 2-1. This rule is applicable only if 2 is greater than 1, otherwise Sl No 3 = 0",
                        "validation_status": "Error",
                        "field_value": f"",
                        "field_name": f"",
                        "error_code": "512",
                        "name_range": f""
                    }
        try:
            if payload["ITR"]["ITR6"]["PARTA_OI"]["ScheduleTPSAFlg"] == "Y":
                range_arr = BusinessValidation.find_acc_range(list7, workbook,is_req_val=True)
                if payload["ITR"]["ITR6"]["ScheduleTPSA"]:
                    if "DtlsTaxesPaid" in payload["ITR"]["ITR6"]["ScheduleTPSA"] and len(payload["ITR"]["ITR6"]["ScheduleTPSA"]["DtlsTaxesPaid"])==0:
                        copy_error = copy.deepcopy(error_dict)
                        copy_error["name_range"] = "ITR6TPSA_Tax_Paid_Table"
                        error_list.append(copy_error)
                    if range_arr != [] and range_arr != None:
                        for error in range_arr:
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = error["value"]
                            copy_error["name_range"] = error["name"]
                            error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_513(payload, error_list, workbook):
        '''
        Summery Line
        ITR6TPSA_Tax_Paid_Table
        In ITR6TPSA_Tax_Paid_Table, the date in column Date of Deposit should be not be greater than today's date (i.e. current date)
        '''
        try:
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
            find_val = find_table("ITR6TPSA_Tax_Paid_Table",workbook)
            n = 6
            f_val = []
            # using list comprehension
            if find_val != []:
                final = [find_val[i * n:(i + 1) * n] for i in range((len(find_val) + n - 1) // n )]
            for d in final:
                f_val.append(d[3])        
            for i in f_val:
                if i != None:
                    current_date = datetime.datetime.now().date()
                    date_obj = datetime.datetime.strptime(i, "%Y-%m-%d").date()
                    if date_obj > current_date:
                        error_dict = {
                        "remark": "In schedule TPSA, Date at which tax is deposit cannot be after Current date",
                        "field_name": f"",
                        "validation_status": "Error",
                        "field_value": i,
                        "error_code": "513",
                        "name_range": "ITR6TPSA_Tax_Paid_Table"
                        }
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_517(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6HP1_Income_HP_Tot should be greater than sum(ITR6FSI_IFHP_Inc_1,ITR6FSI_IFHP_Inc_2)
        # ITR.ITR6.ScheduleHP.TotalIncomeChargeableUnHP
        '''
        try:
            if payload["ITR"]["ITR6"].get("ScheduleHP") and payload["ITR"]["ITR6"]["ScheduleHP"].get("TotalIncomeChargeableUnHP"):
                itr6hp1_income_hp_tot = payload["ITR"]["ITR6"]["ScheduleHP"].get("TotalIncomeChargeableUnHP")
            else:
                itr6hp1_income_hp_tot = 0
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6FSI_IFHP_Inc_1")
            # if isinstance(val_1, (int,float)):
            #     val_1 = val_1
            # else:
            if not isinstance(val_1, (int,float)):
                val_1 = 0
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6FSI_IFHP_Inc_2")
            # if isinstance(val_2, (int,float)):
            #     val_2 = val_2
            # else:
            if not isinstance(val_2, (int,float)):
                val_2 = 0
            sum_amt = (val_1+val_2)
            if itr6hp1_income_hp_tot < sum_amt:
                error_dict = {
                    "remark": "If tax relief is claimed against House Property, then income from House property should be more" \
                        "than the amount of income shown under House property in Schedule FSI",
                    "validation_status": "Error",
                    "field_value": itr6hp1_income_hp_tot,
                    "field_name": f"",
                    "error_code": "517",
                    "name_range": "ITR6HP1_Income_HP_Tot"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_518(payload,error_list,workbook):
        '''
        Summery Line
        Value of sum(ITR6PL_Tot_Oth_Inc,ITR6TA_OprRevTot,ITR6TAIAS_TotSale,ITR6PLIndAS_Tot_Oth_Inc) should be greater than sum(ITR6FSI_PGBP_Inc_1,ITR6FSI_PGBP_Inc_2)
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PL_Tot_Oth_Inc",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6TAIAS_TotSale",is_int=True)
            val_3 = BusinessValidation.get_name_range_data(workbook,"ITR6PLIndAS_Tot_Oth_Inc",is_int=True)
            val_4 = BusinessValidation.get_name_range_data(workbook,"ITR6TA_OprRevTot",is_int=True)
            match_val_4 = BusinessValidation.get_name_range_data(workbook,"ITR6FSI_PGBP_Inc_1",is_int=True)
            match_val_5 = BusinessValidation.get_name_range_data(workbook,"ITR6FSI_PGBP_Inc_2",is_int=True)
            sum_amt = (val_1 + val_2 +val_3 +val_4)
            match_amt= (match_val_4 + match_val_5)
            if sum_amt < match_amt:
                error_dict = {
                    "remark": "If tax relief is claimed against PGBP, then income from PGBP should be more than the amount of income shown under PGBP in Schedule FSI",
                    "validation_status": "Error",
                    "field_value": match_amt,
                    "field_name": f"",
                    "error_code": "518",
                    "name_range": "ITR6FSI_PGBP_Inc_1"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    

    @staticmethod
    def rule_520(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6OS_Gr_Inc_NR_4 should be greater than sum(ITR6FSI_OS_Inc_1,ITR6FSI_OS_Inc_2)
        '''
        try:
            if payload["ITR"]["ITR6"].get("ScheduleOS") and payload["ITR"]["ITR6"]["ScheduleOS"].get("IncChargeableFrmOthSrc"):
                itr6os_gr_inc_nr_4 = payload["ITR"]["ITR6"]["ScheduleOS"].get("IncChargeableFrmOthSrc")
            else:
                itr6os_gr_inc_nr_4 = 0
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6FSI_OS_Inc_1")
            # if isinstance(val_1, (int,float)):
            #     val_1 = val_1
            # else:
            if not isinstance(val_1, (int,float)):
                val_1 = 0
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6FSI_OS_Inc_2")
            # if isinstance(val_2, (int,float)):
            #     val_2 = val_2
            # else:
            if not isinstance(val_2, (int,float)):
                val_2 = 0
            sum_amt = (val_1+val_2)
            if itr6os_gr_inc_nr_4 < sum_amt:
                error_dict = {
                    "remark": "If tax relief is claimed against IFOS, then income from IFOS should be more than the amount of income shown under IFOS in Schedule FSI",
                    "validation_status": "Error",
                    "field_value": itr6os_gr_inc_nr_4,
                    "field_name": f"",
                    "error_code": "520",
                    "name_range": "ITR6OS_Gr_Inc_NR_4"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_551(payload, error_list):
        '''
        Summery Line
        Value of ITR6PGBP_Oth_Addn_28_44DA should be greater than ITR6OI_Amt_Not_Cr_Tot
        In Schedule BP, Sl No 23 should be minimum of sum of amounts entered at Sl No 5a to 5d of Part A OI
        ITR.ITR6.Schedule10AA.DeductSEZ.DedUs10Detail.TotalDedUs10Sub
        '''
        error_dict = {
            "remark": "If deduction u/s 10AA is claimed, Schedule 10AA should be filled and the amount should match with amount reported in the said schedule",
            "validation_status": "Error",
            "field_value": "",
            "field_name": f"",
            "error_code": "551",
            "name_range": "ITR6PB_Ded_10AA"
        }
        try:
            if payload["ITR"]["ITR6"].get("PartB-TI") and payload["ITR"]["ITR6"]["PartB-TI"].get("DeductionsUnder10Aor10AA"):
                val = payload["ITR"]["ITR6"]["PartB-TI"].get("DeductionsUnder10Aor10AA")
                if payload["ITR"]["ITR6"].get("Schedule10AA") and payload["ITR"]["ITR6"]["Schedule10AA"].get("DeductSEZ") and payload["ITR"]["ITR6"]["Schedule10AA"]["DeductSEZ"].get("DedUs10Detail"):
                        c_val = payload["ITR"]["ITR6"]["Schedule10AA"]["DeductSEZ"].get("DedUs10Detail")
                        if "TotalDedUs10Sub" in c_val:
                            if val > 0 and c_val["TotalDedUs10Sub"] == val :
                                    if "Undertaking" in c_val and "DedFromUndertakingWithAy" in c_val["Undertaking"]:
                                        if len(c_val["Undertaking"]["DedFromUndertakingWithAy"]) == 0 :
                                            copy_error = copy.deepcopy(error_dict)
                                            copy_error["field_value"] = val
                                            error_list.append(copy_error)
                                    elif "Undertaking" in c_val["Undertaking"] and "DedFromUndertakingWithAy" not in c_val["Undertaking"]:
                                        copy_error = copy.deepcopy(error_dict)
                                        copy_error["field_value"] = val
                                        error_list.append(copy_error)
                            elif val > 0 and c_val["TotalDedUs10Sub"] != val:
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["field_value"] = val
                                error_list.append(copy_error)
                elif ("Schedule10AA" not in payload["ITR"]["ITR6"] or "DeductSEZ" not in payload["ITR"]["ITR6"]["Schedule10AA"] or "DedUs10Detail" not in payload["ITR"]["ITR6"]["Schedule10AA"]["DeductSEZ"]):
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_value"] = val
                    error_list.append(copy_error)

        except Exception:
            pass

    @staticmethod
    def rule_604(payload,error_list,workbook):
        '''
        Summery Line
        If ITR6ChVIA_Dedn_80G is greater than zero, the value of ITR680G_100_wol_Amt_Tot or ITR680G_50_wol_Amt_Tot or
         ITR680G_100_wl_Amt_Tot or ITR680G_50_wl_Amt_Tot should be greater than zero
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80G",is_int=True)
            if val_1 > 0 :
                val_2 = BusinessValidation.get_name_range_data(workbook,"ITR680G_100_wol_Amt_Tot",is_int=True)
                val_3 = BusinessValidation.get_name_range_data(workbook,"ITR680G_50_wol_Amt_Tot",is_int=True)
                val_4 = BusinessValidation.get_name_range_data(workbook,"ITR680G_100_wl_Amt_Tot",is_int=True)
                val_5 = BusinessValidation.get_name_range_data(workbook,"ITR680G_50_wl_Amt_Tot",is_int=True)
                if (val_2 < 0 or val_3 < 0 or val_4 < 0 or val_5 < 0 ):
                    error_dict = {
                        "remark": "If deduction under section 80G claimed in under Chapter VI-A then its mandatory to fill details in Schedule 80G",
                        "validation_status": "Error",
                        "field_value": val_1,
                        "field_name": f"",
                        "error_code": "604",
                        "name_range": "ITR6ChVIA_Dedn_80G"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_606(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR680G_80G_Amout_Tot cannot be greater than ITR680G_80G_Deduction
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR680G_80G_Amout_Tot",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR680G_80G_Deduction",is_int=True)
            if val_2 > val_1 :
                    error_dict = {
                        "remark": "In Schedule 80G : the value of the field “Eligible amount of"\
                            "Donations” cannot be more than value at field “Total Donations”",
                        "validation_status": "Error",
                        "field_value": val_2,
                        "field_name": f"",
                        "error_code": "606",
                        "name_range": "ITR680G_80G_Deduction"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass
    @staticmethod
    def rule_605(payload, error_list):
        '''
        Summery Line
        The value in PAN column of the tables ITR680G_100_WOQL_Table, ITR680G_50_WOQL_Table, ITR680G_100_WQL_Table 
        and ITR680G_50_WQL_Table should not match with ITR6PAG1_PAN or ITR6Ver_PAN
        # ITR680G_100_WOQL_Table # ITR.ITR6.Schedule80G.Don100Percent.DoneeDetail[0]
        # ITR680G_50_WOQL_Table # ITR.ITR6.Schedule80G.Don50PercentNoApprReqd.DoneeDetail[0]
        # ITR680G_100_WQL_Table # ITR.ITR6.Schedule80G.Don100PercentApprReqd.DoneeDetail[0]
        # ITR680G_50_WQL_Table # ITR.ITR6.Schedule80G.Don50PercentApprReqd.DoneeDetail[0]

        # ITR6PAG1_PAN # ITR.ITR6.Verification.Declaration.AssesseeVerPAN
        # ITR6Ver_PAN # ITR.ITR6.PartA_GEN1.FilingStatus.AssesseeRep.RepPAN
        '''
        error_dict = {
            "remark": "In Schedule 80G Donee PAN cannot be same as “Assessee PAN” or “PAN at Verification",
            "validation_status": "Error",
            "field_value": "",
            "field_name": "",
            "error_code": "605",
            "name_range": ""
        }
        try:
            check_pan = []
            # check_pan = ['AGRPY7777K', None]
            if payload["ITR"]["ITR6"].get("Verification") and payload["ITR"]["ITR6"]["Verification"].get("Declaration"):
                if "AssesseeVerPAN" in payload["ITR"]["ITR6"]["Verification"].get("Declaration"):
                    check_pan.append(payload["ITR"]["ITR6"]["Verification"]["Declaration"]["AssesseeVerPAN"])
                else:
                    check_pan.append(None)
            if payload["ITR"]["ITR6"].get("PartA_GEN1") and payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus"):
                if "AssesseeVerPAN" in payload["ITR"]["ITR6"]["PartA_GEN1"].get("FilingStatus") and "RepPAN" in payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["AssesseeRep"].get("RepPAN"):
                    check_pan.append(payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["AssesseeVerPAN"]["RepPAN"])
                else:
                    check_pan.append(None)
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don100Percent"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don100Percent")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don100Percent"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            if dodetail["DoneePAN"] in check_pan:
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["field_value"] = dodetail["DoneePAN"]
                                copy_error["name_range"] = "ITR680G_100_WOQL_Table"
                                copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don100Percent.DoneeDetail[{i+1}].DoneePAN"
                                error_list.append(copy_error)
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentNoApprReqd"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentNoApprReqd")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don50PercentNoApprReqd"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            if dodetail["DoneePAN"] in check_pan:
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["field_value"] = dodetail["DoneePAN"]
                                copy_error["name_range"] = "ITR680G_50_WOQL_Table"
                                copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don50PercentNoApprReqd.DoneeDetail[{i+1}].DoneePAN"
                                error_list.append(copy_error)
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don100PercentApprReqd"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don100PercentApprReqd")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don100PercentApprReqd"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            if dodetail["DoneePAN"] in check_pan:
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["field_value"] = dodetail["DoneePAN"]
                                copy_error["name_range"] = "ITR680G_100_WQL_Table"
                                copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don100PercentApprReqd.DoneeDetail[{i+1}].DoneePAN"
                                error_list.append(copy_error)
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentApprReqd"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentApprReqd")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don50PercentApprReqd"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            if dodetail["DoneePAN"] in check_pan:
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["field_value"] = dodetail["DoneePAN"]
                                copy_error["name_range"] = "ITR680G_50_WQL_Table"
                                copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don50PercentApprReqd.DoneeDetail[{i+1}].DoneePAN"
                                error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_607(payload, error_list):
        '''
        Summery Line
        The value in PAN column of the tables ITR680G_100_WOQL_Table, ITR680G_50_WOQL_Table, ITR680G_100_WQL_Table 
        and ITR680G_50_WQL_Table should not match with ITR6PAG1_PAN or ITR6Ver_PAN
        # ITR680G_100_WOQL_Table # ITR.ITR6.Schedule80G.Don100Percent.DoneeDetail[0]
        # ITR680G_50_WOQL_Table # ITR.ITR6.Schedule80G.Don50PercentNoApprReqd.DoneeDetail[0]
        # ITR680G_100_WQL_Table # ITR.ITR6.Schedule80G.Don100PercentApprReqd.DoneeDetail[0]
        # ITR680G_50_WQL_Table # ITR.ITR6.Schedule80G.Don50PercentApprReqd.DoneeDetail[0]

        # ITR6PAG1_PAN # ITR.ITR6.Verification.Declaration.AssesseeVerPAN
        # ITR6Ver_PAN # ITR.ITR6.PartA_GEN1.FilingStatus.AssesseeRep.RepPAN
        Updated as discussed with chandni
        '''
        error_dict = {
            "remark": "In Schedule 80G the cash donation limit cannot exceed ₹2000",
            "validation_status": "Error",
            "field_value": "",
            "field_name": "",
            "error_code": "607",
            "name_range": ""
        }
        try:
            def validate_donations(payload, error_dict, error_list, section_key, table_name_key):
                if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get(section_key):
                    val = payload["ITR"]["ITR6"]["Schedule80G"].get(section_key)
                    if "DoneeDetail" in val:
                        for i, dodetail in enumerate(val.get("DoneeDetail")):
                            if "DonationAmtCash" in dodetail:
                                if isinstance(dodetail["DonationAmtCash"], (int, float)) and dodetail["DonationAmtCash"] > 0:
                                    if "DonationElgAmt" in dodetail:
                                        if isinstance(dodetail["DonationElgAmt"], (int, float)) and dodetail["DonationElgAmt"] > 2000:
                                            copy_error = copy.deepcopy(error_dict)
                                            copy_error["field_value"] = dodetail.get("DonationAmtCash", dodetail.get("DoneePAN"))
                                            copy_error["name_range"] = table_name_key
                                            copy_error["field_name"] = f"ITR.ITR6.Schedule80G.{section_key}.DoneeDetail[{i+1}].DonationAmtCash"
                                            error_list.append(copy_error)

            # Define sections and table names
            sections = [
                ("Don100Percent", "ITR680G_100_WOQL_Table"),
                ("Don50PercentNoApprReqd", "ITR680G_50_WOQL_Table"),
                ("Don100PercentApprReqd", "ITR680G_100_WQL_Table"),
                ("Don50PercentApprReqd", "ITR680G_50_WQL_Table")
            ]

            # Validate each section
            for section_key, table_name_key in sections:
                validate_donations(payload, error_dict, error_list, section_key, table_name_key)

        except Exception:
            pass


    @staticmethod
    def rule_611(payload, error_list):
        '''
        Summery Line
        Any PAN appearing 1 of the 4 tables should not be appear in the other tables
        # ITR680G_100_WOQL_Table # ITR.ITR6.Schedule80G.Don100Percent.DoneeDetail[0]
        # ITR680G_50_WOQL_Table # ITR.ITR6.Schedule80G.Don50PercentNoApprReqd.DoneeDetail[0]
        # ITR680G_100_WQL_Table # ITR.ITR6.Schedule80G.Don100PercentApprReqd.DoneeDetail[0]
        # ITR680G_50_WQL_Table # ITR.ITR6.Schedule80G.Don50PercentApprReqd.DoneeDetail[0]

        # ITR6PAG1_PAN # ITR.ITR6.Verification.Declaration.AssesseeVerPAN
        # ITR6Ver_PAN # ITR.ITR6.PartA_GEN1.FilingStatus.AssesseeRep.RepPAN
        '''
        error_dict = {
            "remark": "In Schedule 80G, if PAN is already entered in anyone of the set of blocks (i.e 100%, 50%, with Qualifying limit,"\
            " without Qualifying limit) then same PAN cannot be entered in any other block",
            "validation_status": "Error",
            "field_value": "",
            "field_name": "",
            "error_code": "611",
            "name_range": ""
        }
        try:
            a=[]
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don100Percent"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don100Percent")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don100Percent"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = dodetail["DoneePAN"]
                            copy_error["name_range"] = "ITR680G_100_WOQL_Table"
                            copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don100Percent.DoneeDetail[{i+1}].DoneePAN"
                            a.append(copy_error)
                            # a.append({"PAN":dodetail["DoneePAN"],"name_range":"ITR680G_100_WOQL_Table","index":i+1})
                            # a.append(dodetail["DoneePAN"])
            b=[]
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentNoApprReqd"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentNoApprReqd")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don50PercentNoApprReqd"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = dodetail["DoneePAN"]
                            copy_error["name_range"] = "ITR680G_50_WOQL_Table"
                            copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don50PercentNoApprReqd.DoneeDetail[{i+1}].DoneePAN"
                            b.append(copy_error)
                            # b.append({"PAN":dodetail["DoneePAN"],"name_range":"ITR680G_50_WOQL_Table","index":i+1})
                            # b.append(dodetail["DoneePAN"])
            c=[]
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don100PercentApprReqd"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don100PercentApprReqd")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don100PercentApprReqd"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = dodetail["DoneePAN"]
                            copy_error["name_range"] = "ITR680G_100_WQL_Table"
                            copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don100PercentApprReqd.DoneeDetail[{i+1}].DoneePAN"
                            c.append(copy_error)
                            # c.append({"PAN":dodetail["DoneePAN"],"name_range":"ITR680G_100_WQL_Table","index":i+1})
                            # c.append(dodetail["DoneePAN"])
            d=[]
            if payload["ITR"]["ITR6"].get("Schedule80G") and payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentApprReqd"):
                val = payload["ITR"]["ITR6"]["Schedule80G"].get("Don50PercentApprReqd")
                if "DoneeDetail" in val:
                    for i,dodetail in enumerate(payload["ITR"]["ITR6"]["Schedule80G"]["Don50PercentApprReqd"].get("DoneeDetail")):
                        if "DoneePAN" in dodetail:
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = dodetail["DoneePAN"]
                            copy_error["name_range"] = "ITR680G_50_WQL_Table"
                            copy_error["field_name"] = f"ITR.ITR6.Schedule80G.Don50PercentApprReqd.DoneeDetail.[{i+1}].DoneePAN"
                            d.append(copy_error)
                            # d.append({"PAN":dodetail["DoneePAN"],"name_range":"ITR680G_50_WQL_Table","index":i+1})
                            # d.append(dodetail["DoneePAN"])

            def m(source,main1,main2,main3):
                q=[]
                for i,jj in enumerate(source):
                    q+=list(filter(lambda x:x["field_value"]==jj["field_value"],main1))
                    q+=list(filter(lambda x:x["field_value"]==jj["field_value"],main2))
                    q+=list(filter(lambda x:x["field_value"]==jj["field_value"],main3))
                return q

            tab1 = m(a,b,c,d)
            tab2 = m(b,c,d,a)
            tab3 = m(c,d,a,b)
            tab4 = m(d,a,b,c)
            for t1 in tab1:
                error_list.append(t1)
            for t2 in tab2:
                error_list.append(t2)
            for t3 in tab3:
                error_list.append(t3)
            for t4 in tab4:
                error_list.append(t4)
        except Exception:
            pass

    @staticmethod
    def rule_612(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR680G_80G_Deduction should match with ITR6ChVIA_Dedn_80G_SC
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR680G_80G_Deduction",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80G_SC",is_int=True)
            if val_1 != val_2 :
                    error_dict = {
                        "remark": "In Schedule VIA, value at Sl. No. 1a of system calculated value of 80G should match with value at eligible donation at Sl. No. E in Schedule 80G",
                        "validation_status": "Error",
                        "field_value": val_1,
                        "field_name": f"",
                        "error_code": "612",
                        "name_range": "ITR680G_80G_Deduction"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_615(payload, error_list, workbook):
        '''
        Summery Line
        ITR6TPSA_Tax_Paid_Table
        In ITR6TPSA_Tax_Paid_Table, the date in column Date of Deposit should be not be greater than today's date (i.e. current date)
        '''
        try:
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
            find_val = find_table("ITR6_80GGA_Table",workbook)
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_PAN")
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6Ver_PAN")
            n = 12
            f_val = []
            pan_val = []
            # using list comprehension
            if find_val != []:
                final = [find_val[i * n:(i + 1) * n] for i in range((len(find_val) + n - 1) // n )]
                pan_match = [find_val[i * n:(i + 1) * n] for i in range((len(find_val) + n - 1) // n )]
                for d in final:
                    f_val.append(d[8])
                for p_match in pan_match:
                    pan_val.append(p_match[7])
                for val_value in f_val:
                    if val_value != None and val_value > 2000:
                        error_dict = {
                        "remark": "In Schedule 80GGA, amount donated in cash should not exceed Rs 2,000",
                        "validation_status": "Error",
                        "field_value": val_value,
                        "field_name": f"",
                        "error_code": "615",
                        "name_range": "ITR6_80GGA_Table"
                        }
                        error_list.append(error_dict)
                for m_val in f_val:
                    if m_val != None :
                        if (m_val == val_1 or m_val == val_2) :
                            error_dict = {
                            "remark": "In Sch 80GGA Donee PAN should not be same as “Assessee PAN” or “PAN at Verification”",
                            "validation_status": "Error",
                            "field_value": m_val,
                            "field_name": f"",
                            "error_code": "616",
                            "name_range": "ITR6_80GGA_Table"
                            }
                            error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_617(payload,error_list,workbook):
        '''
        Summery Line
        Value of ITR6_80GGA_Don_Tot is greater than zero, then ITR6ChVIA_Dedn_80GGA should be greater than zero
        '''
        try:
            val_1 = BusinessValidation.get_name_range_data(workbook,"ITR6_80GGA_Don_Tot",is_int=True)
            val_2 = BusinessValidation.get_name_range_data(workbook,"ITR6ChVIA_Dedn_80GGA",is_int=True)
            if val_1 > 0 and val_2 < 0:
                error_dict = {
                    "remark": "If deduction u/s 80GGA is claimed in Chaper VI-A, details shall be provided in Schedule 80GGA",
                    "validation_status": "Error",
                    "field_value": val_1,
                    "field_name": f"",
                    "error_code": "617",
                    "name_range": "ITR6_80GGA_Don_Tot"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_377(payload, error_list, workbook):
        '''
        Summery Line
            "In Schedule OS – column 3 of table 2e, the sum of all the
            dropdown value of Col 2 Amount of income of 1a(i) should not
            exceed the field 1a(i) “Dividend income [other than (ii)]”"
        '''
        try:
            value_range_data = workbook.defined_names["DTAA_Item_1ai"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
            if isinstance(value, (int, float)):
                dividend_flag = payload["ITR"]["ITR6"]["ScheduleOS"].get("IncOthThanOwnRaceHorse") and \
                    isinstance(payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("DividendOthThan22e"), (int, float))
                if dividend_flag and value > payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("DividendOthThan22e"):
                    error_dict = {
                            "remark": "Income subject to DTAA rate exceeds the income reported under respective field",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "377",
                            "name_range": "DTAA_Item_1ai"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_379(payload, error_list, workbook):
        '''
        Summery Line
            "In Schedule OS – column 3 of table 2e, the sum of dropdown value
            of Col 2 Amount of Income of 1c should not exceed the field 1c
            “Rental income from machinery, plants, buildings, etc., Gross”"

        '''
        try:
            value_range_data = workbook.defined_names["DTAA_Item_1c"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
            if isinstance(value, (int, float)):
                target_range_data = workbook.defined_names["ITR6OS_Rent"]
                target_destinations = list(target_range_data.destinations)
                target_ws, target_reg = target_destinations[0]
                if isinstance(target_ws, str):
                    # reading obj from wb object
                    target_ws = workbook[target_ws]
                target_region = target_ws[target_reg]
                target_value = target_region.value
                if isinstance(target_value, str):
                    target_value = int(target_value)
                if isinstance(target_value, (int, float)) and value > target_value:
                    error_dict = {
                            "remark": "Income subject to DTAA rate exceeds the income reported under respective field",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "379",
                            "name_range": "DTAA_Item_1c"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_380(payload, error_list, workbook):
        '''
        Summery Line
           "In Schedule OS – column 3 of table 2e, the sum of dropdown value
            of Col 2 Amount of income of 1d should not exceed the field 1d
            “Income of the nature referred to in section 56(2)(x) which is
            chargeable to tax “"
        '''
        try:
            value_range_data = workbook.defined_names["DTAA_Item_1d"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
            if isinstance(value, (int, float)):
                target_range_data = workbook.defined_names["ITR6OS_Inc_56_2_x"]
                target_destinations = list(target_range_data.destinations)
                target_ws, target_reg = target_destinations[0]
                if isinstance(target_ws, str):
                    # reading obj from wb object
                    target_ws = workbook[target_ws]
                target_region = target_ws[target_reg]
                target_value = target_region.value
                if isinstance(target_value, str):
                    target_value = int(target_value)
                if isinstance(target_value, (int, float)) and value > target_value:
                    error_dict = {
                            "remark": "Income subject to DTAA rate exceeds the income reported under respective field",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "380",
                            "name_range": "DTAA_Item_1d"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_381(payload, error_list, workbook):
        '''
        Summery Line
            "In Schedule OS – column 3 of table 2e, the sum of dropdown value
            of Col 2 Amount of Income of 2a should not exceed the field 2a
            “Winnings from lotteries, crossword puzzles etc. chargeable u/s
            115BB”"
        '''
        try:
            value_range_data = workbook.defined_names["DTAA_Item_2a"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
            if isinstance(value, (int, float)):
                target_range_data = workbook.defined_names["ITR6OS_Lott"]
                target_destinations = list(target_range_data.destinations)
                target_ws, target_reg = target_destinations[0]
                if isinstance(target_ws, str):
                    # reading obj from wb object
                    target_ws = workbook[target_ws]
                target_region = target_ws[target_reg]
                target_value = target_region.value
                if isinstance(target_value, str):
                    target_value = int(target_value)
                if isinstance(target_value, (int, float)) and value > target_value:
                    error_dict = {
                            "remark": "Income subject to DTAA rate exceeds the income reported under respective field",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "381",
                            "name_range": "DTAA_Item_2a"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_382(payload, error_list, workbook):
        '''
        Summery Line
            "In Schedule OS – column 3 of table 2e, the sum of dropdown value
            of Col 2 Amount of Income of 2c should not exceed the field 2c
            “Any other income chargeable at special rate” above"
        '''
        try:
            value_range_data = workbook.defined_names["DTAA_Item_2c"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
            if isinstance(value, (int, float)):
                target_range_data = workbook.defined_names["ITR6OS_Any_Oth_SP_Tot"]
                target_destinations = list(target_range_data.destinations)
                target_ws, target_reg = target_destinations[0]
                if isinstance(target_ws, str):
                    # reading obj from wb object
                    target_ws = workbook[target_ws]
                target_region = target_ws[target_reg]
                target_value = target_region.value
                if isinstance(target_value, str):
                    target_value = int(target_value)
                if isinstance(target_value, (int, float)) and value > target_value:
                    error_dict = {
                            "remark": "Income subject to DTAA rate exceeds the income reported under respective field",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "382",
                            "name_range": "DTAA_Item_2c"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_383(payload, error_list, workbook):
        '''
        Summery Line
            "In Schedule OS – column 3 of table 2e, the sum of dropdown value
            of Col 2 Amount of Income of 2d should not exceed the field 2d
            “Pass through income in the nature of income from other sources
            chargeable at special rates” above"
        '''
        try:
            value_range_data = workbook.defined_names["DTAA_Item_2d"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
            if isinstance(value, (int, float)):
                target_range_data = workbook.defined_names["ITR6OS_PTI_Tot"]
                target_destinations = list(target_range_data.destinations)
                target_ws, target_reg = target_destinations[0]
                if isinstance(target_ws, str):
                    # reading obj from wb object
                    target_ws = workbook[target_ws]
                target_region = target_ws[target_reg]
                target_value = target_region.value
                if isinstance(target_value, str):
                    target_value = int(target_value)
                if isinstance(target_value, (int, float)) and value > target_value:
                    error_dict = {
                            "remark": "Income subject to DTAA rate exceeds the income reported under respective field",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "383",
                            "name_range": "DTAA_Item_2d"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

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
    def rule_384(payload, error_list, workbook):
        '''
        Summery Line
            In schedule OS, deduction claimed at Sl. No. 3d or at Sl. No. 8b
            will not be allowed in case you have opted for benefit of lower
            taxation u/s 115BAB
        '''
        try:
            value = BusinessValidation.get_name_range_data(workbook, 'ITR6PAG1_Opt_115BA_BAA_BAB')
            if isinstance(value, (int, float)):
                target_value_1 = BusinessValidation.get_name_range_data(workbook, 'ITR6OS_PTI_Tot', \
                    is_int=True)
                target_value_2 = BusinessValidation.get_name_range_data(workbook, 'ITR6OS_Exp_Tot', \
                    is_int=True)
                if value and value.upper() == "115BAB" and isinstance(target_value_1, (int, float)) and \
                    isinstance(target_value_2, (int, float)) and (target_value_2 > 0 or target_value_2 > 0):
                    error_dict = {
                            "remark": "In schedule OS, deduction claimed at Sl. No. 3d or at Sl. No. 8b will "\
                                "not be allowed in case you have opted for benefit of lower taxation u/s 115BAB",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "384",
                            "name_range": "ITR6OS_RH_Ded & ITR6OS_Exp_Tot"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def validate_value(obj,all_paths,is_req_val=True):
        '''
        Summery Line
            validate list of value
        '''
        invalid_paths=[]
        all_paths_splitted = []
        for i in all_paths:
            all_paths_splitted.append(i.split("."))
        
        for el in all_paths_splitted:
            ml = len(el)
            dt={}
            for i,e in enumerate(el):
                if(i==(ml-1)):
                    if (e not in dt) or (is_req_val and (dt[e]=='' or dt[e]==0)) or (not is_req_val and (dt[e]!='' or dt[e]!=0)):
                        invalid_paths.append((".".join(el)))
                        break
                else:
                    if (i==0 and e not in obj) or (i>0 and e not in dt):
                        invalid_paths.append((".".join(el)))
                        break
                    else:
                        dt = obj[e] if i==0 else dt[e]
        return invalid_paths

    @staticmethod
    def find_acc_range(lists,workbook, is_req_val=True):
        '''
        Summery Line
            find value according to range
        '''
        retList=[]
        for i in lists:
            value_range_data = workbook.defined_names[i]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if (is_req_val and (value=='' or value==0 or value=='0' and value == None)) or (not is_req_val and value != "" and value != "0" and value != 0 and value != None):
            # if (is_req_val and (value=='' or value==0 or value=='0' or value == None)) or (not is_req_val and (value != "" or value != "0" or value != 0 or value != None)): # updated_03
                retList.append({"name":i,"value":value})
        return retList

    
    @staticmethod
    def find_value_f_range(name_range,values,workbook):
        s_values = []
        value_range_data = workbook.defined_names[name_range]
        sales_destinations = list(value_range_data.destinations)
        for sheetname, cellAddress in sales_destinations:
            cellAddress = cellAddress.replace('$','')
        worksheet = workbook[sheetname]
        for i in range(0,len(worksheet[cellAddress])):
            for e in list(filter(lambda x:x.coordinate in values,worksheet[cellAddress][i])):
                s_values.append(e.value)
        return s_values
    
    @staticmethod
    def rule_11(payload, error_list,workbook):
        '''
        Summery Line
            "If 'Y' is selected for the question 'Whether the financial statements of the company are drawn up in \
            compliance to the Indian Accounting Standards specified in Annexure to the companies (Indian Accounting Standards) \
            Rules, 2015' from Part A general 1 then Manufacturing A/c, Trading A/c, Profit & loss A/c & Balance sheet cannot be filled"
        '''
        error_dict = {
                    "remark": "If 'Y' is selected for the question 'Whether the financial statements of the company are drawn up in "\
                        "compliance to the Indian Accounting Standards specified in Annexure to the companies (Indian Accounting Standards) "\
                        "Rules, 2015' from Part A general 1 then Manufacturing A/c, Trading A/c, Profit & loss A/c & Balance sheet cannot be filled",
                    "field_name": "",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "11",
                    "name_range": ""
                }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["FinancialStmtFlag"] == "Y" :
                # arr = BusinessValidation.validate_value(payload,list1.keys(),is_req_val=False)
                # if arr != [] and arr != None :
                #     for ar in arr:
                #         copy_error = copy.deepcopy(error_dict)
                #         copy_error["field_name"] = ar
                #         copy_error["name_range"] = list1[ar]
                #         error_list.append(copy_error)
                range_arr = BusinessValidation.find_acc_range(list1, workbook, is_req_val=False)
                if range_arr != [] and range_arr != None:
                    for error in range_arr:
                        copy_error = copy.deepcopy(error_dict)
                        copy_error["field_value"] = error["value"]
                        copy_error["name_range"] = error["name"]
                        error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_12(payload, error_list,workbook):
        '''
        Summery Line
            "If 'N' is selected for the question 'Whether the financial statements of the company are drawn up in compliance to the Indian\
            Accounting Standards specified in Annexure to the companies (Indian Accounting Standards) Rules, 2015' from Part A general 1 \
            then Manufacturing A/c -Ind As, Trading A/c - Ind As, Profit & loss A/c-Ind As & Balance sheet -Ind As cannot be filled"
        '''
        error_dict = {
                    "remark": "If 'N' is selected for the question 'Whether the financial statements of the company are drawn up in compliance to the Indian"\
                        " Accounting Standards specified in Annexure to the companies (Indian Accounting Standards) Rules, 2015' from Part A general 1 "\
                        "then Manufacturing A/c -Ind As, Trading A/c - Ind As, Profit & loss A/c-Ind As & Balance sheet -Ind As cannot be filled",
                    "field_name": "",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "12",
                    "name_range": ""
                }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["FinancialStmtFlag"] == "N" :
                # arr = BusinessValidation.validate_value(payload,list2.keys(),is_req_val=False)
                # if arr != [] and arr != None :
                #     for ar in arr:
                #         copy_error = copy.deepcopy(error_dict)
                #         copy_error["field_name"] = ar
                #         copy_error["name_range"] = list2[ar]
                #         error_list.append(copy_error)
                range_arr = BusinessValidation.find_acc_range(list2, workbook,is_req_val=False)
                if range_arr != [] and range_arr != None:
                    for error in range_arr:
                        copy_error = copy.deepcopy(error_dict)
                        copy_error["field_value"] = error["value"]
                        copy_error["name_range"] = error["name"]
                        error_list.append(copy_error)
                
        except Exception:
            pass

    @staticmethod
    def rule_133(payload, error_list,workbook):
        '''
        Summery Line
            "If assessee is company under liquidation, then schedule OL should be mandatory"
            If ITR6PAG1_Und_Liq Is "Y"/"Yes", Then all names ranges in List 5 is mandatory
            ITR.ITR6.PartA_GEN1.FilingStatus.UnderLiquidation
        '''
        error_dict = {
                    "remark": "If assessee is company under liquidation, then schedule OL should be mandatory",
                    "field_name": "",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "133",
                    "name_range": ""
                }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["UnderLiquidation"] == "Y" :
                range_arr = BusinessValidation.find_acc_range(list5, workbook)
                if range_arr != [] and range_arr != None:
                    for error in range_arr:
                        copy_error = copy.deepcopy(error_dict)
                        copy_error["field_value"] = error["value"]
                        copy_error["name_range"] = error["name"]
                        error_list.append(copy_error)
                
        except Exception:
            pass

    # as discussed with chandani mam write fresh code of rule no 134 in FY24 sheet (rule 133 has been informed already)
    @staticmethod
    def rule_2024_134(payload, error_list, workbook):
        '''
        Summery Line
            "If assessee is company under liquidation, then schedule OL should be mandatory"
            If ITR6PAG1_Und_Liq Is "Y"/"Yes", Then all names ranges in List 5 is mandatory
            ITR.ITR6.PartA_GEN1.FilingStatus.UnderLiquidation
        '''
        error_dict = {
                    # "remark": "If assessee is company under liquidation, then schedule OL should be mandatory",
                    "remark": "Schedule OL cannot blank if 'Yes' is selected at whether the assessee company is under liquidation?",
                    "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.UnderLiquidation",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "134_2024",
                    "name_range": "ITR6PAG1_Und_Liq"
                }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["UnderLiquidation"] == "Y" :
                opn_val, clg_val = None, None
                opn_val = BusinessValidation.get_name_range_data(workbook, 'ITR6PAOL_Tot_Opn_Bal', is_int=True)
                clg_val = BusinessValidation.get_name_range_data(workbook, 'ITR6PAOL_Tot_Clg_Bal', is_int=True)
                if opn_val <=0 and clg_val<=0:
                    error_list.append(error_dict)
        except Exception:
            pass

    # @staticmethod
    # def rule_13(payload, error_list, workbook):
    #     '''
    #     Summery Line
    #         "If Assessee is liable for audit u/s 44AB, Part A BS and Part A P&L cannot be blank"
    #         If ITR6PAG1_Liab_Tax_Audit is 'Y', values in all the namerange in 'List 3' should not be blank
    #         ITR.ITR6.PartA_GEN2For6.LiableSec44ABflg
    #     '''
    #     error_dict = {
    #                 "remark": "If Assessee is liable for audit u/s 44AB, Part A BS and Part A P&L cannot be blank",
    #                 "field_name": "",
    #                 "validation_status": "Error",
    #                 "field_value": "",
    #                 "error_code": "13",
    #                 "name_range": ""
    #             }
    #     try:
    #         if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["LiableSec44ABflg"] == "Y" :
    #             # arr = BusinessValidation.validate_value(payload,list3.keys(),is_req_val=True)
    #             # for ar in arr:
    #             #     copy_error = copy.deepcopy(error_dict)
    #             #     copy_error["field_name"] = ar
    #             #     copy_error["name_range"] = list3[ar]
    #             #     error_list.append(copy_error)
    #             range_arr = BusinessValidation.find_acc_range(list3, workbook,is_req_val=True)
    #             for error in range_arr:
    #                 copy_error = copy.deepcopy(error_dict)
    #                 copy_error["field_value"] = error["value"]
    #                 copy_error["name_range"] = error["name"]
    #                 error_list.append(copy_error)
                
    #     except Exception:
    #         pass

    @staticmethod
    def rule_13(payload, error_list):
        '''
        Summery Line
        ITR6PAG1_Opt_115BA_BAA_BAB is selected as 115BA/115BAA/115BAA_BAB then ,
        ITR6PAG1_AY_115BA_BAA_BAB,ITR6PAG1_115BA_Ack_No, ITR6PAG1_115BA_filing_date_1 
        are mandatory
        '''
        error_dict = {
                    "remark": "",
                    "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.Section115BA",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "13",
                    "name_range": "ITR6PAG1_Opt_115BA_BAA_BAB"
                }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115BA"] == "115BAA" \
                or payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115BA"] == "115BAB"\
                    or payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115BA"] == "115BA": 

                filing_status_fields = [
                ("Section115BAAY", "ITR6PAG1_AY_115BA_BAA_BAB", "Please enter AY in which option for taxation u/s 115BA/115BAA/115BAB is exercised for the first time"),
                ("ReceiptNo115BA", "ITR6PAG1_115BA_Ack_No", "Please enter Acknowledgement number of relevant form filed (10-IB/10-IC/10-ID)"),
                ("115BAFormFiledDate", "ITR6PAG1_115BA_filing_date_1", "Please enter Date of filing of relevant form (10-IB/10-IC/10-ID)"),
            ]

            for field, name_range, remark in filing_status_fields:
                if not payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"][field]:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = f"ITR.ITR6.PartA_GEN1.FilingStatus.{field}"
                    copy_error["name_range"] = name_range
                    copy_error["field_value"] = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"][field]
                    copy_error["remark"] = remark
                    error_list.append(copy_error)

                                
        except Exception:
            pass

    @staticmethod
    def rule_14(payload, error_list):
        '''
        Summery Line
            #1
            Value of ITR6BS_TotEqt_Liab should be equal to ITR6BS_Tot_Asst and Value of ITR6BSIAS_TotEqt_Liab should be equal to ITR6BSIAS_Tot_Asst
            ITR.ITR6.PARTA_BSFor6FrmAY13.EquityAndLiablities.TotEquityAndLiabilities
            ITR.ITR6.PARTA_BSFor6FrmAY13.TotalAssets
            ITR.ITR6.PARTA_BSIndAS.EquityAndLiablities.Liabilities.CurrentLiabilities.TotalEquityLiab
            ITR.ITR6.PARTA_BSIndAS.TotalAssets

            #2
            Summery Line
            ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY is selected as "Y",
            then  ITR.ITR6.PartA_GEN1.FilingStatus.SectionCurrAY,
            ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAYRecNo,
            ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAYDate
            are mandatory.
        '''
        error_dict = {
                    "remark": "",
                    "field_name": "",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "14",
                    "name_range": ""
                }
        try:
            #1
            if payload["ITR"]["ITR6"]["PARTA_BSFor6FrmAY13"]["EquityAndLiablities"]["TotEquityAndLiabilities"] != payload["ITR"]["ITR6"]["PARTA_BSFor6FrmAY13"]["TotalAssets"]:
                copy_error = copy.deepcopy(error_dict)
                copy_error["field_value"] = payload["ITR"]["ITR6"]["PARTA_BSFor6FrmAY13"]["EquityAndLiablities"]["TotEquityAndLiabilities"]
                copy_error["field_name"] = "ITR.ITR6.PARTA_BSFor6FrmAY13.EquityAndLiablities.TotEquityAndLiabilities"
                copy_error["name_range"] = "ITR6BS_TotEqt_Liab"
                copy_error["remark"] = "In the Balance Sheet : Total of Equity & Liability should be equal to total of Assets"
                error_list.append(copy_error)

            if payload["ITR"]["ITR6"]["PARTA_BSIndAS"]["EquityAndLiablities"]["Liabilities"]["CurrentLiabilities"]["TotalEquityLiab"] != payload["ITR"]["ITR6"]["PARTA_BSIndAS"]["TotalAssets"]:
                copy_error = copy.deepcopy(error_dict)
                copy_error["field_value"] = payload["ITR"]["ITR6"]["PARTA_BSIndAS"]["EquityAndLiablities"]["Liabilities"]["CurrentLiabilities"]["TotalEquityLiab"]
                copy_error["field_name"] = "ITR.ITR6.PARTA_BSIndAS.EquityAndLiablities.Liabilities.CurrentLiabilities.TotalEquityLiab"
                copy_error["name_range"] = "ITR6BSIAS_TotEqt_Liab"
                copy_error["remark"] = "In the Balance Sheet : Total of Equity & Liability should be equal to total of Assets"
                error_list.append(copy_error)
            #2
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["Section115CurrAY"] == "Y":
                filing_status_fields = [
                ("Section115CurrAY", "ITR6PAG1_Opt_115BA_BAA_BAB_Sec", "Please enter section in which option for taxation is exercised"),
                ("Section115CurrAYRecNo", "ITR6PAG1_115BA_Ack_No_2", "Please enter Acknowledgement number of relevant form filed (10-IB/10-IC/10-ID)"),
                ("Section115CurrAYDate", "ITR6PAG1_115BA_filing_date_2", "Please enter Date of filing of relevant form (10-IB/10-IC/10-ID)"),
            ]

            for field, name_range, remark in filing_status_fields:
                if not payload["PartA_GEN1"]["FilingStatus"][field]:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_value"] = payload["PartA_GEN1"]["FilingStatus"][field]
                    copy_error["field_name"] = f"ITR.ITR6.PartA_GEN1.FilingStatus.{field}"
                    copy_error["name_range"] = name_range
                    copy_error["remark"] = remark
                    error_list.append(copy_error)

        except Exception:
            pass
    
    @staticmethod
    def rule_84(payload,error_list, workbook):
        '''
        Summery Line
            "If ITR6PL_Description_Table column Business Code has a value, then ITR6PL_PremInc_44AE_Tot_2 should be greater than zero",
        '''
        try:
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
            find_val = find_table("ITR6PL_Description_Table",workbook)
            match_val = BusinessValidation.get_name_range_data(workbook,"ITR6PL_PremInc_44AE_Tot_2",is_int=True)
            n = 9
            f_val = []
            # using list comprehension
            if find_val != []:
                final = [find_val[i * n:(i + 1) * n] for i in range((len(find_val) + n - 1) // n )]
            for d in final:
                f_val.append(d[4])
            if len(f_val) != 0 and sum(x is None for x in f_val) != len(f_val) and match_val <= 0:
                error_dict = {
                            "remark": "If 'business code' u/s 44AE is selected, then it is mandatory to declare income u/s 44AE.",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": match_val,
                            "error_code": "84",
                            "name_range": "ITR6PL_Description_Table"
                    }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_87(payload ,error_list, workbook):
        '''
        Summery Line
            "Tonnage capacity cannot exceed 100MT in Sl. No. 61 of Profit & Loss account",
        '''
        try:
            value_range_data = workbook.defined_names["ITR6PL_PremInc_Tonnage"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
                if isinstance(value, (int, float)) and value > 100:
                    error_dict = {
                            "remark": "Tonnage capacity cannot exceed 100MT in Sl. No. 61 of Profit & Loss account",
                            "field_name": f"",
                            "validation_status": "Error",
                            "field_value": value,
                            "error_code": "87",
                            "name_range": "ITR6PL_PremInc_Tonnage"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_94(payload, error_list,workbook):
        '''
        Summery Line
            "In Part A P&L, if assessee has opted for taxation u/s 44B, SI. No.
            62b "Net Profit" cannot be less than 7.5% of " Gross receipts/turnover"
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"] == "Y" :
                value_range_data = workbook.defined_names["ITR6PL_No_Acc_NP_Sec44B"]
                sales_destinations = list(value_range_data.destinations)
                sales_ws, sales_reg = sales_destinations[0]
                if isinstance(sales_ws, str):
                    # reading obj from wb object
                    sales_ws = workbook[sales_ws]
                sales_region = sales_ws[sales_reg]
                value = sales_region.value
                if isinstance(value, str):
                    value = int(value)
                if isinstance(value, (int, float)):
                    target_range_data = workbook.defined_names["ITR6PL_No_Acc_Exp_Sec44B"]
                    target_destinations = list(target_range_data.destinations)
                    target_ws, target_reg = target_destinations[0]
                    if isinstance(target_ws, str):
                        # reading obj from wb object
                        target_ws = workbook[target_ws]
                    target_region = target_ws[target_reg]
                    target_value = target_region.value
                    if isinstance(target_value, str):
                        target_value = int(target_value)
                    if isinstance(target_value, (int, float)) and value < round(target_value*7.5/100,2):
                        error_dict = {
                        "remark": "In Part A P&L, if assessee has opted for taxation u/s 44B, SI. No."\
                                "62b 'Net Profit' cannot be less than 7.5% of 'Gross receipts/turnover'",
                        "field_name": "ITR.ITR6.PartA_GEN2For6.IncDclrdUs",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"],
                        "error_code": "94",
                        "name_range": "ITR6PAG1_Pres_Inc"
                    }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_95(payload, error_list,workbook):
        '''
        Summery Line
            "In Part A P&L, if assessee has opted for taxation u/s 44BB, SI. No.
            62b "Net Profit " cannot be less than 10% of " Gross receipts/turnover"
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"] == "Y" :
                value_range_data = workbook.defined_names["ITR6PL_No_Acc_NP_Sec44BB"]
                sales_destinations = list(value_range_data.destinations)
                sales_ws, sales_reg = sales_destinations[0]
                if isinstance(sales_ws, str):
                    # reading obj from wb object
                    sales_ws = workbook[sales_ws]
                sales_region = sales_ws[sales_reg]
                value = sales_region.value
                if isinstance(value, str):
                    value = int(value)
                if isinstance(value, (int, float)):
                    target_range_data = workbook.defined_names["ITR6PL_No_Acc_Exp_Sec44BB"]
                    target_destinations = list(target_range_data.destinations)
                    target_ws, target_reg = target_destinations[0]
                    if isinstance(target_ws, str):
                        # reading obj from wb object
                        target_ws = workbook[target_ws]
                    target_region = target_ws[target_reg]
                    target_value = target_region.value
                    if isinstance(target_value, str):
                        target_value = int(target_value)
                    if isinstance(target_value, (int, float)) and value < round(target_value*10/100,2):
                        error_dict = {
                        "remark": "In Part A P&L, if assessee has opted for taxation u/s 44BB, SI. No."\
                            "62b 'Net Profit' cannot be less than 10% of 'Gross receipts/turnover'",
                        "field_name": "ITR.ITR6.PartA_GEN2For6.IncDclrdUs",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"],
                        "error_code": "95",
                        "name_range": "ITR6PAG1_Pres_Inc"
                    }
                error_list.append(error_dict)
        except Exception:
            pass

    
    @staticmethod
    def rule_96(payload, error_list,workbook):
        '''
        Summery Line
            "In Part A P&L, if assessee has opted for taxation u/s 44BB, SI. No.
            62b "Net Profit " cannot be less than 10% of " Gross receipts/turnover"
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"] == "Y" :
                value_range_data = workbook.defined_names["ITR6PL_No_Acc_NP_Sec44BBA"]
                sales_destinations = list(value_range_data.destinations)
                sales_ws, sales_reg = sales_destinations[0]
                if isinstance(sales_ws, str):
                    # reading obj from wb object
                    sales_ws = workbook[sales_ws]
                sales_region = sales_ws[sales_reg]
                value = sales_region.value
                if isinstance(value, str):
                    value = int(value)
                if isinstance(value, (int, float)):
                    target_range_data = workbook.defined_names["ITR6PL_No_Acc_Exp_Sec44BBA"]
                    target_destinations = list(target_range_data.destinations)
                    target_ws, target_reg = target_destinations[0]
                    if isinstance(target_ws, str):
                        # reading obj from wb object
                        target_ws = workbook[target_ws]
                    target_region = target_ws[target_reg]
                    target_value = target_region.value
                    if isinstance(target_value, str):
                        target_value = int(target_value)
                    if isinstance(target_value, (int, float)) and value < round(target_value*5/100,2):
                        error_dict = {
                        "remark": "In Part A P&L, if assessee has opted for taxation u/s 44BB, SI. No."\
                            "62b 'Net Profit' cannot be less than 5% of 'Gross receipts/turnover'",
                        "field_name": "ITR.ITR6.PartA_GEN2For6.IncDclrdUs",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"],
                        "error_code": "96",
                        "name_range": "ITR6PAG1_Pres_Inc"
                    }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_97(payload, error_list,workbook):
        '''
        Summery Line
            "In Part A P&L, if assessee has opted for taxation u/s 44BB, SI. No.
            62b "Net Profit " cannot be less than 5% of " Gross receipts/turnover"
            If ITR6PAG1_Pres_Inc is 'Y, then ITR6PL_No_Acc_NP_Sec44BBB cannot be les than 10% of ITR6PL_No_Acc_Exp_Sec44BBB
        '''
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"] == "Y" :
                value_range_data = workbook.defined_names["ITR6PL_No_Acc_NP_Sec44BBB"]
                sales_destinations = list(value_range_data.destinations)
                sales_ws, sales_reg = sales_destinations[0]
                if isinstance(sales_ws, str):
                    # reading obj from wb object
                    sales_ws = workbook[sales_ws]
                sales_region = sales_ws[sales_reg]
                value = sales_region.value
                if isinstance(value, str):
                    value = int(value)
                if isinstance(value, (int, float)):
                    target_range_data = workbook.defined_names["ITR6PL_No_Acc_Exp_Sec44BBB"]
                    target_destinations = list(target_range_data.destinations)
                    target_ws, target_reg = target_destinations[0]
                    if isinstance(target_ws, str):
                        # reading obj from wb object
                        target_ws = workbook[target_ws]
                    target_region = target_ws[target_reg]
                    target_value = target_region.value
                    if isinstance(target_value, str):
                        target_value = int(target_value)
                    if isinstance(target_value, (int, float)) and value < round(target_value*5/100,2):
                        error_dict = {
                        "remark": "In Part A P&L, if assessee has opted for taxation u/s 44BB, SI. No."\
                            "62b 'Net Profit' cannot be less than 5% of 'Gross receipts/turnover'",
                        "field_name": "ITR.ITR6.PartA_GEN2For6.IncDclrdUs",
                        "validation_status": "Error",
                        "field_value": payload["ITR"]["ITR6"]["PartA_GEN2For6"]["IncDclrdUs"],
                        "error_code": "97",
                        "name_range": "ITR6PAG1_Pres_Inc"
                    }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_99(payload, error_list,workbook):
        '''
        Summery Line
            "In P&L, for 44AE same registration number of good carriages
                cannot be entered more than once."
        '''
        try:
            value_range_data = workbook.defined_names["ITR6PL_Reg_no_check"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if isinstance(value, str):
                value = int(value)
            if isinstance(value, (int, float)) and value > 1:
                error_dict = {
                    "remark": "In P&L, for 44AE same registration number of good carriages"\
                        "cannot be entered more than once.",
                    "field_name": "ITR.ITR6.PARTA_PL.TotalPrsumptvIncUs44E",
                    "validation_status": "Error",
                    "field_value": value,
                    "error_code": "99",
                    "name_range": "ITR6PL_Reg_no_check"
                }
            error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_181(payload,error_list,workbook):
        '''
        Summery Line
        "In schedule BP ""Sl. No. 28 Deduction allowable under section
        32 AD"" cannot be more than ""0"""
        ITR6PGBP_Dedn_32AD cannot be more than Zero
        ITR6PGBP_Dedn_32AD
        '''
        try:
            value_range_data = workbook.defined_names["ITR6PGBP_Dedn_32AD"]
            sales_destinations = list(value_range_data.destinations)
            sales_ws, sales_reg = sales_destinations[0]
            if isinstance(sales_ws, str):
                # reading obj from wb object
                sales_ws = workbook[sales_ws]
            sales_region = sales_ws[sales_reg]
            value = sales_region.value
            if value > 0:
                error_dict = {
                    "remark": 'In schedule BP Sl. No. 28 Deduction allowable under section32 AD cannot be more than "0"',
                    "validation_status": "Error",
                    "field_value": value,
                    "field_name" : f"ITR6PGBP_Dedn_32AD",
                    "error_code": "181",
                    "name_range": "ITR6PGBP_Dedn_32AD"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_184(payload, error_list,workbook):
        '''
        Summery Line
            itr6pgbp_cy_inc_spebi
        '''
        try:
            itr6pgbp_cy_inc_spebi = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_CY_Inc_SpeBI",is_int=True)
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
            itr6pgbp_section_table = find_table("ITR6PGBP_Section_Table",workbook)
            # itr6pgbp_section_table = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_Section_Table",is_int=True)
            if itr6pgbp_cy_inc_spebi > 0 and None in itr6pgbp_section_table:
                error_dict = {
                    "remark": "In Schedule BP, If income/ loss from specified business is entered then nature of specified business cannot be blank",
                    "validation_status": "Error",
                    "field_value": itr6pgbp_cy_inc_spebi,
                    "field_name" : f"",
                    "error_code": "184",
                    "name_range": "ITR6PGBP_CY_Inc_SpeBI"
                }
                error_list.append(error_dict)
        except Exception:
            pass



    @staticmethod
    def rule_186(payload, error_list,workbook):
        '''
        Summery Line
        Value of ITR6PGBP_Oth_Exmpt_Tot cannot be less than ITR6EI_Amt_Tot 
        If ITR6PAG1_Residential_status is NRI - Non-Resident, then value in Row 39 and 4o of ITR6SI_Table canot be greater then Zero (31 and 32)
        '''
        error_dict = {
                        "remark": "Non-resident taxpayer cannot offer income u/s 115BBF",
                        "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.ResidentialStatus",
                        "validation_status": "Error",
                        "field_value": f"",
                        "error_code": "186",
                        "name_range": "ITR6SI_Table"
                    }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("ResidentialStatus") == "NRI":
                values = ["G31","G32"]
                val = BusinessValidation.find_value_f_range("ITR6SI_Table",values,workbook)
                if val != [] and val != None :
                    for i in val:
                        if i > 0 :
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = i
                            copy_error["field_name"] = "ITR.ITR6.PartA_GEN1.FilingStatus.ResidentialStatus"
                            error_list.append(copy_error)
                val_1 = BusinessValidation.get_name_range_data(workbook, "ITR6FSI_Tot_TR_1", is_int=True)
                val_2 = BusinessValidation.get_name_range_data(workbook, "ITR6FSI_Tot_TR_2", is_int=True)
                # if val_1 != 0 and val_2 != 0:
                if val_1 not in [None, "", 0] and val_2 not in [None, "", 0]:
                    error_dict = {
                        "remark": "Schedule FSI is not applicable for Non-residents",
                        "validation_status": "Error",
                        "field_value": val_1,
                        "field_name": f"",
                        "error_code": "515",
                        "name_range": "ITR6FSI_Tot_TR_1"
                    }
                    error_list.append(error_dict)

                val_3 = BusinessValidation.get_name_range_data(workbook, "ITR6TR_Tot_Tax_Paid", is_int=True)
                val_4 = BusinessValidation.get_name_range_data(workbook, "ITR6TR_Tot_Tax_Relief", is_int=True)
                if val_3 < 0 and val_4 < 0:
                    error_dict = {
                        "remark": "Schedule TR is not applicable for Non-residents",
                        "validation_status": "Error",
                        "field_value": val_3,
                        "field_name": f"",
                        "error_code": "524",
                        "name_range": "ITR6TR_Tot_Tax_Paid"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_192(payload, error_list,workbook):
        '''
        Summery Line
        If in Schedule SI, benefit of Income from Insurance Business u/s 115B is claimed then it is mandatory to fill Sl. No. 4b of Schedule BP
        ITR.ITR6.CorpScheduleBP.BusinessIncOthThanSpec.PLUs44sChapXIIGUs115B
        '''
        
        error_dict = {
                        "remark": "If in Schedule SI, benefit of Income from Insurance Business u/s 115B is claimed then it is mandatory to fill Sl. No. 4b of Schedule BP",
                        "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.ResidentialStatus",
                        "validation_status": "Error",
                        "field_value": f"",
                        "error_code": "186",
                        "name_range": "ITR6SI_Table"
        }
        try:
            if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("PLUs44sChapXIIGUs115B") and \
                isinstance(payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("PLUs44sChapXIIGUs115B"),(int,float)):
                val_1 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("PLUs44sChapXIIGUs115B")
                values = ["G4"]
                val = BusinessValidation.find_value_f_range("ITR6SI_Table",values,workbook)
                if val != [] and val != None :
                    for i in val:
                        if i != val_1:
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = i
                            error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_137(payload, error_list,workbook):
        '''
        Summery Line
            ITR6HP1_Perc_Share
        '''
        error_dict = {
            "remark": "Assessee share of co-owned property is zero then interest on"\
                    "borrowed capital cannot be be claimed.",
            "validation_status": "Error",
            "field_value": f"",
            "field_name": f"",
            "error_code": "137",
            "name_range": ""
        }
        try:
            itr6hp1_perc_share = BusinessValidation.get_name_range_data(workbook,"ITR6HP1_Perc_Share",is_int=True)
            itr6hp1_int_borr_cap = BusinessValidation.get_name_range_data(workbook,"ITR6HP1_Int_Borr_Cap",is_int=True)
            if itr6hp1_perc_share == 0 and itr6hp1_int_borr_cap != 0:
                copy_error = copy.deepcopy(error_dict)
                copy_error["field_name"] = f""
                copy_error["name_range"] = "ITR6HP1_Perc_Share"
                copy_error["field_value"] = itr6hp1_perc_share
                error_list.append(copy_error)
            itr6hp2_perc_share = BusinessValidation.get_name_range_data(workbook,"ITR6HP2_Perc_Share",is_int=True)
            itr6hp2_int_borr_cap = BusinessValidation.get_name_range_data(workbook,"ITR6HP2_Int_Borr_Cap",is_int=True)
            if itr6hp2_perc_share == 0 and itr6hp2_int_borr_cap != 0:
                copy_error = copy.deepcopy(error_dict)
                copy_error["field_name"] = f""
                copy_error["name_range"] = "ITR6HP2_Perc_Share"
                copy_error["field_value"] = itr6hp2_perc_share
                error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_141(payload, error_list,workbook):
        '''
        Summery Line
            If ITR6HP1_Type is not 'N - Self Occupied', then ITR6HP1_Gross_Rent cannot be zero
            If ITR6HP2_Type is not 'N - Self Occupied', then ITR6HP2_Gross_Rent cannot be zero
        '''
        error_dict = {
                    "remark": "If Type of property is let-out or deemed let out then Gross rent in Schedule HP cannot be 0.",
                    "field_name": f"",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "141",
                    "name_range": ""
                }
        try:
            value_1 = BusinessValidation.get_name_range_data(workbook,"ITR6HP1_Type")
            value_2 = BusinessValidation.get_name_range_data(workbook,"ITR6HP2_Type")
            target_value_1 = BusinessValidation.get_name_range_data(workbook, "ITR6HP1_Gross_Rent",is_int=True)
            target_value_2 = BusinessValidation.get_name_range_data(workbook, "ITR6HP2_Gross_Rent",is_int=True)
            if value_1 == "N - Self Occupied" and target_value_1 == 0:
                copy_error = copy.deepcopy(error_dict)
                copy_error["field_name"] = f""
                copy_error["name_range"] = "ITR6HP1_Type"
                copy_error["field_value"] = value_1
                error_list.append(copy_error)
            if value_2 == "N - Self Occupied" and target_value_2 == 0:
                copy_error = copy.deepcopy(error_dict)
                copy_error["field_name"] = f""
                copy_error["name_range"] = "ITR6HP2_Type"
                copy_error["field_value"] = value_2
                error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_418(payload, error_list,workbook):
        '''
        Summery Line
            "Schedule BFLA,, Sl No 2(i) Brought forward HP Loss should be
            equal to Sl No 4(xiv) adjustment of above losses in Schedule
            BFLA, of CFL"
            ITR6BFLA_HP_Col_2 and ITR6CFL_HPL_Bal_Avbl should be equal
            ITR6BFLA_HP_Col_2 ITR.ITR6.ScheduleBFLA.HP.IncBFLA.BFlossPrevYrUndSameHeadSetoff

        '''
        error_dict = {
                    "remark": "Schedule BFLA,, Sl No 2(i) Brought forward HP Loss should be equal to Sl No 4(xiv) adjustment of above losses in Schedule BFLA, of CFL",
                    "field_name": f"",
                    "validation_status": "Error",
                    "field_value": "",
                    "error_code": "418",
                    "name_range": ""
                }
        try:
            value_1 = BusinessValidation.get_name_range_data(workbook,"ITR6BFLA_HP_Col_2")
            value_2 = BusinessValidation.get_name_range_data(workbook,"ITR6CFL_HPL_Bal_Avbl")
            if value_1 != value_2:
                copy_error = copy.deepcopy(error_dict)
                copy_error["field_name"] = f""
                copy_error["name_range"] = "ITR6BFLA_HP_Col_2"
                copy_error["field_value"] = value_1
                error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_146(payload, error_list,workbook):
        '''
        Summery Line
        ITR.ITR6.ScheduleHP.PassThroghIncome
        =SUM(ITR6PTI_HP_NL_1,ITR6PTI_HP_NL_2,ITR6PTI_HP_NL_3,ITR6PTI_HP_NL_4,ITR6PTI_HP_NL_5)
        '''
        try:
            value_1 = BusinessValidation.get_name_range_data(workbook,"ITR6HP1_Income_HP_PTI")
            # if isinstance(value_1, (int,float)):
            #     value_1 = value_1
            # else:
            if not isinstance(value_1, (int,float)):
                value_1 = 0
            target_value_1 = BusinessValidation.get_name_range_data(workbook, "ITR6PTI_HP_NL_1")
            # if isinstance(target_value_1, (int,float)):
            #     target_value_1 = target_value_1
            # else:
            if not isinstance(target_value_1, (int,float)):
                target_value_1 = 0
            target_value_2 = BusinessValidation.get_name_range_data(workbook, "ITR6PTI_HP_NL_2")
            # if isinstance(target_value_2, (int,float)):
            #     target_value_2 = target_value_2
            # else:
            if not isinstance(target_value_2, (int,float)):
                target_value_2 = 0
            target_value_3 = BusinessValidation.get_name_range_data(workbook, "ITR6PTI_HP_NL_3")
            # if isinstance(target_value_3, (int,float)):
            #     target_value_3 = target_value_3
            # else:
            if not isinstance(target_value_3, (int,float)):
                target_value_3 = 0
            target_value_4 = BusinessValidation.get_name_range_data(workbook, "ITR6PTI_HP_NL_4")
            # if isinstance(target_value_4, (int,float)):
            #     target_value_4 = target_value_4
            # else:
            if not isinstance(target_value_4, (int,float)):
                target_value_4 = 0
            target_value_5 = BusinessValidation.get_name_range_data(workbook, "ITR6PTI_HP_NL_5")
            # if isinstance(target_value_5, (int,float)):
            #     target_value_5 = target_value_5
            # else:
            if not isinstance(target_value_5, (int,float)):
                target_value_5 = 0
            
            sum_amt = target_value_1 + target_value_2 + target_value_3 + target_value_4 + target_value_5
            if value_1 != sum_amt:
                error_dict = {
                    "remark": "In Schedule HP, SI. No. 3 Pass through income should be equal to equal to the amount of net income/ loss of HP mentioned in Schedule PTI",
                    "validation_status": "Error",
                    "field_value": value_1,
                    "field_name": f"",
                    "error_code": "146",
                    "name_range": "ITR6HP1_Income_HP_PTI"
                }
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_214(payload, error_list, workbook):
        '''
        Summery Line
        In Schedule BP, sum of values entered from 37(i) to 37(ix) should match with sum of values declared at SI. No. 4a(i) to 4a(ix) respectively
        match table values "Annexure" sheet
        '''
        error_dict = {
            "remark": "In Schedule BP, sum of values entered from 37(i) to 37(ix) should match with sum of values declared at SI. No. 4a(i) to 4a(ix) respectively",
            "field_name": "",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "214",
            "name_range": ""
        }
        try:
            if payload["ITR"]["ITR6"]["PARTA_OI"].get("DeemedProfUs33AB") and payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("DeemIncUs33AB"):
                val_1 = payload["ITR"]["ITR6"]["PARTA_OI"].get("DeemedProfUs33AB")
                val_2 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("DeemIncUs33AB")
                if val_1 != val_2:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = "ITR.ITR6.PARTA_OI.DeemedProfUs33AB"
                    copy_error["name_range"] = "ITR6OI_Deem_33AB"
                    error_list.append(copy_error)
            
            if payload["ITR"]["ITR6"]["PARTA_OI"].get("DeemedProfUs33ABA") and payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("DeemIncUs33ABA"):
                val_1 = payload["ITR"]["ITR6"]["PARTA_OI"].get("DeemedProfUs33ABA")
                val_2 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("DeemIncUs33ABA")
                if val_1 != val_2:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = "ITR.ITR6.PARTA_OI.DeemedProfUs33ABA"
                    copy_error["name_range"] = "ITR6OI_Deem_33ABA"
                    error_list.append(copy_error)

            if payload["ITR"]["ITR6"]["PARTA_OI"].get("DeemedProfUs33AC") and payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("DeemIncUs33AC"):
                val_1 = payload["ITR"]["ITR6"]["PARTA_OI"].get("DeemedProfUs33AC")
                val_2 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"].get("DeemIncUs33AC")
                if val_1 != val_2:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = "ITR.ITR6.PARTA_OI.DeemedProfUs33AC"
                    copy_error["name_range"] = "ITR6OI_Deem_33AC"
                    error_list.append(copy_error)

            # match according to range
            check_list4_1 = BusinessValidation.find_acc_range(list4_1,workbook)
            check_list4_2 = BusinessValidation.find_acc_range(list4_2,workbook)
            s_val = []
            for i,e in enumerate(check_list4_1):
                if e["value"]!=check_list4_2[i]["value"]:
                    s_val.append(check_list4_2[i])
            if s_val != None and s_val != []:
                for ai in s_val:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = f""
                    copy_error["name_range"] = ai
                    error_list.append(copy_error)

        except Exception:
            pass

    @staticmethod
    def rule_208(payload, error_list,workbook):
        '''
        Summery Line
        Value of ITR6PGBP_Oth_Exmpt_Tot cannot be less than ITR6EI_Amt_Tot 
        '''
        error_dict = {
                        "remark": "Amount can be reduced from Schedule BP at SI. No. A4c i.e. Profit from activities covered under rule 7A, 7B(1), \
                            7B(1A) and 8 only if business code is selected as 1003, 1002, 1001 respectively",
                        "field_name": "ITR.ITR6.CorpScheduleBP.BusinessIncOthThanSpec.ProfitFrmActCvrd.ProfitFrmActCvrdUndrRule7A",
                        "validation_status": "Error",
                        "field_value": f"",
                        "error_code": "208",
                        "name_range": "ITR6_NatureOfBusiness"
                    }
        try:
            if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule7A") > 0:
                values = ["F4","F5","F6"]
                val = BusinessValidation.find_value_f_range("ITR6_NatureOfBusiness",values,workbook)
                if val != [] and val != None :
                    for i in val:
                        if i!='01003':
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = i
                            error_list.append(copy_error)
            if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule7B1") and\
                isinstance(payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule7B1",0), (int,float)):
                val_1 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule7B1")
                val_2 = 0
                if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule7B1A") and\
                    isinstance(payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule7B1A",0), (int,float)):
                    val_2 = payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule7B1A")
                sum = val_1 + val_2
                if sum > 0:
                    values = ["F4","F5","F6"]
                    val = BusinessValidation.find_value_f_range("ITR6_NatureOfBusiness",values,workbook)
                    if val != [] and val != None :
                        for i in val:
                            if i != '01002':
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["field_value"] = i
                                error_list.append(copy_error)
            if payload["ITR"]["ITR6"]["CorpScheduleBP"]["BusinessIncOthThanSpec"]["ProfitFrmActCvrd"].get("ProfitFrmActCvrdUndrRule8") > 0:
                values = ["F4","F5","F6"]
                val = BusinessValidation.find_value_f_range("ITR6_NatureOfBusiness",values,workbook)
                if val != [] and val != None :
                    for i in val:
                        if i!='01001':
                            copy_error = copy.deepcopy(error_dict)
                            copy_error["field_value"] = i
                            error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_209(payload, error_list,workbook):
        '''
        Summery Line
            If ITR6PAG1_Opt_115BA_BAA_BAB or ITR6PAG1_Opt_115BA_BAA_BAB_Sec is 115BA - Section 115BA or 115BAA - Section 
            115BAA or 115BAB - Section 115BAB then ITR6PGBP_Dedn_35AD_1 should be zero
        '''
        try:
            itr6pag1_opt_115ba_baa_bab = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_Opt_115BA_BAA_BAB")
            itr6pag1_opt_115ba_baa_bab_sec = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_Opt_115BA_BAA_BAB_Sec")
            itr6pgbp_dedn_35ad_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_Dedn_35AD_1")
            
            if (itr6pag1_opt_115ba_baa_bab == "115BA - Section 115BA" or itr6pag1_opt_115ba_baa_bab == "115BAA - Section 115BAA" or itr6pag1_opt_115ba_baa_bab == "115BAB - Section 115BAB") or \
                (itr6pag1_opt_115ba_baa_bab_sec == "115BA - Section 115BA" or itr6pag1_opt_115ba_baa_bab_sec == "115BAA - Section 115BAA" or itr6pag1_opt_115ba_baa_bab_sec == "115BAB - Section 115BAB"):
                if itr6pgbp_dedn_35ad_1 != 0 :
                    error_dict = {
                        "remark": "If opted for benefit of lower rate of taxation u /s 115BAB/ 115BA/ 115BAA, deduction u/s 35AD (Sl. No. 49) in Schedule BP cannot be claimed",
                        "validation_status": "Error",
                        "field_value": itr6pgbp_dedn_35ad_1,
                        "field_name": f"",
                        "error_code": "209",
                        "name_range": "ITR6PGBP_Dedn_35AD_1"
                    }
                    error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_210(payload, error_list,workbook):
        '''
        Summery Line
           If ITR6PAG1_Opt_115BA_BAA_BAB or ITR6PAG1_Opt_115BA_BAA_BAB_Sec is 115BAA - Section 115BAA or 115BAB - Section 115BAB then ITR6PGBP_Dedn_35AD_1, 
           ITR6ESR_Excess_351ii, ITR6ESR_Excess_351iia, ITR6ESR_Excess_351iii, ITR6ESR_Excess_35_2AA and ITR6ESR_Excess_35CCC should be zero
        '''
        error_dict = {
            "remark": "In schedule BP, 'Deductions in accordance with section 35AD(1)' or In schedule ESR deduction u/s 35(1)(ii), 35(1)(iia), "\
                        "35(1)(iii), 35(2AA) or 35CCC cannot be claimed if 115BAA or 115BAB is opted",
            "validation_status": "Error",
            "field_value": "",
            "field_name": f"",
            "error_code": "210",
            "name_range": ""
        }
        try:
            itr6pag1_opt_115ba_baa_bab = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_Opt_115BA_BAA_BAB")
            itr6pag1_opt_115ba_baa_bab_sec = BusinessValidation.get_name_range_data(workbook,"ITR6PAG1_Opt_115BA_BAA_BAB_Sec")

            if (itr6pag1_opt_115ba_baa_bab == "115BA - Section 115BA" or itr6pag1_opt_115ba_baa_bab == "115BAA - Section 115BAA" or itr6pag1_opt_115ba_baa_bab == "115BAB - Section 115BAB") or \
                (itr6pag1_opt_115ba_baa_bab_sec == "115BA - Section 115BA" or itr6pag1_opt_115ba_baa_bab_sec == "115BAA - Section 115BAA" or itr6pag1_opt_115ba_baa_bab_sec == "115BAB - Section 115BAB"):
                
                itr6pgbp_dedn_35ad_1 = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_Dedn_35AD_1",is_int=True)
                itr6esr_excess_351ii = BusinessValidation.get_name_range_data(workbook,"ITR6ESR_Excess_351ii",is_int=True)
                itr6esr_excess_351iia = BusinessValidation.get_name_range_data(workbook,"ITR6ESR_Excess_351iia",is_int=True)
                itr6esr_excess_351iii = BusinessValidation.get_name_range_data(workbook,"ITR6ESR_Excess_351iii",is_int=True)
                itr6esr_excess_35_2aa = BusinessValidation.get_name_range_data(workbook,"ITR6ESR_Excess_35_2AA",is_int=True)
                itr6esr_excess_35ccc = BusinessValidation.get_name_range_data(workbook,"ITR6ESR_Excess_35CCC",is_int=True)
                
                if itr6pgbp_dedn_35ad_1 != 0 and itr6esr_excess_351ii != 0 and itr6esr_excess_351iia != 0 and itr6esr_excess_351iii != 0 and itr6esr_excess_35_2aa != 0 and itr6esr_excess_35ccc != 0:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_value"] = itr6pgbp_dedn_35ad_1
                    copy_error["name_range"] = "ITR6PGBP_Dedn_35AD_1"
                    error_list.append(copy_error)

                itr6mat_p_l_pat = BusinessValidation.get_name_range_data(workbook,"ITR6MAT_P_L_PAT",is_int=True)

                if itr6mat_p_l_pat != 0 and itr6mat_p_l_pat != None:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["remark"] = "As per section 115JB assessee is not liable to compute MAT, if opting for tax regime under section 115BAA or 115BAB"
                    copy_error["field_value"] = itr6mat_p_l_pat
                    copy_error["name_range"] = "ITR6MAT_P_L_PAT"
                    copy_error["error_code"] = "490"
                    error_list.append(copy_error)
        except Exception:
            pass

    @staticmethod
    def rule_215(payload, error_list,workbook):
        '''
        Summery Line
        Value of ITR6PGBP_Oth_Addn_28_44DA should be greater than ITR6OI_Amt_Not_Cr_Tot
        In Schedule BP, Sl No 23 should be minimum of sum of amounts entered at Sl No 5a to 5d of Part A OI
        '''
        try:
            itr6pgbp_oth_addn_28_44da = BusinessValidation.get_name_range_data(workbook,"ITR6PGBP_Oth_Addn_28_44DA",is_int=True)
            itr6oi_amt_not_cr_tot = BusinessValidation.get_name_range_data(workbook,"ITR6OI_Amt_Not_Cr_Tot",is_int=True)
            if itr6pgbp_oth_addn_28_44da < itr6oi_amt_not_cr_tot :
                error_dict = {
                    "remark": "In Schedule BP, Sl No 23 should be minimum of sum of amounts entered at Sl No 5a to 5d of Part A OI",
                    "validation_status": "Error",
                    "field_value": itr6pgbp_oth_addn_28_44da,
                    "field_name": f"",
                    "error_code": "215",
                    "name_range": "ITR6PGBP_Oth_Addn_28_44DA"
                }
                error_list.append(error_dict)
        except Exception:
            pass


    @staticmethod
    def rule_591(payload, error_list,workbook):
        '''
        Summery Line
        Value of ITR6PGBP_Oth_Exmpt_Tot cannot be less than ITR6EI_Amt_Tot 
        '''
        error_dict = {
                        "remark": "In Schedule TDS (As per Form 16A/16B/16C/16D)/TCS, year of tax deduction cannot\
                             be '0' / 'null' if there is a claim brought forward of TDS",
                        "field_name": f"",
                        "validation_status": "Error",
                        "field_value": f"",
                        "error_code": "591",
                        "name_range": ""
                    }
        try:
            val_1 = BusinessValidation.find_value_f_range("ITR6TDS_B_Amt_Bf",["G6"],workbook)
            val_2 = BusinessValidation.find_value_f_range("ITR6TDS_B_FY_Col",["F6"],workbook)
            if val_1[0] != None and val_1[0] != "":
                if val_2[0] == None and val_2[0] == "":
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_value"] = val_1[0]
                    copy_error["name_range"] = "ITR6TDS_B_Amt_Bf"
                    error_list.append(copy_error)

            val_3 = BusinessValidation.find_value_f_range("ITR6TDS_A_Amt_Bf",["G7"],workbook)
            val_4 = BusinessValidation.find_value_f_range("ITR6TDS_A_FY_Ded",["F7"],workbook)
            if val_3[0] != None and val_3[0] != "":
                if val_4[0] == None and val_4[0] == "":
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_value"] = val_3[0]
                    copy_error["name_range"] = "ITR6TDS_A_Amt_Bf"
                    error_list.append(copy_error)

            val_5 = BusinessValidation.find_value_f_range("ITR6TDS_A2_Amt_Bf",["G8"],workbook)
            val_6 = BusinessValidation.find_value_f_range("ITR6TDS_A2_FY_Ded",["F8"],workbook)
            if val_5[0] != None and val_5[0] != "":
                if val_6[0] == None and val_6[0] == "":
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_value"] = val_5[0]
                    copy_error["name_range"] = "ITR6TDS_A2_Amt_Bf"
                    error_list.append(copy_error)
                          
        except Exception:
            pass

    @staticmethod
    def rule_641(payload, error_list):
        '''
        Summery Line
            If ITR6PB_PGBP_Tot is greater than zero, then ITR6_80GGA_Elg_Amt_Tot should be equal to zero
            ITR.ITR6.PartB-TI.ProfBusGain.TotProfBusGain
            ITR.ITR6.Schedule80GGA.TotalEligibleDonationAmt80GGA
        '''
        
        try:
            if payload["ITR"]["ITR6"]["PartB-TI"]["ProfBusGain"]["TotProfBusGain"] > 0 :
                if payload["ITR"]["ITR6"]["Schedule80GGA"]["TotalEligibleDonationAmt80GGA"] != 0 :
                    error_dict = {
                    "remark": "Deduciton u/s 80GGA is only allowed to assessee having no Business Income",
                    "field_name": "ITR.ITR6.PartB-TI.ProfBusGain.TotProfBusGain",
                    "validation_status": "Error",
                    "field_value": payload["ITR"]["ITR6"]["PartB-TI"]["ProfBusGain"]["TotProfBusGain"],
                    "error_code": "641",
                    "name_range": "ITR6_80GGA_Elg_Amt_Tot"
                    }
                    error_list.append(error_dict)                
        except Exception:
            pass

    @staticmethod
    def rule_642(payload, error_list):
        '''
        Summery Line
            "If deduction u/s 80M has to be claimed, then date of distribution of dividend under ITR680M_Table cannot be after
            “one month prior to the date for furnishing the return of income
            under sub-section (1) of section 139”"
        '''
        error_dict = {
                    "remark": "If deduction u/s 80M has to be claimed, then date of distribution of dividend under ITR680M_Table cannot be after “one month prior to the date for furnishing the return of income under sub-section (1) of section 139”",
                    "field_name": f"",
                    "validation_status": "Error",
                    "field_value": f"",
                    "error_code": "642",
                    "name_range": ""
                }
        try:
            if payload["ITR"]["ITR6"]["ScheduleVIA"]["UsrDeductUndChapVIA"]:
                if "Section80MDtls" in payload["ITR"]["ITR6"]["ScheduleVIA"]["UsrDeductUndChapVIA"]:
                    for _ in payload["ITR"]["ITR6"]["ScheduleVIA"]["UsrDeductUndChapVIA"]["Section80MDtls"]:
                        if "Section80MDate" in _:
                            if datetime.datetime.strptime(_.get("Section80MDate"), "%d/%m/%Y") > datetime.datetime.now() + relativedelta(months=-1):
                                copy_error = copy.deepcopy(error_dict)
                                copy_error["name_range"] = "ITR680M_Table"
                                copy_error["field_value"] = _.get("Section80MDate")
                                error_list.append(copy_error)    
        except Exception:
            pass

    @staticmethod
    def rule_648(payload, error_list, workbook):
        try:
            error_dict = {
                "remark": "",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "",
                "name_range": ""
            }

            def perform_check(index, error_code):
                name_range_key = f"ITR6OS_Qtr_breakup_check_{index}"
                val = BusinessValidation.get_name_range_data(workbook, name_range_key, is_int=True)

                if val != 0:
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["remark"] = "In Schedule OS, Sl. No. 10 ,Break up of Income by way of Winnings from online games"\
                "should be equal to Sl. No. 2Aii Income by way of winnings from online games." if error_code == "375" else f"In Schedule OS: Quarterly break is matching with the amount of income reported Sl No. {index}"
                    copy_error["name_range"] = name_range_key
                    copy_error["field_value"] = val
                    copy_error["error_code"] = error_code
                    error_list.append(copy_error)

            perform_check(1, "376")
            perform_check(2, "375")
            perform_check(3, "650")
            perform_check(4, "651")
            perform_check(5, "652")
            perform_check(6, "653")
            perform_check(7, "649")
            perform_check(8, "648")

        except Exception:
            pass



    @staticmethod
    def rule_2024_5(payload, error_list):
        '''
        Summery Line
        IN DUE DATE FOR FILING OF RETURN FIELD, DUE DATE CANNOT BE LEFT BLANK. PLEASE SELECT THE 
        APPROPRIATE DUE DATE OF FILING FROM THE DROP DOWN AS APPLICABLE.
        '''
        

        try:
            if not payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("ItrFilingDueDate"):
                error_dict = {
                                "remark": "Due Date for filing of Return is required. Please select the appropriate due date of filing from the drop down as applicable.",
                                "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.ItrFilingDueDate",
                                "validation_status": "Error",
                                "field_value": f"",
                                "error_code": "2024_5",
                                "name_range": "ITR6PAG1_Due_Date_for_filing_ROI"
                }
                error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_2024_6(payload, error_list):
        '''
        Summery Line
            "IF THE TAX PAYER IS LIABLE FOR AUDIT UNDER SECTION 44AB, , THEN CONDITION BY VIRTUE OF WHICH 
            THE TAX PAYER IS LIABLE AT BI, BII, BIII OR BIV IS REQUIRED TO BE SELECTED."
        '''
        error_dict = {
            "remark": "If the Tax Payer is liable for audit u/s 44AB, , Then condition by virtue of which" \
                        "the Tax Payer is Liable at Bi, Bii, Biii or Biv is required to be selected",
            "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.Cndnfor44AB",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_6",
            "name_range": "ITR6PAG1_Cndnfor44AB"
        }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]["LiableSec44ABflg"] == "Y":
                if not payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Cndnfor44AB"):
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_24(payload, error_list):
        '''
        Summery Line
            "IN PART A GENERAL , SL. NO. R - "LEGAL ENTITY IDENTIFIER (LEI) DETAILS" IS MANDATORY IF 
            AMOUNT IN PART B-TTI AT SL. NO. 12 'REFUND' IS 50 CRORES OR MORE"
        '''
        error_dict = {
            "remark": "Please enter Legal Entity Identifier (LEI) Details.",
            "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.Cndnfor44AB",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_24",
            "name_range": "ITR6PAG1_LEI_Number_ValidUpto"
        }
        try:
            if payload["ITR"]["ITR6"]["PartB_TTI"]["Refund"] and payload["ITR"]["ITR6"]["PartB_TTI"]["Refund"]["RefundDue"]:
                if payload["ITR"]["ITR6"]["PartB_TTI"]["Refund"]["RefundDue"] >= 500000000: #type validate first and node validate
                    lei_fields = [
                        ("LEINumber", "ITR6PAG1_LEI_Number"),
                        ("ValidUptoDate", "ITR6PAG1_LEI_Number_ValidUpto"),
                    ]
            filing_status = payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]
            leidtls = filing_status.get("LEIDtls", {})
               
            for field, name_range in lei_fields:
                if not leidtls.get(field):
                # if not payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["LEIDtls"].get(field):
                    copy_error = copy.deepcopy(error_dict)
                    copy_error["field_name"] = f"ITR.ITR6.PartA_GEN1.FilingStatus.LEIDtls.{field}"
                    copy_error["name_range"] = name_range
                    error_list.append(copy_error)
        except Exception:
            pass
        
    @staticmethod
    def rule_2024_25(payload, error_list):
        '''
        Summery Line
            "TAXPAYER HAS TO SELECT EITHER OF "YES'' OR "NO" IN THE QUESTION "WHETHER YOU ARE RECOGNIZED AS MSME ?""
        '''
        error_dict = {
            "remark": "Please select option at field 'Whether you are recognized as MSME ?'",
            "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.ifMSME",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_25",
            "name_range": "ITR6PAG1_MSME_Recoginsed"
        }
        try:
            if not payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("ifMSME"):
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_26(payload, error_list):
        '''
        Summery Line
            "TAXPAYER HAS SELECTED "YES" IN THE QUESTION " WHETHER YOU ARE RECOGNIZED AS MSME?" 
            THEN DETAILS OF REGISTRATION ARE MANDATORY TO BE FILLED UP"
        '''
        error_dict = {
            "remark": "Please provide registration number allotted as per the MSMED Act, 2006.",
            "field_name": "ITR.ITR6.PartA_GEN1.FilingStatus.RegNumMSMEDAct2006",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_26",
            "name_range": "ITR6PAG1_MSME_RegistNumber"
        }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("ifMSME") == "Y":
                if payload["ITR"]["ITR6"]["PartA_GEN1"] and payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]:
                    if not payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("RegNumMSMEDAct2006"):
                        error_list.append(error_dict)
        except Exception:
            pass
      
    @staticmethod
    def rule_2024_27(payload, error_list):
        '''
        Summery Line
            "IN PART A GENERAL, WHETHER LIABLE FOR AUDIT UNDER SECTION 44AB? IS YES, ACKNOWLEDGEMENT 
            NUMBER IS MANDATORY TO BE FILLED UP."
        '''
        error_dict = {
            "remark": "Please provide Acknowledgement Number of the Audit Report u/s 44AB",
            "field_name": "ITR.ITR6.PartA_GEN2For6.AuditInfo.AckNum44AB",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_27",
            "name_range": "ITR6PAG1_AckNum44AB"
        }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                if payload["ITR"]["ITR6"]["PartA_GEN2For6"].get("LiableSec44ABflg") == "Y":
                    if "AuditInfo" not in payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                        error_list.append(error_dict)
                    else:
                        if not payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditInfo"].get("AckNum44AB"):
                            error_list.append(error_dict)
        except Exception:
            pass
      
    @staticmethod
    def rule_2024_30(payload, error_list):
        '''
        Summery Line
            "IN PART A GENERAL, WHETHER LIABLE FOR AUDIT UNDER SECTION 44AB? IS YES, ACKNOWLEDGEMENT 
            NUMBER IS MANDATORY TO BE FILLED UP."
        '''
        error_dict = {
            "remark": "Please enter acknowledgement number in other audit report table.",
            "field_name": "ITR.ITR6.PartA_GEN2For6.AuditInfo.AckNum44AB",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_30",
            "name_range": "ITR6PAG1_Other_Income_Tax_Audit_Table"
        }
        try:
            if "PartA_GEN2For6" in payload["ITR"]["ITR6"] and "AuditDetails" in payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                for val in payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditDetails"]:
                    if "AuditedSection" in val or "AnyOtherSection" in val or "AuditFlag" in val or "DateOfAudit" in val:
                        if "AckNumOth" not in val:
                            error_list.append(error_dict)
        except Exception:
            pass
            
    @staticmethod
    def rule_2024_28(payload, error_list):
        '''
        Summery Line
            "IN PART A GENERAL, WHETHER LIABLE FOR AUDIT UNDER SECTION 44AB? IS YES, 
            UDIN IS MANDATORY TO BE FILLED UP."
        '''
        error_dict = {
            "remark": "Please provide UDIN under Part-A General Information.",
            "field_name": "ITR.ITR6.PartA_GEN2For6.AuditInfo.UDIN",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_28",
            "name_range": "ITR6PAG1_UDIN"
        }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                if payload["ITR"]["ITR6"]["PartA_GEN2For6"].get("LiableSec44ABflg") == "Y":
                    if "AuditInfo" not in payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                        error_list.append(error_dict)
                    else:
                        if not payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditInfo"].get("UDIN"):
                            error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_29(payload, error_list):
        '''
        Summery Line
            "Please provide Acknowledgement Number of the Audit Report u/s 92E."
        '''
        error_dict = {
            "remark": "Please provide Acknowledgement Number of the Audit Report u/s 92E.",
            "field_name": "ITR.ITR6.PartA_GEN2For6.AuditInfo.UDIN",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_29",
            "name_range": "ITR6PAG1_Liab_TP_Audit"
        }
        try:
            # ITR.ITR6.PartA_GEN2For6.LiableSec92Eflg
            # ITR.ITR6.PartA_GEN2For6.AuditDetails92E.AckNum92E
            if payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                if payload["ITR"]["ITR6"]["PartA_GEN2For6"].get("LiableSec92Eflg") == "Y":
                    if "AuditDetails92E" not in payload["ITR"]["ITR6"]["PartA_GEN2For6"]:
                        error_list.append(error_dict)
                    else:
                        if not payload["ITR"]["ITR6"]["PartA_GEN2For6"]["AuditDetails92E"].get("AckNum92E"):
                            error_list.append(error_dict)
        except Exception:
            pass
    
    @staticmethod
    def rule_2024_426(payload, error_list):
        '''
        Summery Line
            "IN SCHEDULE OS, SL. NO. 10 THE QUARTERLY BREAK UP OF INCOME BY WAY OF WINNINGS FROM ONLINE 
            GAMES CHARGEABLE U/S 115BBJ SHOULD BE EQUAL TO SL. NO. 2AII INCOME BY WAY OF WINNINGS FROM 
            ONLINE GAMES CHARGEABLE U/S 115BBJ"
        '''
        error_dict = {
            "remark": "In Schedule OS, Sl. No. 10 ,Break up of Income by way of Winnings from online games"\
                "should be equal to Sl. No. 2Aii Income by way of winnings from online games.",
            "field_name": "ITR.ITR6.PartA_GEN2For6.AuditInfo.UDIN",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_426",
            "name_range": "ITR6OS_OnlineGames"
        }
        try:
            # payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"]["IncChrgblUs115BBJ"]
            # payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"]["DateRange"]["Upto15Of6"]
            if payload["ITR"]["ITR6"]["ScheduleOS"] and payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"]:
                total_game = payload["ITR"]["ITR6"]["ScheduleOS"]["IncOthThanOwnRaceHorse"].get("IncChrgblUs115BBJ")
                
                try:
                    if total_game and payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"] and payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"]["DateRange"]:
                        game_156 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"]["DateRange"].get("Upto15Of6", 0)
                        game_159 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"]["DateRange"].get("Up16Of6To15Of9", 0)
                        game_1512 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"]["DateRange"].get("Up16Of9To15Of12", 0)
                        game_153 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"]["DateRange"].get("Up16Of12To15Of3", 0)
                        game_313 = payload["ITR"]["ITR6"]["ScheduleOS"]["IncFrmOnGames"]["DateRange"].get("Up16Of3To31Of3", 0)

                        if total_game != game_156 + game_159 + game_1512 + game_153 + game_313:
                            error_list.append(error_dict)
                except Exception:
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_524(payload, error_list):
        '''
        Summery Line
            "IN PART A GENERAL, "115BAB/ 115BA" IS SELECTED FOR THE QUESTION "HAVE YOU OPTED FOR TAXATION 
            UNDER SECTION 115BA/115BAA/115BAB" OR 115BAB/ 115BA IS SELECTED FOR THE QUESTION "IF NO, WHETHER 
            YOU ARE CHOOSING TO OPT FOR TAXATION UNDER SECTION 115BA/115BAA/115BAB THIS YEAR?" THEN SCHEDULE 
            80GGC IS NOT TO BE FILLED."
        '''
        error_dict = {
            "remark": "Deduction u/s 80GGC can't be claimed Since '115BA/115BAB' is selected at 'Part A General'",
            "field_name": "ITR.ITR6.Schedule80GGC.TotalEligibleDonationAmt80GGC",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_524",
            "name_range": "ITR680GGC_EligibleContribution_Tot"
        }
        try:
            if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]:
                if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115BA") == "115BA" \
                    or payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("Section115BA") == "115BAB"\
                    or payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") == "115BA"\
                    or payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"].get("SectionCurrAY") == "115BAB":
                    try:
                        if payload["ITR"]["ITR6"]["Schedule80GGC"].get("TotalEligibleDonationAmt80GGC") != 0:
                            error_list.append(error_dict)
                    except Exception:
                        error_list.append(error_dict)

        except Exception:
            pass
        

    @staticmethod
    def rule_2024_530(payload, error_list):
        '''
        Summery Line
            "IF GROSS TOTAL INCOME IN PART B TI IS ZERO, SL. NO. D "ELIGIBLE AMOUNT OF CONTRIBUTION" 
            CANNOT BE MORE THAN 0"

            in gross "GrossTotalIncome" is 0 but "TotalEligibleDonationAmt80GGC" not present, in this case error should not populate.
        '''
        error_dict = {
            "remark": "Deducton u/s 80GGC cannot be claimed since Gross Total Income In Part B TI is Zero.",
            "field_name": "ITR.ITR6.Schedule80GGC.TotalEligibleDonationAmt80GGC",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_530",
            "name_range": "ITR680GGC_EligibleContribution_Tot"
        }
        try:
            if payload["ITR"]["ITR6"]["PartB-TI"]:
                if payload["ITR"]["ITR6"]["PartB-TI"].get("GrossTotalIncome") == 0:
                    try:
                        if payload["ITR"]["ITR6"]["Schedule80GGC"]["TotalEligibleDonationAmt80GGC"]:
                            if payload["ITR"]["ITR6"]["Schedule80GGC"].get("TotalEligibleDonationAmt80GGC") != 0:
                                error_list.append(error_dict)
                    except Exception:
                        pass
                        # error_list.append(error_dict)

        except Exception:
            pass
    

    @staticmethod
    def rule_2024_531(payload, error_list):
        '''
        Summery Line
            "IF DEDUCTION UNDER SECTION 80GGC CLAIMED IN SL. NO (A) OF SCH VI A THEN ITS MANDATORY TO FILL 
            DETAILS IN SCHEDULE 80GGC"
        '''
        error_dict = {
            "remark": "Please fill details in schedule 80GGC.",
            "field_name": "ITR.ITR6.Schedule80GGC.TotalEligibleDonationAmt80GGC",
            "validation_status": "Error",
            "field_value": "",
            "error_code": "2024_530",
            "name_range": "ITR680GGC_Table"
        }
        try:
            if payload["ITR"]["ITR6"]["ScheduleVIA"]["UsrDeductUndChapVIA"]:
                if payload["ITR"]["ITR6"]["ScheduleVIA"]["UsrDeductUndChapVIA"].get("Section80GGC") > 0:
                    try:
                        if not payload["ITR"]["ITR6"]["Schedule80GGC"].get("Schedule80GGCDetails"):
                            error_list.append(error_dict)
                    except Exception:
                        error_list.append(error_dict)

        except Exception:
            pass
    

    @staticmethod
    def rule_2024_532(payload,error_list):
        '''
        Summery Line
        """If value at ITR680IAC_AmtDedCurAY > """"0"""",
        Then below fields are mandatory
        ITR680IAC_DateIncrpStrup
        ITR680IAC_NatureOfBusiness
        ITR680IAC_InterMnstBoardCertNum
        ITR680IAC_FstAYDeduction"
        '''
        try:
            error_dict = {
                "remark": "Please fill all the details in Schedule-80IAC.",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "532",
                "name_range": ""
            }
            if "Schedule80IAC" in payload["ITR"]["ITR6"] in "AmtDedCurAY" in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                if payload["ITR"]["ITR6"]["Schedule80IAC"]["AmtDedCurAY"] > 0:
                    if "DateIncrpStrup" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_AmtDedCurAY"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.DateIncrpStrup"
                        error_list.append(error_dict)
                    if "NatureOfBusiness" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_AmtDedCurAY"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.NatureOfBusiness"
                        error_list.append(error_dict)
                    if "InterMnstBoardCertNum" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_AmtDedCurAY"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.InterMnstBoardCertNum"
                        error_list.append(error_dict)
                    if "FstAYDeduction" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_AmtDedCurAY"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.FstAYDeduction"
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_533(payload,error_list):
        '''
        Summery Line
        "If value at ITR6PAG1_date_Inc < ""31st March 2016"",
        Then below fields should be Blank

        ITR680IAC_DateIncrpStrup
        ITR680IAC_NatureOfBusiness
        ITR680IAC_InterMnstBoardCertNum
        ITR680IAC_FstAYDeduction
        ITR680IAC_AmtDedCurAY
        '''
        try:
            error_dict = {
                "remark": "Deducton u/s 80IAC cannot be claimed since Date of Incorporation is before 1st April 2016.",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "533",
                "name_range": ""
            }
            if "OrgFirmInfo" in payload["ITR"]["ITR6"]["PartA_GEN1"] and "DateOFFormOrIncorp" in payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]:
                if payload["ITR"]["ITR6"]["PartA_GEN1"]["OrgFirmInfo"]["DateOFFormOrIncorp"] < "2016-03-31":
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["DateIncrpStrup"]:
                        error_dict["name_range"] = "ITR6PAG1_date_Inc"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.DateIncrpStrup"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["DateIncrpStrup"]
                        error_list.append(error_dict)
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["NatureOfBusiness"]:
                        error_dict["name_range"] = "ITR6PAG1_date_Inc"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.NatureOfBusiness"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["NatureOfBusiness"]
                        error_list.append(error_dict)
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["InterMnstBoardCertNum"]:
                        error_dict["name_range"] = "ITR6PAG1_date_Inc"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.InterMnstBoardCertNum"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["InterMnstBoardCertNum"]
                        error_list.append(error_dict)
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["FstAYDeduction"]:
                        error_dict["name_range"] = "ITR6PAG1_date_Inc"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.FstAYDeduction"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["FstAYDeduction"]
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_534(payload,error_list):
        '''
        Summery Line
        "If value at ITR6PAG1_If_start_up = ""No"",

        Then below fields should be Blank

        ITR680IAC_DateIncrpStrup
        ITR680IAC_NatureOfBusiness
        ITR680IAC_InterMnstBoardCertNum
        ITR680IAC_FstAYDeduction
        ITR680IAC_AmtDedCurAY
        '''
        try:
            error_dict = {
                "remark": 'Deducton u/s 80IAC cannot be claimed since "No" has been selected at the field "Whether you are recognized as start up by DPIIT" In Part A General.',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "534",
                "name_range": ""
            }
            if "FilingStatus" in payload["ITR"]["ITR6"]["PartA_GEN1"] and "StartUpDPIITFlag" in payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]:
                if payload["ITR"]["ITR6"]["PartA_GEN1"]["FilingStatus"]["StartUpDPIITFlag"] == "N":
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["DateIncrpStrup"]:
                        error_dict["name_range"] = "ITR6PAG1_If_start_up"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.DateIncrpStrup"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["DateIncrpStrup"]
                        error_list.append(error_dict)
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["NatureOfBusiness"]:
                        error_dict["name_range"] = "ITR6PAG1_If_start_up"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.NatureOfBusiness"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["NatureOfBusiness"]
                        error_list.append(error_dict)
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["InterMnstBoardCertNum"]:
                        error_dict["name_range"] = "ITR6PAG1_If_start_up"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.InterMnstBoardCertNum"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["InterMnstBoardCertNum"]
                        error_list.append(error_dict)
                    if payload["ITR"]["ITR6"]["Schedule80IAC"]["FstAYDeduction"]:
                        error_dict["name_range"] = "ITR6PAG1_If_start_up"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.FstAYDeduction"
                        error_dict["field_value"] = payload["ITR"]["ITR6"]["Schedule80IAC"]["FstAYDeduction"]
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_535(payload,error_list):
        '''
        Summery Line
        "If value at ITR6ChVIA_Dedn_80IAC_SC > ""ITR680IAC_AmtDedCurAY"",
        ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80IAC
        ITR.ITR6.Schedule80IAC.AmtDedCurAY
        '''
        try:
            error_dict = {
                "remark": 'Value Claimed In 80-IAC field in schedule VIA cannot be higher than the value in schedule 80-IAC.',
                "field_name": "ITR.ITR6.ScheduleVIA.DeductUndChapVIA.Section80IAC",
                "validation_status": "Error",
                "field_value": payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]["Section80IAC"],
                "error_code": "535",
                "name_range": "ITR6ChVIA_Dedn_80IAC_SC"
            }
            if "ScheduleVIA" in payload["ITR"]["ITR6"] and "DeductUndChapVIA" in payload["ITR"]["ITR6"]["ScheduleVIA"] and "Section80IAC" in payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]:
                val_1 = payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]["Section80IAC"]
                val_2 = 0
                if "Schedule80IAC" in payload["ITR"]["ITR6"] and "AmtDedCurAY" in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                    val_2 = payload["ITR"]["ITR6"]["Schedule80IAC"]["AmtDedCurAY"]
                if val_1 > val_2:
                    error_list.append(error_dict)
                    
        except Exception:
            pass

    @staticmethod
    def rule_2024_536(payload,error_list):
        '''
        Summery Line
        "If value at ITR6ChVIA_Dedn_80IAC_SC > ""0"",

        Then below fields are mandatory
        ITR680IAC_DateIncrpStrup
        ITR680IAC_NatureOfBusiness
        ITR680IAC_InterMnstBoardCertNum
        ITR680IAC_FstAYDeduction
        ITR680IAC_AmtDedCurAY
        '''
        try:
            error_dict = {
                "remark": "Please fill all the details in Schedule-80IAC.",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "536",
                "name_range": ""
            }
            if "ScheduleVIA" in payload["ITR"]["ITR6"] and "DeductUndChapVIA" in payload["ITR"]["ITR6"]["ScheduleVIA"] \
                and "Section80IAC" in payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"] and "Section80IAC" in \
                    payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]:
                if payload["ITR"]["ITR6"]["ScheduleVIA"]["DeductUndChapVIA"]["Section80IAC"] > 0:
                    if "DateIncrpStrup" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_DateIncrpStrup"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.DateIncrpStrup"
                        error_list.append(error_dict)
                    if "NatureOfBusiness" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_NatureOfBusiness"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.NatureOfBusiness"
                        error_list.append(error_dict)
                    if "InterMnstBoardCertNum" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_InterMnstBoardCertNum"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.InterMnstBoardCertNum"
                        error_list.append(error_dict)
                    if "FstAYDeduction" not in payload["ITR"]["ITR6"]["Schedule80IAC"]:
                        error_dict["name_range"] = "ITR680IAC_FstAYDeduction"
                        error_dict["field_name"] = "ITR.ITR6.Schedule80IAC.FstAYDeduction"
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2024_613(payload,error_list):
        '''
        Summery Line
        If value at ITR6115TD_AccretedIncome > "0",

        Then below field is mandatory
        ITR6115TD_SpecifiedDate
        '''
        try:
            error_dict = {
                "remark": 'In Schedule 115TD, Please mention "Specified Date u/s 115TD"',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "613",
                "name_range": ""
            }
            if "Schedule115TD" in payload["ITR"]["ITR6"] and "AccretedIncomeSection115TD" in payload["ITR"]["ITR6"]["Schedule115TD"]:
                if payload["ITR"]["ITR6"]["Schedule115TD"]["AccretedIncomeSection115TD"] > 0:
                    if "SpecifiedDateUs115TD" not in payload["ITR"]["ITR6"]["Schedule115TD"]:
                        error_dict["name_range"] = "ITR6115TD_SpecifiedDate"
                        error_dict["field_name"] = "ITR.ITR6.Schedule115TD.SpecifiedDateUs115TD"
                        error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2025_32(payload,error_list):
        '''
        Summery Line
        If ITR6PAG1_Opt_115BA_BAA_BAB (ITR.ITR6.PartA_GEN1.FilingStatus.Section115BA) is "NA- None of above" and 
        Opt_ITR6PAG1_Opt_115BA_BAA_BAB_CY (ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY******) is "Y",

        Then ITR6PAG1_115BA_filing_date_2 (ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAYDate) and 
        ITR6PAG1_115BA_Ack_No_2 (ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAYRecNo) should not be blank
        '''
        try:
            error_dict = {
                "remark": 'Please provide the date of filing of relevant form (10-IB/10-IC/10-ID) & acknowledgment number Since "Yes" is selected at question "whether you are choosing to opt for taxation under section 115BA/115BAA/115BAB this year"?',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_32",
                "name_range": "IRL_115BA_filing_date_1_PYJ_2"
            }

            filing_status = payload["ITR"]["ITR6"].get("PartA_GEN1", {}).get("FilingStatus", {})

            Section115BA = filing_status.get("Section115BA", "")
            Section115CurrAY = filing_status.get("Section115CurrAY", "")
            Section115CurrAYDate = filing_status.get("Section115CurrAYDate", "")
            Section115CurrAYRecNo = filing_status.get("Section115CurrAYRecNo", "")

            if Section115BA == 'NA' and Section115CurrAY == 'Y':
                if not Section115CurrAYDate or not Section115CurrAYRecNo:
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2025_33(payload,error_list):
        '''
        Summery Line
        If this ITR6PAG1_Cash_recpt_ex_5perc (ITR.ITR6.PartA_GEN2For6.AgrOFAllAmtsRcvd) is "N" ,
        then ITR6PAG1_Liab_Tax_Audit (ITR.ITR6.PartA_GEN2For6.LiableSec44ABflg) should be "Y"
        '''
        try:
            error_dict = {
                "remark": 'You are liable to audit u/s 44AB, since you have selected Sl. No. a2ii as "No" in Part A General.',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_33",
                "name_range": "Liab_tax_audit_Rep"
            }

            AgrOFAllAmtsRcvd = payload["ITR"]["ITR6"].get("PartA_GEN2For6", {}).get("AgrOFAllAmtsRcvd", "")
            LiableSec44ABflg = payload["ITR"]["ITR6"].get("PartA_GEN2For6", {}).get("LiableSec44ABflg", "")

            if AgrOFAllAmtsRcvd == 'N' and LiableSec44ABflg != 'Y':
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2025_34(payload,error_list):
        '''
        Summery Line
        If this ITR6PAG1_Cash_pay_ex_5perc (ITR.ITR6.PartA_GEN2For6.AgrOFAllPayMade) is "N",
        then ITR6PAG1_Liab_Tax_Audit (ITR.ITR6.PartA_GEN2For6.LiableSec44ABflg) should be "Y"
        '''
        try:
            error_dict = {
                "remark": 'You are liable to audit u/s 44AB, since you have selected Sl. No. a2iii as "No" in Part A General.',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_34",
                "name_range": "Liab_tax_audit_Rep"
            }

            AgrOFAllPayMade = payload["ITR"]["ITR6"].get("PartA_GEN2For6", {}).get("AgrOFAllPayMade", "")
            LiableSec44ABflg = payload["ITR"]["ITR6"].get("PartA_GEN2For6", {}).get("LiableSec44ABflg", "")

            if AgrOFAllPayMade == 'N' and LiableSec44ABflg != 'Y':
                error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2025_35(payload,error_list):
        '''
        Summery Line
        "If this ITR6PAG1_Sal_1_10_Cr (ITR.ITR6.PartA_GEN2For6.TotalSalesExcOneCr) is ""Y"" and
        ITR6PAG1_Cash_recpt_ex_5perc (ITR.ITR6.PartA_GEN2For6.AgrOFAllAmtsRcvd) is ""N"" OR   
        ITR6PAG1_Cash_pay_ex_5perc (ITR.ITR6.PartA_GEN2For6.AgrOFAllPayMade) is ""N"" ",

        then ITR6PAG1_Liab_Tax_Audit (ITR.ITR6.PartA_GEN2For6.LiableSec44ABflg) should be "Y"
        '''
        try:
            error_dict = {
                "remark": 'Since you have selected a2i as "Yes" and either of a2ii or a2iii "No" in Part A General, then you are liable to audit u/s 44AB.',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_35",
                "name_range": "Liab_tax_audit_Rep"
            }

            parta_gen2for6 = payload["ITR"]["ITR6"].get("PartA_GEN2For6", {})

            total_sales_exc_1cr = parta_gen2for6.get("TotalSalesExcOneCr", "")
            cash_receipts_flag = parta_gen2for6.get("AgrOFAllAmtsRcvd", "")
            cash_payments_flag = parta_gen2for6.get("AgrOFAllPayMade", "")
            liable_tax_audit = parta_gen2for6.get("LiableSec44ABflg", "")

            if total_sales_exc_1cr == "Y" and (cash_receipts_flag == "N" or cash_payments_flag == "N"):
                if liable_tax_audit != "Y":
                    error_list.append(error_dict)
        except Exception:
            pass

    @staticmethod
    def rule_2025_262(payload,error_list):
        '''
        Summery Line
        ITR6DPM_Depn_15_PropAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate15.DepreciationDetail.ProportionateAggDepreciation)
         > ITR6DPM_Depn_15_NetAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate15.DepreciationDetail.NetAggregateDepreciation) then display error message 
        '''
        try:
            error_dict = {
                "remark": "Schedule DPM, value at Sl. No. 18 cannot be more than value at Sl. No. 17 in 15% block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_262",
                "name_range": "Annexure_3CD_DEP_PM_IT_Act_FV_Table"
            }

            dep_detail = (payload["ITR"]["ITR6"].get("ScheduleDPM", {}).get("PlantMachinery", {}).get("Rate15", {}).get("DepreciationDetail", {}))

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # ensure numeric comparison (sometimes JSON fields come as strings)
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass     
    
    @staticmethod
    def rule_2025_263(payload,error_list):
        '''
        Summery Line 
        ITR6DPM_Depn_30_PropAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate30.DepreciationDetail.ProportionateAggDepreciation)
        > ITR6DPM_Depn_30_NetAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate30.DepreciationDetail.NetAggregateDepreciation) then display error message
        '''
        try:
            error_dict = {
                "remark": "Schedule DPM, value at Sl. No. 18 cannot be more than value at Sl. No. 17 in 30% block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_263",
                "name_range": "Annexure_3CD_DEP_PM_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDPM", {})
                .get("PlantMachinery", {})
                .get("Rate30", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert to numeric safely
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_264(payload,error_list):
        '''
        Summery Line 
        ITR6DPM_Depn_40_PropAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate40.DepreciationDetail.ProportionateAggDepreciation) 
        > ITR6DPM_Depn_40_NetAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate40.DepreciationDetail.NetAggregateDepreciation) then display error message
        '''
        try:
            error_dict = {
                "remark": "Schedule DPM, value at Sl. No. 18 cannot be more than value at Sl. No. 17 in 40% block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_264",
                "name_range": "Annexure_3CD_DEP_PM_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDPM", {})
                .get("PlantMachinery", {})
                .get("Rate40", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert to numeric safely
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_265(payload,error_list):
        '''
        Summery Line 
        ITR6DPM_Depn_45_PropAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate45.DepreciationDetail.ProportionateAggDepreciation)
        > ITR6DPM_Depn_45_NetAgg (ITR.ITR6.ScheduleDPM.PlantMachinery.Rate45.DepreciationDetail.NetAggregateDepreciation) then display error message
        '''
        try:
            error_dict = {
                "remark": "Schedule DPM, value at Sl. No. 18 cannot be more than value at Sl. No. 17 in 45% block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_265",
                "name_range": "Annexure_3CD_DEP_PM_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDPM", {})
                .get("PlantMachinery", {})
                .get("Rate45", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert safely to numbers
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_274(payload,error_list):
        '''
        Summery Line 
        ITR6DOA_Depn_5_PropAgg (ITR.ITR6.ScheduleDOA.Building.Rate5.DepreciationDetail.ProportionateAggDepreciation) 
        > ITR6DOA_Depn_5_NetAgg (ITR.ITR6.ScheduleDOA.Building.Rate5.DepreciationDetail.NetAggregateDepreciation) then display error message
        '''
        try:
            error_dict = {
                "remark": "Schedule DOA, value at Sl. No. 15 cannot be more than value at Sl. No. 14 in 5% building block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_274",
                "name_range": "Annexure_3CD_DEP_Building_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDOA", {})
                .get("Building", {})
                .get("Rate5", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert safely to numbers
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_275(payload,error_list):
        '''
        Summery Line 
        ITR6DOA_Depn_10_PropAgg (ITR.ITR6.ScheduleDOA.Building.Rate10.DepreciationDetail.ProportionateAggDepreciation)
        > ITR6DOA_Depn_10_NetAgg (ITR.ITR6.ScheduleDOA.Building.Rate10.DepreciationDetail.NetAggregateDepreciation) then display error message
        '''
        try:
            error_dict = {
                "remark": "Schedule DOA, value at Sl. No. 15 cannot be more than value at Sl. No. 14 in 10% building block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_275",
                "name_range": "Annexure_3CD_DEP_Building_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDOA", {})
                .get("Building", {})
                .get("Rate10", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert safely to numbers
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_276(payload,error_list):
        '''
        Summery Line 
        ITR6DOA_Depn_40_PropAgg (ITR.ITR6.ScheduleDOA.Building.Rate40.DepreciationDetail.ProportionateAggDepreciation) 
        > ITR6DOA_Depn_40_NetAgg (ITR.ITR6.ScheduleDOA.Building.Rate40.DepreciationDetail.NetAggregateDepreciation) then display error message
        '''
        try:
            error_dict = {
                "remark": "Schedule DOA, value at Sl. No. 15 cannot be more than value at Sl. No. 14 in 40% building block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_276",
                "name_range": "Annexure_3CD_DEP_Building_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDOA", {})
                .get("Building", {})
                .get("Rate40", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert safely to numbers
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_277(payload,error_list):
        '''
        Summery Line 
        ITR6DOA_Depn_10F_PropAgg (ITR.ITR6.ScheduleDOA.FurnitureFittings.Rate10.DepreciationDetail.ProportionateAggDepreciation) 
        > ITR6DOA_Depn_10F_NetAgg (ITR.ITR6.ScheduleDOA.FurnitureFittings.Rate10.DepreciationDetail.NetAggregateDepreciation) then display error message
        '''
        try:
            error_dict = {
                "remark": "Schedule DOA, value at Sl. No. 15 cannot be more than value at Sl. No. 14 in 10% Furniture and Fitting block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_277",
                "name_range": "Annexure_3CD_DEP_FF_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDOA", {})
                .get("FurnitureFittings", {})
                .get("Rate10", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert safely to numbers
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_278(payload,error_list):
        '''
        Summery Line 
        ITR6DOA_Depn_25_PropAgg (ITR.ITR6.ScheduleDOA.IntangibleAssets.Rate25.DepreciationDetail.ProportionateAggDepreciation) 
        > ITR6DOA_Depn_25_NetAgg (ITR.ITR6.ScheduleDOA.IntangibleAssets.Rate25.DepreciationDetail.NetAggregateDepreciation) then display error message 
        '''
        try:
            error_dict = {
                "remark": "Schedule DOA, value at Sl. No. 15 cannot be more than value at Sl. No. 14 in 25% Intangible assets block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_278",
                "name_range": "Annexure_3CD_DEP_IAssets_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDOA", {})
                .get("IntangibleAssets", {})
                .get("Rate25", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert safely to numbers
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_279(payload,error_list):
        '''
        Summery Line 
        "ITR6DOA_Depn_20_PropAgg (ITR.ITR6.ScheduleDOA.Ships.Rate20.DepreciationDetail.ProportionateAggDepreciation)
        > ITR6DOA_Depn_20_NetAgg (ITR.ITR6.ScheduleDOA.Ships.Rate20.DepreciationDetail.NetAggregateDepreciation) then display error message"
        '''
        try:
            error_dict = {
                "remark": "Schedule DOA, value at Sl. No. 15 cannot be more than value at Sl. No. 14 in 20% Ships block",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_279",
                "name_range": "Annexure_3CD_DEP_Ships_IT_Act_FV_Table"
            }

            dep_detail = (
                payload["ITR"]["ITR6"]
                .get("ScheduleDOA", {})
                .get("Ships", {})
                .get("Rate20", {})
                .get("DepreciationDetail", {})
            )

            prop_agg = dep_detail.get("ProportionateAggDepreciation", 0)
            net_agg = dep_detail.get("NetAggregateDepreciation", 0)

            # Convert safely to numbers
            try:
                prop_agg = float(prop_agg)
            except Exception:
                prop_agg = 0

            try:
                net_agg = float(net_agg)
            except Exception:
                net_agg = 0

            if prop_agg > net_agg:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_539(payload,error_list):
        '''
        Summery Line 
        ITR6OS_Int_Exp_Elg (ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.Deductions.IntExp57) >20%  of Sum 
        (ITR6OS_Gr_Div_Oth (ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.DividendOthThan22e)
        + ITR6OS_Gr_Div_2_22e (ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.Dividend22e)), then display error message
        '''
        try:
            error_dict = {
                "remark": "Interest expenditure u/s 57(1) should not be more than 20% of the dividend income at Sl. No. 1ai + Sl. No. 1aii in Schedule OS.",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_539",
                "name_range": "IFOS_Int_Exp_Claim"
            }

            inc_other = (
            payload["ITR"]["ITR6"]
            .get("ScheduleOS", {})
            .get("IncOthThanOwnRaceHorse", {})
        )

            int_exp_57 = inc_other.get("Deductions", {}).get("IntExp57", 0)
            div_other = inc_other.get("DividendOthThan22e", 0)
            div_22e = inc_other.get("Dividend22e", 0)

            # Ensure numeric conversion
            try:
                int_exp_57 = float(int_exp_57)
            except Exception:
                int_exp_57 = 0

            try:
                div_other = float(div_other)
            except Exception:
                div_other = 0

            try:
                div_22e = float(div_22e)
            except Exception:
                div_22e = 0

            total_div = div_other + div_22e
            threshold = 0.20 * total_div

            if int_exp_57 > threshold:
                error_list.append(error_dict)

        except Exception:
            pass     

    @staticmethod
    def rule_2025_382(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_S15_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder15Per.DateRange.Upto15Of6)
        + (ITR6CG_S15_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder15Per.DateRange.Up16Of6To15Of9) 
        + (ITR6CG_S15_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder15Per.DateRange.Up16Of9To15Of12)
         +(ITR6CG_S15_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder15Per.DateRange.Up16Of12To15Of3)
         +(ITR6CG_S15_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder15Per.DateRange.Up16Of3To31Of3) 
         should be equal to ITR6BFLA_STCG_15_Col_5 (ITR.ITR6.ScheduleBFLA.STCG15Per.IncBFLA.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 1 the breakup of all the quarters should be equal to the value from item 5via of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_382",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            stcg_15 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleCG", {})
                .get("AccruOrRecOfCG", {})
                .get("ShortTermUnder15Per", {})
                .get("DateRange", {})
            )

            bfl_stcg_15 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleBFLA", {})
                .get("STCG15Per", {})
                .get("IncBFLA", {})
                .get("IncOfCurYrAfterSetOffBFLosses", 0)
            )

            # Extract values safely
            fields = [
                stcg_15.get("Upto15Of6", 0),
                stcg_15.get("Up16Of6To15Of9", 0),
                stcg_15.get("Up16Of9To15Of12", 0),
                stcg_15.get("Up16Of12To15Of3", 0),
                stcg_15.get("Up16Of3To31Of3", 0),
            ]

            # Convert all to numbers
            total_sum = 0
            for val in fields:
                try:
                    total_sum += float(val)
                except Exception:
                    pass

            try:
                bfl_stcg_15 = float(bfl_stcg_15)
            except Exception:
                bfl_stcg_15 = 0

            if total_sum != bfl_stcg_15:
                error_list.append(error_dict)

        except Exception:
            pass     
    
    @staticmethod
    def rule_2025_384(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_S30_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder30Per.DateRange.Upto15Of6)
        + (ITR6CG_S30_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder30Per.DateRange.Up16Of6To15Of9) 
        + (ITR6CG_S30_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder30Per.DateRange.Up16Of9To15Of12)
        +(ITR6CG_S30_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder30Per.DateRange.Up16Of12To15Of3)
        +(ITR6CG_S30_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder30Per.DateRange.Up16Of3To31Of3) 
        should be equal to ITR6BFLA_STCG_30_Col_5 (ITR.ITR6.ScheduleBFLA.STCG30Per.IncBFLA.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 3 the breakup of all the quarters should be equal to the value from item 5vii of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_384",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            stcg_30 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleCG", {})
                .get("AccruOrRecOfCG", {})
                .get("ShortTermUnder30Per", {})
                .get("DateRange", {})
            )

            bfl_stcg_30 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleBFLA", {})
                .get("STCG30Per", {})
                .get("IncBFLA", {})
                .get("IncOfCurYrAfterSetOffBFLosses", 0)
            )

            # Extract values safely
            fields = [
                stcg_30.get("Upto15Of6", 0),
                stcg_30.get("Up16Of6To15Of9", 0),
                stcg_30.get("Up16Of9To15Of12", 0),
                stcg_30.get("Up16Of12To15Of3", 0),
                stcg_30.get("Up16Of3To31Of3", 0),
            ]

            # Convert all to numbers
            total_sum = 0
            for val in fields:
                try:
                    total_sum += float(val)
                except Exception:
                    pass

            try:
                bfl_stcg_30 = float(bfl_stcg_30)
            except Exception:
                bfl_stcg_30 = 0

            if total_sum != bfl_stcg_30:
                error_list.append(error_dict)

        except Exception:
            pass   
    
    @staticmethod
    def rule_2025_385(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_SAR_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderAppRate.DateRange.Upto15Of6)
        + (ITR6CG_SAR_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderAppRate.DateRange.Up16Of6To15Of9) 
        + (ITR6CG_SAR_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderAppRate.DateRange.Up16Of9To15Of12) 
        +(ITR6CG_SAR_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderAppRate.DateRange.Up16Of12To15Of3)
        +(ITR6CG_SAR_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderAppRate.DateRange.Up16Of3To31Of3) 
        should be equal to ITR6BFLA_STCG_AR_Col_5 (ITR.ITR6.ScheduleBFLA.STCGAppRate.IncBFLA.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 4 the breakup of all the quarters should be equal to the value from item 5viii of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_385",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            stcg_sar = (
                payload["ITR"]["ITR6"]
                .get("ScheduleCG", {})
                .get("AccruOrRecOfCG", {})
                .get("ShortTermUnderAppRate", {})
                .get("DateRange", {})
            )

            bfl_stcg_sar = (
                payload["ITR"]["ITR6"]
                .get("ScheduleBFLA", {})
                .get("STCGAppRate", {})
                .get("IncBFLA", {})
                .get("IncOfCurYrAfterSetOffBFLosses", 0)
            )

            # Extract date range values
            fields = [
                stcg_sar.get("Upto15Of6", 0),
                stcg_sar.get("Up16Of6To15Of9", 0),
                stcg_sar.get("Up16Of9To15Of12", 0),
                stcg_sar.get("Up16Of12To15Of3", 0),
                stcg_sar.get("Up16Of3To31Of3", 0),
            ]

            total_sum = 0
            for val in fields:
                try:
                    total_sum += float(val)
                except Exception:
                    pass

            try:
                bfl_stcg_sar = float(bfl_stcg_sar)
            except Exception:
                bfl_stcg_sar = 0

            if total_sum != bfl_stcg_sar:
                error_list.append(error_dict)

        except Exception:
            pass   
    
    @staticmethod
    def rule_2025_386(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_SDTAA_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderDTAARate.DateRange.Upto15Of6)
        + (ITR6CG_SDTAA_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderDTAARate.DateRange.Up16Of6To15Of9) 
        + (ITR6CG_SDTAA_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderDTAARate.DateRange.Up16Of9To15Of12) 
        +(ITR6CG_SDTAA_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderDTAARate.DateRange.Up16Of12To15Of3)
        +(ITR6CG_SDTAA_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnderDTAARate.DateRange.Up16Of3To31Of3) 
        should be equal to ITR6BFLA_STCG_DTAA_Col_5 (ITR.ITR6.ScheduleBFLA.STCGDTAARate.IncBFLA.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 5 the breakup of all the quarters should be equal to the value from item 5ix of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_386",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            stcg_dtaa = (
                payload["ITR"]["ITR6"]
                .get("ScheduleCG", {})
                .get("AccruOrRecOfCG", {})
                .get("ShortTermUnderDTAARate", {})
                .get("DateRange", {})
            )

            bfl_stcg_dtaa = (
                payload["ITR"]["ITR6"]
                .get("ScheduleBFLA", {})
                .get("STCGDTAARate", {})
                .get("IncBFLA", {})
                .get("IncOfCurYrAfterSetOffBFLosses", 0)
            )

            # Extract date range values
            fields = [
                stcg_dtaa.get("Upto15Of6", 0),
                stcg_dtaa.get("Up16Of6To15Of9", 0),
                stcg_dtaa.get("Up16Of9To15Of12", 0),
                stcg_dtaa.get("Up16Of12To15Of3", 0),
                stcg_dtaa.get("Up16Of3To31Of3", 0),
            ]

            total_sum = 0
            for val in fields:
                try:
                    total_sum += float(val)
                except Exception:
                    pass

            try:
                bfl_stcg_dtaa = float(bfl_stcg_dtaa)
            except Exception:
                bfl_stcg_dtaa = 0

            if total_sum != bfl_stcg_dtaa:
                error_list.append(error_dict)

        except Exception:
            pass   
    
    @staticmethod
    def rule_2025_387(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_L10_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder10Per.DateRange.Upto15Of6)
        + (ITR6CG_L10_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder10Per.DateRange.Up16Of6To15Of9) 
        + (ITR6CG_L10_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder10Per.DateRange.Up16Of9To15Of12) 
        +(ITR6CG_L10_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder10Per.DateRange.Up16Of12To15Of3)
        +(ITR6CG_L10_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder10Per.DateRange.Up16Of3To31Of3) 
        should be equal to ITR6BFLA_LTCG_10_Col_5 (ITR.ITR6.ScheduleBFLA.LTCG10Per.IncBFLA.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 6 the breakup of all the quarters should be equal to the value from item 5xa of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_387",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            ltcg_10 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleCG", {})
                .get("AccruOrRecOfCG", {})
                .get("LongTermUnder10Per", {})
                .get("DateRange", {})
            )

            bfl_ltcg_10 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleBFLA", {})
                .get("LTCG10Per", {})
                .get("IncBFLA", {})
                .get("IncOfCurYrAfterSetOffBFLosses", 0)
            )

            # Extract date range values
            fields = [
                ltcg_10.get("Upto15Of6", 0),
                ltcg_10.get("Up16Of6To15Of9", 0),
                ltcg_10.get("Up16Of9To15Of12", 0),
                ltcg_10.get("Up16Of12To15Of3", 0),
                ltcg_10.get("Up16Of3To31Of3", 0),
            ]

            total_sum = 0
            for val in fields:
                try:
                    total_sum += float(val)
                except Exception:
                    pass

            try:
                bfl_ltcg_10 = float(bfl_ltcg_10)
            except Exception:
                bfl_ltcg_10 = 0

            if total_sum != bfl_ltcg_10:
                error_list.append(error_dict)

        except Exception:
            pass

    @staticmethod
    def rule_2025_389(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_L20_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder20Per.DateRange.Upto15Of6)
        + (ITR6CG_L20_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder20Per.DateRange.Up16Of6To15Of9) 
        + (ITR6CG_L20_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder20Per.DateRange.Up16Of9To15Of12) 
        +(ITR6CG_L20_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder20Per.DateRange.Up16Of12To15Of3)
        +(ITR6CG_L20_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder20Per.DateRange.Up16Of3To31Of3) 
        should be equal to ITR6BFLA_LTCG_20_Col_5 (ITR.ITR6.ScheduleBFLA.LTCG20Per.IncBFLA.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 8 the breakup of all the quarters should be equal to the value from item 5xi of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_389",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            ltcg_20 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleCG", {})
                .get("AccruOrRecOfCG", {})
                .get("LongTermUnder20Per", {})
                .get("DateRange", {})
            )

            bfl_ltcg_20 = (
                payload["ITR"]["ITR6"]
                .get("ScheduleBFLA", {})
                .get("LTCG20Per", {})
                .get("IncBFLA", {})
                .get("IncOfCurYrAfterSetOffBFLosses", 0)
            )

            # Extract date range values
            fields = [
                ltcg_20.get("Upto15Of6", 0),
                ltcg_20.get("Up16Of6To15Of9", 0),
                ltcg_20.get("Up16Of9To15Of12", 0),
                ltcg_20.get("Up16Of12To15Of3", 0),
                ltcg_20.get("Up16Of3To31Of3", 0),
            ]

            total_sum = 0
            for val in fields:
                try:
                    total_sum += float(val)
                except Exception:
                    pass

            try:
                bfl_ltcg_20 = float(bfl_ltcg_20)
            except Exception:
                bfl_ltcg_20 = 0

            if total_sum != bfl_ltcg_20:
                error_list.append(error_dict)

        except Exception:
            pass   
    
    @staticmethod
    def rule_2025_390(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_LDTAA_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnderDTAARate.DateRange.Upto15Of6)
        + (ITR6CG_LDTAA_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnderDTAARate.DateRange.Up16Of6To15Of9)
        + (ITR6CG_LDTAA_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnderDTAARate.DateRange.Up16Of9To15Of12) 
        +(ITR6CG_LDTAA_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnderDTAARate.DateRange.Up16Of12To15Of3)
        +(ITR6CG_LDTAA_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnderDTAARate.DateRange.Up16Of3To31Of3) 
        should be equal to ITR6BFLA_LTCG_DTAA_Col_5 (ITR.ITR6.ScheduleBFLA.LTCGDTAARate.IncBFLA.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 9 the breakup of all the quarters should be equal to the value from item 5xii of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_390",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            ltdtaa = (
                payload["ITR"]["ITR6"]
                .get("ScheduleCG", {})
                .get("AccruOrRecOfCG", {})
                .get("LongTermUnderDTAARate", {})
                .get("DateRange", {})
            )

            bfl_ltdtaa = (
                payload["ITR"]["ITR6"]
                .get("ScheduleBFLA", {})
                .get("LTCGDTAARate", {})
                .get("IncBFLA", {})
                .get("IncOfCurYrAfterSetOffBFLosses", 0)
            )

            # Extract date range values
            fields = [
                ltdtaa.get("Upto15Of6", 0),
                ltdtaa.get("Up16Of6To15Of9", 0),
                ltdtaa.get("Up16Of9To15Of12", 0),
                ltdtaa.get("Up16Of12To15Of3", 0),
                ltdtaa.get("Up16Of3To31Of3", 0),
            ]

            total_sum = 0
            for val in fields:
                try:
                    total_sum += float(val)
                except Exception:
                    pass

            try:
                bfl_ltdtaa = float(bfl_ltdtaa)
            except Exception:
                bfl_ltdtaa = 0

            if total_sum != bfl_ltdtaa:
                error_list.append(error_dict)

        except Exception:
            pass
    
    @staticmethod
    def rule_2025_843(payload,error_list):
        '''
        Summery Line 
        ITR6ChVIA_ParB_Tot_SC (ITR.ITR6.ScheduleVIA.DeductUndChapVIA.TotPartBchapterVIA) 
        this cannot be more than '0' if 
        ITR6PAG1_Opt_115BA_BAA_BAB (ITR.ITR6.PartA_GEN1.FilingStatus.Section115BA) or 
        ITR6PAG1_Opt_115BA_BAA_BAB_Sec (ITR.ITR6.PartA_GEN1.FilingStatus.SectionCurrAY) 
        is Selected as 115BAA/115BAB
        '''
        try:
            error_dict = {
                "remark": "Deduction under Part B cannot be claimed if New tax regime is selected (115BAA or 115BAB)",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_843",
                "name_range": "Ded_Chap_VIA_Part_B"
            }

            filing_status = payload["ITR"]["ITR6"].get("PartA_GEN1", {}).get("FilingStatus", {})
            section_115ba = str(filing_status.get("Section115BA", "")).strip()
            section_curr_ay = str(filing_status.get("SectionCurrAY", "")).strip()

            tot_part_b = payload["ITR"]["ITR6"].get("ScheduleVIA", {}) \
                                            .get("DeductUndChapVIA", {}) \
                                            .get("TotPartBchapterVIA", 0)

            # Convert to int/float safely
            try:
                tot_part_b = float(tot_part_b)
            except:
                tot_part_b = 0

            if section_115ba in ("115BAA", "115BAB") or section_curr_ay in ("115BAA", "115BAB"):
                if tot_part_b > 0:
                    error_dict["field_value"] = tot_part_b
                    error_list.append(error_dict)

        except Exception:
            pass   
    
    @staticmethod
    def rule_2025_383(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_S20_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder20Per.DateRange.Upto15Of6)
        +(ITR6CG_S20_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder20Per.DateRange..Up16Of6To15Of9)
        +(ITR6CG_S20_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder20Per.DateRange.Up16Of9To15Of12)
        +(ITR6CG_S20_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.ShortTermUnder20Per.DateRange.Up16Of12To15Of3) 
        should be equla to  ITR6BFLA_STCG_20_Col_5 (ITR.ITR6.ScheduleBFLA.STCG20Per.IncBFLA.IncOfCurYrUndHeadFromCYLA)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 2 the breakup of all the quarters should be equal to the value from item 5vib of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_383",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            schedule_cg = payload["ITR"]["ITR6"].get("ScheduleCG", {}) \
                                            .get("AccruOrRecOfCG", {}) \
                                            .get("ShortTermUnder20Per", {}) \
                                            .get("DateRange", {})

            sum_val = 0
            for key in ["Upto15Of6", "Up16Of6To15Of9", "Up16Of9To15Of12", "Up16Of12To15Of3"]:
                try:
                    sum_val += float(schedule_cg.get(key, 0))
                except:
                    pass

            bfla_val = payload["ITR"]["ITR6"].get("ScheduleBFLA", {}) \
                                            .get("STCG20Per", {}) \
                                            .get("IncBFLA", {}) \
                                            .get("IncOfCurYrUndHeadFromCYLA", 0)
            try:
                bfla_val = float(bfla_val)
            except:
                bfla_val = 0

            if sum_val != bfla_val:
                error_list.append(error_dict)

        except Exception:
            pass   
    
    @staticmethod
    def rule_2025_388(payload,error_list):
        '''
        Summery Line 
        (ITR6CG_L12.5_156) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Upto15Of6)
        +(ITR6CG_L12.5_159) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Upto15Of6)
        +(ITR6CG_L12.5_1512) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Upto15Of6)
        +(ITR6CG_L12.5_153) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Upto15Of6)
        +(ITR6CG_L12.5_313) (ITR.ITR6.ScheduleCG.AccruOrRecOfCG.LongTermUnder12_5Per.DateRange.Upto15Of6) 
        should be equal to ITR6BFLA_LTCG_12.5_Col_5 (ITR.ITR6.ScheduleBFLA.LTCG12_5Per.IncOfCurYrAfterSetOffBFLosses)
        '''
        try:
            error_dict = {
                "remark": "In Schedule CG, Table F Sl. No. 7 the breakup of all the quarters should be equal to the value from item 5xb of schedule BFLA",
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_388",
                "name_range": "Capital_Gain_Qtr_breakup"
            }

            cgt = payload["ITR"]["ITR6"].get("ScheduleCG", {}) \
                                    .get("AccruOrRecOfCG", {}) \
                                    .get("LongTermUnder12_5Per", {}) \
                                    .get("DateRange", {})

            # Get all five parts
            part_156  = float(cgt.get("Upto15Of6", 0) or 0)
            part_159  = float(cgt.get("Up16Of6To15Of9", 0) or 0)
            part_1512 = float(cgt.get("Up16Of9To15Of12", 0) or 0)
            part_153  = float(cgt.get("Up16Of12To15Of3", 0) or 0)
            part_313  = float(cgt.get("Up16Of3To31Of3", 0) or 0)

            total_sum = part_156 + part_159 + part_1512 + part_153 + part_313

            bfla_val = payload["ITR"]["ITR6"].get("ScheduleBFLA", {}) \
                                            .get("LTCG12_5Per", {}) \
                                            .get("IncOfCurYrAfterSetOffBFLosses", 0)

            try:
                bfla_val = float(bfla_val)
            except:
                bfla_val = 0

            if total_sum != bfla_val:
                error_list.append(error_dict)

        except Exception:
            pass   
    
    @staticmethod
    def rule_2025_548(payload,error_list):
        '''
        Summery Line 
        "ITR6OS_Gr_Div_2_22f (ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.Dividend22f) should be equal to sum of 
        (ITR6OS_Div_2_22_f_15_6) (ITR.ITR6.ScheduleOS.DividendIncUs115BBDAaiii.DateRange.Upto15Of6)  +
        (ITR6OS_Div_2_22_f_15_9) (ITR.ITR6.ScheduleOS.DividendIncUs115BBDAaiii.DateRange.Up16Of6To15Of9) +
        (ITR6OS_Div_2_22_f_15_12) (ITR.ITR6.ScheduleOS.DividendIncUs115BBDAaiii.DateRange.Up16Of9To15Of12) +
        (ITR6OS_Div_2_22_f_15_3) (ITR.ITR6.ScheduleOS.DividendIncUs115BBDAaiii.DateRange.Up16Of12To15Of3) +
        (ITR6OS_Div_2_22_f_31_3) (ITR.ITR6.ScheduleOS.DividendIncUs115BBDAaiii.DateRange.Up16Of3To31Of3) +"
        '''
        try:
            error_dict = {
                "remark": 'In Schedule OS, Sl. No. 10 the quarterly break up of Dividend Income referred in Sl. No. 1a(iii) should be equal to Sl. No. 1a(iii) Dividend income u/s 2(22)(f)',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_548",
                "name_range": "Qty_Income_breakup"
            }

            dividend_declared = payload["ITR"]["ITR6"].get("ScheduleOS", {}) \
                                                    .get("IncOthThanOwnRaceHorse", {}) \
                                                    .get("Dividend22f", 0)

            try:
                dividend_declared = float(dividend_declared)
            except:
                dividend_declared = 0

            # Breakups
            div_ranges = payload["ITR"]["ITR6"].get("ScheduleOS", {}) \
                                            .get("DividendIncUs115BBDAaiii", {}) \
                                            .get("DateRange", {})

            part_156  = float(div_ranges.get("Upto15Of6", 0) or 0)
            part_159  = float(div_ranges.get("Up16Of6To15Of9", 0) or 0)
            part_1512 = float(div_ranges.get("Up16Of9To15Of12", 0) or 0)
            part_153  = float(div_ranges.get("Up16Of12To15Of3", 0) or 0)
            part_313  = float(div_ranges.get("Up16Of3To31Of3", 0) or 0)

            total_sum = part_156 + part_159 + part_1512 + part_153 + part_313

            # Compare
            if total_sum != dividend_declared:
                error_list.append(error_dict)

        except Exception:
            pass   

    @staticmethod
    def rule_2025_549(payload,error_list):
        '''
        Summery Line 
        If ITR6CG_STCL_Buyback (ITR.ITR6.ScheduleCG.ShortTermCapGain.CapitalLossBuyBackShares.TotalCapitalLossBuyBackShares) is 
        > 0 
        then ITR6OS_Gr_Div_2_22f (ITR.ITR6.ScheduleOS.IncOthThanOwnRaceHorse.Dividend22f) cannot be blank
        '''
        try:
            error_dict = {
                "remark": 'Kindly fill in the details of dividend in Sl.No. 1a(iii) of schedule OS if buy back loss is claimed in schedule CG',
                "field_name": "",
                "validation_status": "Error",
                "field_value": "",
                "error_code": "2025_549",
                "name_range": "OS_Div_22_f"
            }

            buyback_loss = payload["ITR"]["ITR6"].get("ScheduleCG", {}) \
                                                .get("ShortTermCapGain", {}) \
                                                .get("CapitalLossBuyBackShares", {}) \
                                                .get("TotalCapitalLossBuyBackShares", 0)

            dividend_declared = payload["ITR"]["ITR6"].get("ScheduleOS", {}) \
                                                    .get("IncOthThanOwnRaceHorse", {}) \
                                                    .get("Dividend22f")

            try:
                buyback_loss = float(buyback_loss)
            except:
                buyback_loss = 0

            # Rule check
            if buyback_loss < 0 and (dividend_declared in (None, "", 0)):
                error_dict["field_value"] = {
                    "buyback_loss": buyback_loss,
                    "dividend22f": dividend_declared
                }
                error_list.append(error_dict)

        except Exception:
            pass   

    @staticmethod
    def rule_compensation_negative_check(payload, error_list, workbook):
        '''
        Summary Line
            "Please enter only zero or positive values in the 'Compensation to Employees' section (Profit & Loss Statement)"
            Check if values in specified nameranges are negative.
        '''
        name_ranges = [
            "ITR6PLIndAS_SalWag",
            "ITR6PLIndAS_Bonus",
            "ITR6PLIndAS_RemMedExp",
            "ITR6PLIndAS_LevEnc",
            "ITR6PLIndAS_LevTrBen",
            "ITR6PLIndAS_SuperAnnFund",
            "ITR6PLIndAS_RecPF",
            "ITR6PLIndAS_RecGraFund",
            "ITR6PLIndAS_AnyOthFund",  
            "ITR6PLIndAS_AnyOthBen",
            "ITR6PL_SalWag",
            "ITR6PL_Bonus",
            "ITR6PL_RemMedExp",
            "ITR6PL_LevEnc",
            "ITR6PL_LevTrBen",
            "ITR6PL_SuperAnnFund",
            "ITR6PL_RecPF",
            "ITR6PL_RecGraFund",
            "ITR6PL_AnyOthFund",
            "ITR6PL_AnyOthBen",
            "ITR6PLIndAS_Paid_NR_Amt"
        ]
 
        for name_range in name_ranges:
            try:
                val = BusinessValidation.get_name_range_data(workbook, name_range, is_int=True)
                
                if isinstance(val, (int, float)) and val < 0:
                     error_dict = {
                        "remark": "Please enter only zero or positive values in the 'Compensation to Employees' section (Profit & Loss Statement)",
                        "validation_status": "Error",
                        "field_value": val,
                        "field_name": "",
                        "error_code": "555",
                        "name_range": name_range
                    }
                     error_list.append(error_dict)
            except Exception:
                pass