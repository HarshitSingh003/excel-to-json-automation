DATE_FORMATES = ["%d/%m%Y","%d-%m-Y", "%d/%b/%Y", "%d-%b-%Y", "%d/%m/%Y"]
DATE_FIELDS = [
    "JSONCreationDate",
    "ITR.ITR6.PartA_GEN1.OrgFirmInfo.DateOFFormOrIncorp",
    "ITR.ITR6.PartA_GEN1.FilingStatus.OrigRetFiledDate",
    "ITR.ITR6.PartA_GEN2For6.AuditInfo.AuditReportFurnishDate",
    "ITR.ITR6.PartA_GEN2For6.AuditDetails92E.DateOfAudit",
    "ITR.ITR6.PartA_GEN2For6.AuditInfo.AuditDate",
    "ITR.ITR6.PartA_GEN1.FilingStatus.NoticeDateUnderSec",
    "ITR.ITR6.PartA_GEN1.FilingStatus.OrigRetFiledDate",
    "ITR.ITR6.PartA_GEN2For6.AuditInfo.AuditReportFurnishDate",
    "ITR.ITR6.PartA_GEN2For6.AuditInfo.AuditDate",
    "ITR.ITR6.PartA_GEN1.OrgFirmInfo.DateofBusCommencement",
    "ITR.ITR6.PartA_GEN1.FilingStatus.NoticeDateUnderSec",
    "ITR.ITR6.PartA_GEN2For6.AuditDetails92E.DateOfAudit",
    ".DateOfBusinessOrg",
    "ITR.ITR6.PartA_GEN2For6.AuditDetails.DateOfAudit",
    "ITR.ITR6.PartA_GEN2For6.AuditReportDetails.AuditReportDate",
    "ITR.ITR6.ScheduleIT.TaxPayment.DateDep",
    "ITR.ITR6.PartA_GEN2For6.AuditInfo.AuditDate",
    "ITR.ITR6.PartA_GEN2For6.AuditInfo.AuditDate"
]

TRANSFORM_FIELDS = [
    "ITR.ITR6.PartA_GEN2For6.TotalSalesExcOneCr",
    "CompDetails.AddressDetailWithZipCode.StateCode",
    "EmployerOrDeductorOrCollectDetl.TCSCreditName",
    "CompDetails.AddressDetailWithZipCode.CountryCode",
    "ITR.ITR6.PartA_GEN1.FilingStatus.Section115BA",
    "ITR.ITR6.PartA_GEN1.FilingStatus.SectionCurrAY",
    "ITR.ITR6.PartA_GEN1.FilingStatus.Section115CurrAY",
    "EmployerOrDeductorOrCollectDetl.TCSCreditName",
    "ShareType",
    "AddressDetail.StateCode",
    "ITR.ITR6.ScheduleHP.PropertyDetails.AddressDetailWithZipCode.StateCode",
    "ITR.ITR6.ScheduleHP.PropertyDetails.PropertyOwner",
    "ITR.ITR6.ScheduleHP.PropertyDetails.Rentdetails.Section24B.Section24BDtls.BankOrInstnName",
    "ITR.ITR6.ScheduleHP.PropertyDetails.Rentdetails.Section24B.Section24BDtls.LoanTknFrom",
    "LoanTknFrom",
    "BankOrInstnName",
    "AddressDetailWithZipCode.StateCode",
    "AddressDetailWithZipCode.CountryCode",
    "Designation",
    "AddressDetailWithZipCode.CountryCode",
    "CountryOfResidence",
    "Code",
    "AgriLandIrrigatedFlag",
    "AuditReportAct",
    "AgriLandOwnedFlag",
    "CountryCode",
    "UnitOfMeasure",
    "AssetParticulars",
    "AssetParticularsOthers",
    "ListedUnlistedFlag",
    "SecuritiesType",
    "RelevantClauseUndrDedClaimed",
    "TypeOfIncome",
    "ShareholderCategory",
    "StateCode",
    "Purpose",
    "ApplicantCategory",
    "CessationMode",
    "ITR.ITR6.ScheduleCG.LongTermCapGain.UnutilizedLtcgFlag",
    "ITR.ITR6.ScheduleCG.ShortTermCapGain.UnutilizedStcgFlag",
    "TDSCreditName",
    "HeadOfIncome",
    "Section115BA",
    "Section115CurrAY",
    "ShareOnOrBefore",
    "CountryName",
    "ifLetOut",
    "ITR.ITR6.PartA_GEN1.OrgFirmInfo.Address.CountryCode",
    "ITR.ITR6.PartA_GEN1.OrgFirmInfo.Address.StateCode",
    "ITR.ITR6.PARTA_OI.MethodOfAcct",
    "ITR.ITR6.PartA_GEN2For6.HoldingStatus.NatOfCompFlg",
    "ITR.ITR6.PartA_GEN1.FilingStatus.ReturnFileSec.IncomeTaxSec",
    "ITR.ITR6.PartA_GEN1.FilingStatus.ResidentialStatus",
    "ITR.ITR6.PartA_GEN1.OrgFirmInfo.StatusOrCompanyType",
    "ITR.ITR6.Verification.Declaration.Capacity",
    "ITR.ITR6.PartA_GEN1.FilingStatus.AssesseeRep.RepCapacity",
    "ITR.ITR6.Schedule80GGA.DonationDtlsSciRsrchRuralDev.AddressDetail.StateCode",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsBldLandNotResHouseUC.Purpose",
    "ITR.ITR6.ScheduleSH.ShrhldngStartUps.SHDtlsAnyTimePrevYearSU.CessationMode",
    "ITR.ITR6.ScheduleSH.ShrhldngStartUps.DtlsShareAppMoneyAlltEndPrvYr.ApplicantCategory",
    "OpenBalShareType",
    "OpenBalAcquisitionCost",
    "ShrsAcqNumberOfShares",
    "ShrsAcqShareType",
    "ShrsAcqAcquisitionCost",
    "ShrsTrsNumberOfShares",
    "ShrsTrsShareType",
    "ShrsTrsSaleConsdr",
    "ClBalNumberOfShares",
    "ClBalShareType",
    "ResidentialStatus",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.OpenBalShareType",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.OpenBalAcquisitionCost",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ShrsAcqNumberOfShares",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ShrsAcqShareType",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ShrsAcqAcquisitionCost",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ShrsTrsNumberOfShares",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ShrsTrsShareType",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ShrsTrsSaleConsdr",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ClBalNumberOfShares",
    "ITR.ITR6.ScheduleAL.AsstLiabilitiesUnlistedCompany.DtlsListedEquitySharesUC.ClBalShareType",
    "ITR.ITR6.ScheduleSH.ShrhldngUnlistedCompany.DtlsSHEndPreviousYearUC.ResidentialStatus",
    "ITR.ITR6.Schedule80GGA.DonationDtlsSciRsrchRuralDev.AddressDetail.StateCode",
    "ITR.ITR6.Schedule115AD.Schedule115ADDtls.ShareOnOrBefore",
    "EntityType",
    "IncmTypeUnt",
    "ITR.ITR6.PartA_GEN1.FilingStatus.Cndnfor44AB",
    "AccountType",
    "ITR.ITR6.PartB_TTI.Refund.BankAccountDtls.AddtnlBankDetails.AccountType",
    "Rate",
    "ShareTransferredOnOrBefore"
]

SECTION_FIELDS = ["TDSSection", "Rate"]

SECTION_MAPPING = {
    "193": "193",
    "194": "194",
    "194A": "94A",
    "194B": "94B",
    "194BA": "94BA",
    "194BB": "4BB",
    "194C": "94C",
    "194D": "94D",
    "194DA": "4DA",
    "194E": "94E",
    "194EE": "4EE",
    "194F": "4F",
    "194G": "4G",
    "194H": "4H",
    "194I(a)": "4-IA",
    "194I(b)": "4-IB",
    "194IA": "4IA",
    "194IB": "4IB",
    "194IC": "4IC",
    "194J(a)": "94J-A",
    "194JA": "94J-A",
    "194J(b)": "94J-B",
    "194JB": "94J-B",
    "194K": "94K",
    "194LA": "4LA",
    "194LB": "4LB",
    "194LC (2)(i) and (ia)": "4LC1",
    "194LC (2)(ib)": "4LC2",
    "194LC (2)(ic)": "4LC3",
    "194LBA(a)": "4BA1",
    "194LBA(b)": "4BA2",
    "194LBA(c)": "LBA3",
    "194LBB": "LBB",
    "194R": "94R",
    "194S": "94S",
    "194B/4BP": "94B-P",
    "194R/4RP": "94R-P",
    "194S/4SP": "94S-P",
    "194LBC": "LBC",
    "194LD": "4LD",
    "194M": "94M",
    "194N": "94N",
    "194N -First Proviso": "94N-F",
    "194N- Third Proviso": "94N-C",
    "194N- First Proviso read with Third Proviso": "94N-FT",
    "194O": "94O",
    "194P": "94P",
    "194Q": "94Q",
    "195": "195",
    "196A": "96A",
    "196B": "96B",
    "196C": "96C",
    "196D": "96D",
    "196D(1A)": "96DA",
    "194BA(2)": "94BA-P",
    "Loss from buy back of 'shares taxable at 10%'": "LTL10",
    "Loss from buy back of 'shares taxable at 12.5%'": "LTL12_5",
	"Loss from buy back of 'shares taxable at 20%'": "STL20",
    "Loss from buy back of 'shares taxable at 30%'": "STL30",
    "Loss from buy back of 'shares taxable at applicable rate'": "STLAR"
}


BOOL_REPLACE_FIELDS = ["UseForRefund"]

STRING_FIELDS = [
    "ITR6OI_Cls_Stk_RM",
    "ITR6OI_Cls_Stk_FG",
    "ValFinishedGoods",
    "GrossReceipt",
    "ValRawMaterial",
    "PLAcntPrepSchedVICompAct",
    "PLAcctFlg"
]

EXCEPTIONAL_FIELDS = [
    "ITR.ITR6.PARTA_BSIndAS.EquityAndLiablities.Equity.OtherEquityReserv.OthersTotal",
    "ITR.ITR6.PARTA_BSIndAS.EquityAndLiablities.Equity.OtherEquityReserv.TotalOtherResrv",
    "ITR.ITR6.PartB-TI.CapGain.CapGains30Per115BBH",
    "ITR.ITR6.ScheduleCG.IncmFromVDATrnsf"
]

SELECT_REPLACE_VALUES = ["Select", "(Select)","(SELECT)"]

EMPTY_REPLACE_VALUES = [None]

INT_FIELDS = [
    "CountryCodeMobile",
    "MobileNo",
    "IncomeTaxSec",
    "GrossReceipt",
    "PinCode"
]

DECRYPT_FIELDS = [
    "RepAadhaar", 
    "AudFrmAadhaar", 
    "KeyPersnAadhaar"
]


Schedule80_IA_config = [
{   
    "parent": "Schedule80_IA",
    "child": "DeductUs80_IA_4_i",
    "value": "INFRAFAC"
},
{   
    "parent": "Schedule80_IA",
    "child": "DeductUs80_IA_4_iv",
    "value": "POWER"
},
{
    "parent": "Schedule80_IA",
    "child": "DeductUs80_IA_4_v",
    "value": "REVIVAL_POWER_PLNT"
}]

Schedule80_IB_config = [
{   
    "parent": "Schedule80_IB",
    "child": "DeductJKLocUs80_IB_4_Und",
    "value": "INDSRTL_JK"
},
{   
    "parent": "Schedule80_IB",
    "child": "DeductMinOilUs80_IB_9_Und",
    "value": "COMM_PROD"
},
{
    "parent": "Schedule80_IB",
    "child": "DeductHousUs80_IB_10_Und",
    "value": "HOUSING_PROJECT"
},
{
    "parent": "Schedule80_IB",
    "child": "DeductFruitVegUs80_IB_11A_Und",
    "value": "FRIUTS_VEGTBLE"
},
{
    "parent": "Schedule80_IB",
    "child": "DeductFoodGrainUs80_IB_11A_Und",
    "value": "STOR_TRANS"
}]

Schedule80_IC_config = [
{   
    "parent": "Schedule80_IC",
    "child": "DeductInSikkim_Und",
    "value": "INDSTRL_SIKKIM"
},
{   
    "parent": "Schedule80_IC",
    "child": "DeductInHimachalP_Und",
    "value": "INDSRTL_HP"
},
{
    "parent": "Schedule80_IC",
    "child": "DeductInUttaranchal_Und",
    "value": "INDSRTL_UTTARANCHAL"
}]

Schedule80_IC_DeductInNorthEast_config = [
{   
    "parent": "Schedule80_IC",
    "child": "DeductInNorthEast",
    "s_child":"Assam_Und",
    "value": "INDSRTL_ASSAM"
},
{
    "parent": "Schedule80_IC",
    "child": "DeductInNorthEast",
    "s_child":"ArunachalPradesh_Und",
    "value": "INDSRTL_ARUNPRADESH"
},
{
    "parent": "Schedule80_IC",
    "child": "DeductInNorthEast",
    "s_child":"Manipur_Und",
    "value": "INDSRTL_MANIPUR"
},
{
    "parent": "Schedule80_IC",
    "child": "DeductInNorthEast",
    "s_child":"Mizoram_Und",
    "value": "INDSRTL_MIZORAM"
},
{
    "parent": "Schedule80_IC",
    "child": "DeductInNorthEast",
    "s_child":"Meghalaya_Und",
    "value": "INDSRTL_MEGHALAYA"
},
{
    "parent": "Schedule80_IC",
    "child": "DeductInNorthEast",
    "s_child":"Nagaland_Und",
    "value": "INDSRTL_NAGALND"
},
{
    "parent": "Schedule80_IC",
    "child": "DeductInNorthEast",
    "s_child":"Tripura_Und",
    "value": "INDSRTL_TRIPURA"
}]

VALIDATE_VALUE = [
    "DetailsForiegnBank",
    "DtlsForeignCustodialAcc",
    "DtlsForeignEquityDebtInterest",
    "DtlsForeignCashValueInsurance",
    "DetailsFinancialInterest",
    "DetailsImmovableProperty",
    "DetailsOthAssets",
    "DetailsOfAccntsHvngSigningAuth",
    "DetailsOfTrustOutIndiaTrustee",
    "DetailsOfOthSourcesIncOutsideIndia"
    ]


CHECK_DEF_AND_SET = ["UseForRefund"]

# valto_replace_capacity=[{"Keys":["AS"],"value":"A"}]

# sSharedSecretKey = "AWubbjbVYQIg9vhh"
# iteration = 1000