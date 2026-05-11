from .transformation import DataTypeTransformation
MANDATORY_NODE_STRUCTURE = {
    "CreationInfo": {
        "field_required": [
            ("SWVersionNo", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("SWCreatedBy", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("JSONCreatedBy", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("JSONCreationDate",str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
            ("IntermediaryCity", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("Digest", str, DataTypeTransformation.str_transform, False, None, None, None),
        ],
    },
    "Form_ITR6": {
        "field_required": [
            ("FormName", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("Description", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("AssessmentYear", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("SchemaVer",str, DataTypeTransformation.str_transform, False, None, None, None),
            ("FormVer", str, DataTypeTransformation.str_transform, False, None, None, None),
        ],
    },
    "PartA_GEN1": {
        "node_required":{
            "OrgFirmInfo": {
                "node_required": {
                    "Address":{
                        "node_optional": {
                            "Phone": {
                                "field_optional": [
                                    ("STDcode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PhoneNo", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("STDcode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PhoneNo", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_required": [
                            ("ResidenceNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("LocalityOrArea", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCodeMobile", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("MobileNo", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EmailAddress", str, DataTypeTransformation.str_transform, True, None, None, None),
                        ],
                        "field_optional": [
                            ("ResidenceName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("RoadOrStreet", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("MobileNoSec", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CountryCodeMobileNoSec", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("EmailAddressSecondary", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    },
                    "AssesseeName": {
                        "field_required": [
                            ("SurNameOrOrgName", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "field_optional": [
                            ("OrgOldName", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
                "field_required": [
                    ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateOFFormOrIncorp", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("StatusOrCompanyType", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("DomesticCompFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "field_optional": [
                    ("CINissuedByMCA", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateofBusCommencement", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                ]
            },
            "FilingStatus": {
                "node_required": {
                    "ReturnFileSec":{
                        "field_required": [
                            ("IncomeTaxSec", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    },
                },
                "node_optional": {
                    "AssesseeRep": {
                        "field_optional": [
                            ("RepName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("RepCapacity", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("RepAddress", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("RepPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("RepAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    },
                    "LEIDtls":{
                        "field_optional":[
                            ("LEINumber",str,DataTypeTransformation.str_transform,False,None,None,None),
                            ("ValidUptoDate",str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                        ]
                    }
                },
                "field_required": [
                    ("ItrFilingDueDate",str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("ifMSME", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ResidentialStatus", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("FinancialStmtFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("UnderLiquidation", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("FiiFpiFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("Sec581AFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AsseseeRepFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("StartUpDPIITFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "field_optional": [
                    ("ReceiptNo", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OrigRetFiledDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("UniqueNumNoticeUs", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NoticeDateUnderSec", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("Section115BA", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("Section115BAAY", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ReceiptNo115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("115BAFormFiledDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("Section115CurrAY", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("SectionCurrAY", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Section115CurrAYDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("Section115CurrAYRecNo", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("GrossReceipt", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ResidentSec90", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("NRI_PE", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("NriSEPinIndia", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AggrPaymentTransac", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NumberOfUsers", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RegistratedLaw", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ActDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ActRegNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ActRegDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("IsIfsc", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("SebiRegnNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("RecgnNumAllottedByDPIIT", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("InterMinisterialCertFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("CertificationNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Form2AccordPara5DPIITFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateOfFilingForm2", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("RegNumMSMEDAct2006",str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Cndnfor44AB",str, DataTypeTransformation.str_transform, False, str.lower, None, None),
                ]
            }
        }
    },
    "PartA_GEN2For6": {
        "node_required": {
            "HoldingStatus": {
                "array_optional": {
                    "HoldingCompDetail": {
                        "node_optional": {
                            "CompDetails": {
                                "node_optional": {
                                    "AddressDetailWithZipCode": {
                                        "field_optional": [
                                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("CompName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CompPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                    ("CompSharePercent", int, DataTypeTransformation.float_transformation_without_roundof, False, None, None, None),
                                ]
                            }
                        }
                    },
                    "SubsidiaryCompDetail": {
                        "node_optional": {
                            "CompDetails": {
                                "node_optional": {
                                    "AddressDetailWithZipCode": {
                                        "field_optional": [
                                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("CompName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CompPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                    ("CompSharePercent", int, DataTypeTransformation.float_transformation_without_roundof, False, None, None, None),
                                ]
                            }
                        }
                    }
                },
                "field_required": [
                    ("NatOfCompFlg", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
            },
            "NatureOfComp": {
                "field_required": [
                    ("PubSectCompUs2_36AFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("RBICompFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("CompLes40PercSharGovRBIFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("BankCompUs5Flg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("SchedBankOfRBIActFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("CompWithIRDARegisterFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("NonBankFIICompFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("CompanyUnlistedFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
            }
        },
        "node_optional": {
            "AuditInfo": {
                "field_optional": [
                    ("AuditReportFurnishDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("AuditorName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AuditorMemNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AudFrmName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AudFrmRegNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AudFrmPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AudFrmAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AuditDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("AckNum44AB",int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UDIN", str, DataTypeTransformation.str_transform, False, None, None, None),

                ]
            },
            "AuditDetails92E": {
                "field_optional": [
                    ("DateOfAudit", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("AckNum92E",int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "NatOfBus": {
                "array_optional": {
                    "NatureOfBusiness": {
                        "field_optional": [
                            ("Code", str, DataTypeTransformation.zipcode_transform, False, None, None, None),
                            ("TradeName1", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("Description", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
            }
        },
        "field_required": [
            ("LiableSec44AAflg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("IncDclrdUs", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("LiableSec44ABflg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("LiableSec92Eflg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
        ],
        "field_optional": [
            ("TotalSalesExcOneCr", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("AgrOFAllAmtsRcvd", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("AgrOFAllPayMade", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("AuditedByAccountantFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("AccountAuditFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
        ],
        "array_optional": {
            "AuditDetails": {
                "field_optional": [
                    ("AuditedSection", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AnyOtherSection", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AuditFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateOfAudit", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("AckNumOth", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "field_required": [
                    ("AuditedSection", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ],
            },
            "AuditReportDetails": {
                "field_optional": [
                    ("AuditReportAct", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AuditReportActOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AuditReportSection", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("OtherITActFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AuditReportDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                ]
            },
            "BusOrganisation": {
                "node_optional": {
                    "AddressDetailWithZipCode": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("BusOrgType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("CompName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("BusOrgPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateOfBusinessOrg", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                ]
            },
            "KeyPersons": {
                "node_optional": {
                    "AddressDetailWithZipCode": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("PersonName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Designation", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("KeyPerPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("KeyPersnAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("DirectorIdNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
            },
            "ShareHolderInfo": {
                "node_optional": {
                    "AddressDetailWithZipCode": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("ShareHolderInfoName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("PercentageOfShare", int, DataTypeTransformation.float_transformation_without_roundof, False, None, None, None),
                    ("ShareHolderPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ShareHolderAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("PercentageOfShare", int, DataTypeTransformation.float_transformation_without_roundof, True, None, None, None),
                ]
            },
            "OwnershipInfo": {
                "node_optional": {
                    "AddressDetailWithZipCode": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("OwnerName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("PercentageOfShare", int, DataTypeTransformation.float_transformation_without_roundof, False, None, None, None),
                    ("OwnerPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("OwnerAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("PercentageOfShare", int, DataTypeTransformation.float_transformation_without_roundof, True, None, None, None),
                ]
            },
            "FrnCompImmediatePrntCompDtls": {
                "node_optional": {
                    "AddressDetailWithZipCode": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("Name", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("TaxpayerRegNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryOfResidence", str, DataTypeTransformation.str_transform, False, None, None, None),
                ]
            },
            "FrnCompUltimatePrntCompDtls": {
                "node_optional": {
                    "AddressDetailWithZipCode": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("Name", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("TaxpayerRegNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryOfResidence", str, DataTypeTransformation.str_transform, False, None, None, None),
                ]
            }
        }
    },
    "PARTA_BSFor6FrmAY13": {
        "node_required": {
            "EquityAndLiablities": {
                "node_required": {
                    "ShareHolderFund": {
                        "node_required": {
                            "ShareCapital": {
                                "field_required": [
                                    ("Authorised", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("IssuedSubsPaidUp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SubscribedNotFullyPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotShareCapital", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "ResrNSurp": {
                                "field_required": [
                                    ("CapResr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapRedempResr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SecurPremResr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DebunRedResr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RevResr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ShareOptOSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OtherResrvTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PLAccount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotResrNSurp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_optional": {
                                    "OtherResrvDtls": {
                                        "field_optional": [
                                            ("Nature", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "array_optional": []
                                    }
                                }
                            }
                        },
                        "field_required": [
                            ("MoneyRecvdAgainstShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotShareHolderFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "ShareAppMoneyAllot": {
                        "field_required": [
                            ("PendingLtOneYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PendingMtOneYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "NonCurrLiabilities": {
                        "node_required": {
                            "LongTermBorrowings": {
                                "node_required": {
                                    "BondsDebentures": {
                                        "field_required": [
                                            ("ForeignCurrency", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Rupee", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    },
                                    "TermLoans": {
                                        "node_required": {
                                            "RupeeLoans": {
                                                "field_required": [
                                                    ("FromBanks", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("FromOthers", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                            }
                                        },
                                        "field_required": [
                                            ("ForeignCurrency", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalTermLoans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("DeferredPymtLiabilities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepositsFrmRelatedParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OtherDeposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LoansAndAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthersLoanAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LongTermMaturities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalLTBorrowings", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "OthLongTermLiablities": {
                                "field_required": [
                                    ("TradePayables", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalOthLtLiabilities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LongTermProvisions": {
                                "field_required": [
                                    ("ProvEmpBenefits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("NetDefferedTaxLiability", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalNonCurrLiabilites", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "CurrentLiabilities": {
                        "node_required": {
                            "ShortTrmBorrowings": {
                                "node_required": {
                                    "LoansRepaybleOnDemand": {
                                        "field_required": [
                                            ("FromBanks", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FrmNonBanking", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("OthFinanceInst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotLoansRepaybleOnDemand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("DepositsFrmRelatedParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LoansAndAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthLoansAndAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthDeposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotShortTrmBorrowings", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "TradePayables": {
                                "field_required": [
                                    ("OSMoreThanOneYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalTradePayables", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "OthCurrLiabilities": {
                                "field_required": [
                                    ("CurrMatOnLTDebt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrMatFinanceOblg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AccrInterestNotDue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AccrInterest", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("IncRecvdAdvance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("UnpaidDividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AppMonyRecvdAllotSecurities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("UnpaidMatDeposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("UnpaidMatureDebenture", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthPayables", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotOthCurrLiabilities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "ShortTermProv": {
                                "field_required": [
                                    ("EmpBenefitProv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ITProvision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProposedDividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TaxOnDividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthProvision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotShortTermProvisions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("TotCurrLiabilitiesProvision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
                "field_required": [
                    ("TotEquityAndLiabilities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "Assets": {
                "node_required": {
                    "NonCurrAssets": {
                        "node_required": {
                            "FixedAsset": {
                                "node_required": {
                                    "Tangible": {
                                        "field_required": [
                                            ("GrossBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Depreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImpairmentLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("NetBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    },
                                    "InTangible": {
                                        "field_required": [
                                            ("GrossBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Amortization", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImpairmentLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("NetBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("CapWrkProg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("IntangibleAssetUnDev", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotFixedAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "NonCurrInvstmnts": {
                                "node_required": {
                                    "EquityInstruments": {
                                        "field_required": [
                                            ("ListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("UnListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("InvInProperty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PreferenceShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("GovtOrTrustSecurities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DebenturesOrBonds", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("MutualFunds", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InvstmntInPrtnrShipFirm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OtherInvstmnts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotNonCurrInvstmnts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LongTrmLoanAdv": {
                                "node_required": {
                                    "LTLoanAdvDtls": {
                                        "field_required": [
                                            ("BusOrProf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("NotForBusOrProf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ShareHolderUs2_22", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("CapitalAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SecurityDeposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LoanAdvRelatedParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthLoanAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotLTLoanAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "OthNonCurrAssets": {
                                "node_required": {
                                    "LTTradeReceivables": {
                                        "field_required": [
                                            ("Secured", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Unsecured", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Doubtful", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotOthNonCurrAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NonCurrAssetUs2_22", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("NetDeferredTaxAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotNonCurrAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "CurrentAssets": {
                        "node_required": {
                            "CurrInvstmnts": {
                                "node_required": {
                                    "EquityInstruments": {
                                        "field_required": [
                                            ("ListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("UnListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("PreferenceShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("GovtOrTrustSecurities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DebenturesOrBonds", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("MutualFunds", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InvstmntInPrtnrShipFirm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OtherInvstmnts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotCurrInvstmnts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "Inventories": {
                                "field_required": [
                                    ("RawMatl", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WorkInProgress", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FinOrTradGood", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("StkInTrade", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("StoresConsumables", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LooseTools", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotInventries", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "TradeReceivables": {
                                "field_required": [
                                    ("OSMoreThanSixMonths", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalTradeReceivables", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "CashNCashEquivalents": {
                                "field_required": [
                                    ("BalWithBanks", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ChequesDrafts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CashInHand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotCashNCashEquivalents", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "TotShortTermLoanAdv": {
                                "node_required": {
                                    "STLoanAdvDtls": {
                                        "field_required": [
                                            ("BusOrProf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("NotForBusOrProf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ShareHolderUs2_22", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("LoanAdv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotShrtTermLoans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("OtherCurrAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotCurrAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            },
        },
        "field_required": [
            ("TotalAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
    },
    "PARTA_BSIndAS": {
        "node_required": {
            "EquityAndLiablities": {
                "node_required": {
                    "Equity": {
                        "node_required": {
                            "EquityShareCapital": {
                                "field_required": [
                                    ("Authorised", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("IssuedSubsPaidUp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SubscribedNotFullyPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotShareCapital", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Authorised", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "OtherEquityReserv": {
                                "field_required": [
                                    ("CapRedempResr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DebunRedResr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ShareOptOSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthersTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalOtherResrv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RetainedEarngs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotResrNRetEar", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalEquity", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_optional": {
                                    "OtherResrvDtls": {
                                        "field_optional": [
                                            ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),\
                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        },
                    },
                    "Liabilities": {
                        "node_required": {
                            "NonCurrLiabilities": {
                                "node_required": {
                                    "FinancialLiabilities": {
                                        "node_required": {
                                            "BondsDebentures": {
                                                "field_required": [
                                                    ("ForeignCurrency", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("Rupee", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                            },
                                            "TermLoans": {
                                                "node_required": {
                                                    "RupeeLoans": {
                                                        "field_required": [
                                                            ("FromBanks", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                            ("FromOthers", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                        ],
                                                    }
                                                },
                                                "field_required": [
                                                    ("ForeignCurrency", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalTermLoans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                            }
                                        },
                                        "field_required": [
                                            ("DeferredPymtLiabilities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Deposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LoansReltdParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LongTermMaturities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LiabilityComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("OtherLoans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalLTBorrowings", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TradePayables", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("OtherFinancialLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    },
                                    "Provisions": {
                                        "field_required": [
                                            ("ProvEmpBenefits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalProvisions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OthersProvisions": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                    "OtherNonCurLiabilites": {
                                        "field_required": [
                                            ("Advances", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalOthNonCurrLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OthersNonCurrLiab": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                },
                                "field_required": [
                                    ("DefrdTaxCurrLiabilites", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalNonCurrLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "CurrentLiabilities": {
                                "node_required": {
                                    "FinancialLiabBorrowings": {
                                        "node_required": {
                                            "LoansRepaybleOnDemand": {
                                                "field_required": [
                                                    ("FromBanks", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("FrmOtherParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotLoansRepaybleOnDemand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                            }
                                        },
                                        "field_required": [
                                            ("LoansFrmRelatedParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Deposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalBorrowings", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TradePayables", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "BrwngOtherLoans": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                    "OthFinancialLiabilities": {
                                        "field_required": [
                                            ("CurrMatOnLTDebt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("CurrMatFinanceOblg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AccrInterest", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("UnpaidDividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AppMonyRecvdAllotSecurities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("UnpaidMatDeposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("UnpaidMatureDebenture", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotOthFinancialLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OthPayables": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                    "OtherCuurLiabilities": {
                                        "field_required": [
                                            ("RevenueRecvdAdvance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("OthersAdvTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalOthCurrLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OtherAdvance": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            },
                                            "Others": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                    "Provosions": {
                                        "field_required": [
                                            ("ProvosionEmpBenft", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalProvosions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OthersProvisions": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                },
                                "field_required": [
                                    ("TottalFinancialLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrTaxLiabilities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalCurrentLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalEquityLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                        },
                    },
                },
            },
            "Assets": {
                "node_required": {
                    "NonCurrAssets": {
                        "node_required": {
                            "PropertyPlantEquip": {
                                "node_required": {
                                    "FinancialAssets": {
                                        "node_required": {
                                            "Investments": {
                                                "field_required": [
                                                    ("ListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("UnListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("InvstPrfShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("InvstGovtTrust", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("InvstInDebenture", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("InvstInMutualFunds", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("InvstInPartnershpFirm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalNonCurrentInvst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "field_optional": [
                                                    ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "array_optional": {
                                                    "OtherInvestment": {
                                                        "field_optional": [
                                                            ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                        ],
                                                        "cm_field_map": [
                                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                        ],
                                                        "array_optional": []
                                                    }
                                                }
                                            },
                                            "TradeReceivables": {
                                                "field_required": [
                                                    ("SecuredConsGoods", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("UnSecuredConsGoods", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("Doubtful", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalTradeReceivbls", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                            },
                                            "Loans": {
                                                "field_required": [
                                                    ("SecurityDepsts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("LoansRltdParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalLoans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("LoansBPPurpose", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("LoansNotBPPurpose", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("LoansToShrHolders", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "field_optional": [
                                                    ("OthersTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": {
                                                    "OtherLoans": {
                                                        "field_optional": [
                                                            ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                        ],
                                                        "cm_field_map": [
                                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                        ],
                                                        "array_optional": []
                                                    }
                                                }
                                            },
                                            "OtherFinacialAssets": {
                                                "field_required": [
                                                    ("BankDeposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("OtherDeposits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalOthFinancialAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("DefrdTaxAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                            },
                                            "OtherNonCurrentAssets": {
                                                "field_required": [
                                                    ("CapitalAdvanc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("AdvancOthCapital", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalNonCurrAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("NonCurrAsstDueShrHldr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "field_optional": [
                                                    ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "array_optional": {
                                                    "OtherNonCurrAsst": {
                                                        "field_optional": [
                                                            ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                        ],
                                                        "cm_field_map": [
                                                            ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                        ],
                                                        "array_optional": []
                                                    }
                                                }
                                            }
                                        },
                                        "field_required": [
                                            ("TotalNonCurrntAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_required": [
                                    ("GrossBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Depreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImpairmentLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapWrkProg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InvstPropGrossBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InvstPropDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InvstPropImprLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InvstPropNetBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("GoodWlGrossBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("GoodWlImprLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("GoodWlNetBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthIntAstGrossBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthIntAstAmortisation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthIntAstImprLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthIntAstNetBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("IntAstUndrDevlpmnt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BioAstGrossBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BioAstImprLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BioAstNetBlock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                    },
                    "CurrentAssets": {
                        "node_required": {
                            "Inventories": {
                                "field_required": [
                                    ("RawMaterials", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WorkInProgress", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FinishedGoods", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("StockInTrade", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("StoresSpares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LooseTools", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalInventories", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "FinancialAssets": {
                                "node_required": {
                                    "Investments": {
                                        "field_required": [
                                            ("ListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("UnListedEquities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("InvstPrfShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("InvstGovtTrust", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("InvstInDebenture", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("InvstInMutualFunds", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("InvstInPartnershpFirm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("OtherInvestment", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalCurrentInvst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    },
                                    "TradeReceivables": {
                                        "field_required": [
                                            ("SecuredConsGoods", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("UnSecuredConsGoods", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("Doubtful", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalTradeReceivbls", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    },
                                    "CashEquivalents": {
                                        "field_required": [
                                            ("BalancesWithBanks", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ChequeDraftsInHand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("CashOnHand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalCashEquivalents", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("BankBalanceOther", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OtherCashDtls": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                    "Loans": {
                                        "field_required": [
                                            ("SecurityDepsts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LoansRltdParties", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalLoans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LoansBPPurpose", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LoansNotBPPurpose", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LoansToShrHolders", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OtherLoans": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                    "OtherCurrentAssets": {
                                        "field_required": [
                                            ("AdvancOthCapital", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalOthCurrentAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalCurrAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "array_optional": {
                                            "OthersCurrentAssts": {
                                                "field_optional": [
                                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ],
                                                "array_optional": []
                                            }
                                        }
                                    },
                                },
                                "field_required": [
                                    ("OtherFinancialAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalFinancialAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrentTaxAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                    }
                },
            },
        },
        "field_required": [
            ("TotalAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
    },
    "PARTA_PL": {
        "node_required": {
            "CreditsToPL": {
                "node_required": {
                    "OthIncome": {
                        "field_required": [
                            ("RentInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Comissions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Dividends", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnSaleFixedAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnInvChrSTT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnOthInv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnCurrFluct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnCnvInvntryToCapAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnAgriIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("MiscOthIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotOthIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "field_optional": [
                            ("LiabilityWrittenBack", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OtherIncomeNotTurnover", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                        "cm_field_map": [
                            ("LiabilityWrittenBack", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OtherIncomeNotTurnover", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_optional": {
                            "OtherIncDtls": {
                                "field_optional": [
                                    ("NatureOfIncome", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        }
                    }
                },
                "field_required": [
                    ("TotCreditsToPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "field_optional": [
                    ("GrossProfitTrnsfFrmTrdAcc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
            },
            "DebitsToPL": {
                "node_required": {
                    "DebitPlAcnt": {
                        "node_required": {
                            "EmployeeComp": {
                                "field_required": [
                                    ("SalsWages", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Bonus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("MedExpReimb", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LeaveEncash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LeaveTravelBenft", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToSuperAnnFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToPF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToGratFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToOthFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthEmpBenftExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotEmployeeComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "field_optional": [
                                    ("AnyCompPaidToNonRes", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                    ("AmtPaidToNonRes", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtPaidToNonRes", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "Insurances": {
                                "field_required": [
                                    ("MedInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LifeInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("KeyManInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotInsurances", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "CommissionExpdrDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "RoyalityDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "ProfessionalConstDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "RatesTaxesPays": {
                                "node_required": {
                                    "ExciseCustomsVAT": {
                                        "field_required": [
                                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("VATorSaleTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("Cess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                    }
                                },
                            },
                            "BadDebtDtls": {
                                "field_required": [
                                    ("BadDebtAmtDtlsTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthersPANNotAvlblDtlTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthersAmtLt1Lakh", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BadDebt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_optional": {
                                    "BadDebtAmtDtls": {
                                        "field_optional": [
                                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    },
                                    "OthersPANNotAvlblDtl": {
                                        "field_optional": [
                                            ("Name", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("FlatDoorBlockNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("PremisesBuildingName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("RoadStreetPostOffice", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("AreaLocality", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("TownCityDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                }
                            },
                            "InterestExpdrtDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InterestExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("Freight", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ConsumptionOfStores", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PowerFuel", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RentExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RepairsBldg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RepairMach", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StaffWelfareExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Entertainment", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Hospitality", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Conference", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Hospitality", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SalePromoExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Advertisement", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("HotelBoardLodge", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TravelExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ForeignTravelExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ConveyanceExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TelephoneExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("GuestHouseExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClubExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FestivalCelebExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Scholarship", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Gift", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Donation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AuditFee", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OtherExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProvForBadDoubtDebt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthProvisionsExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PBIDTA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DepreciationAmort", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PBT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_optional": {
                            "OtherExpensesDtls": {
                                "field_optional": [
                                    ("ExpenseNature", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "TaxProvAppr": {
                        "node_required": {
                            "Appropriations": {
                                "field_required": [
                                    ("TrfToReserves", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotAppropriations", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "field_optional": [
                                    ("ProposedDividend", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TaxOnDividend", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AppropriationsCSR", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AnyOtherAppr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("ProvForCurrTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProvDefTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitAfterTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalBFPrevYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmtAvlAppr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PartnerAccBalTrf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            }
        },
        "node_optional": {
            "NoBooksOfAccPL": {
                "field_optional": [
                    ("GrossReceipt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NetProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
            }
        },
        "field_required": [
            ("TotalNumOfMonths", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "field_optional": [
            ("TotalPrsumptvIncUs44EGoods", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalPrsumptvIncUs44E", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "array_optional": {
            "NatOfBus44AE": {
                "field_optional": [
                    ("NameOfBusiness", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CodeAE", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Description", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
            },
            "GoodsDtlsUs44AE": {
                "field_optional": [
                    ("RegNumberGoodsCarriage", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("OwnedLeasedHiredFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("TonnageCapacity", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("HoldingPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PresumptiveIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TonnageCapacity", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("HoldingPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PresumptiveIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "NoBooksOfAccPLDetails": {
                "field_optional": [
                    ("Section", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("GrossReceipt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NetProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
            }
        }
    },
    "PARTA_PLIndAS": {
        "node_required": {
            "CreditsToPL": {
                "node_required": {
                    "OthIncome": {
                        "field_required": [
                            ("RentInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Comissions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Dividends", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnSaleFixedAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnInvChrSTT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnOthInv", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnCurrFluct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnCnvInvntryToCapAsst", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitOnAgriIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("MiscOthIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotOthIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LiabilityWrittenBack", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OtherIncomeNotTurnover", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_optional": {
                            "OtherIncDtls": {
                                "field_optional": [
                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        }
                    }
                },
                "field_required": [
                    ("GrossProfitTrnsfFrmTrdAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotCreditsToPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DebitsToPL": {
                "node_required": {
                    "DebitPlAcnt": {
                        "node_required": {
                            "EmployeeComp": {
                                "field_required": [
                                    ("SalsWages", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Bonus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("MedExpReimb", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LeaveEncash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LeaveTravelBenft", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToSuperAnnFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToPF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToGratFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ContToOthFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthEmpBenftExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotEmployeeComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "field_optional": [
                                    ("AnyCompPaidToNonRes", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("AmtPaidToNonRes", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtPaidToNonRes", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "Insurances": {
                                "field_required": [
                                    ("MedInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LifeInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("KeyManInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthInsur", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotInsurances", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "CommissionExpdrDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "RoyalityDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "ProfessionalConstDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "RatesTaxesPays": {
                                "node_required": {
                                    "ExciseCustomsVAT": {
                                        "field_required": [
                                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "field_optional": [
                                            ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("VATorSaleTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("Cess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                    }
                                },
                            },
                            "BadDebtDtls": {
                                "field_required": [
                                    ("BadDebtAmtDtlsTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthersPANNotAvlblDtlTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("OthersAmtLt1Lakh", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BadDebt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_optional": {
                                    "BadDebtAmtDtls": {
                                        "field_optional": [
                                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                    "OthersPANNotAvlblDtl": {
                                        "field_optional": [
                                            ("Name", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("FlatDoorBlockNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("PremisesBuildingName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("RoadStreetPostOffice", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("AreaLocality", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("TownCityDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            },
                            "InterestExpdrtDtls": {
                                "field_required": [
                                    ("NonResOtherCompany", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("InterestExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("Freight", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ConsumptionOfStores", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PowerFuel", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RentExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RepairsBldg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RepairMach", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StaffWelfareExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Entertainment", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Hospitality", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Conference", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Hospitality", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SalePromoExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Advertisement", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("HotelBoardLodge", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TravelExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ForeignTravelExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ConveyanceExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TelephoneExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("GuestHouseExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClubExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FestivalCelebExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Scholarship", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Gift", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Donation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AuditFee", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OtherExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProvForBadDoubtDebt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthProvisionsExpdr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PBIDTA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DepreciationAmort", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PBT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_optional": {
                            "OtherExpensesDtls": {
                                "field_optional": [
                                    ("ExpenseNature", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        }
                    },
                    "TaxProvAppr": {
                        "node_required": {
                            "Appropriations": {
                                "field_required": [
                                    ("TrfToReserves", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotAppropriations", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "field_optional": [
                                    ("ProposedDividend", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TaxOnDividend", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AppropriationsCSR", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AnyOtherAppr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                            }
                        },
                        "field_required": [
                            ("ProvForCurrTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProvDefTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitAfterTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalBFPrevYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmtAvlAppr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PartnerAccBalTrf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            },
        },
        "node_optional": {
            "OtherComprnsvInc": {
                "node_optional": {
                    "ItemsNotReclsfdPnL": {
                        "field_optional": [
                            ("ChangesInSurplus", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ReMesDefinedBenftPlans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("EquityOCI", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FairValFVTPl", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShareOfOtherComprInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncomeTaxNotPnL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalNotPnL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("ChangesInSurplus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ReMesDefinedBenftPlans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EquityOCI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairValFVTPl", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShareOfOtherComprInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthersTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncomeTaxNotPnL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalNotPnL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_optional": {
                            "OtherIncDtls": {
                                "field_optional": [
                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "ItemsReclsfdPnL": {
                        "field_optional": [
                            ("ExchangeDiff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DebtsOCI", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("EffecPortionGainnLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShareOCI", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthersTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncomeTaxReclsPnL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalPnL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("ExchangeDiff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DebtsOCI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EffecPortionGainnLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShareOCI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthersTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncomeTaxReclsPnL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalPnL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_optional": {
                            "OtherIncDtls": {
                                "field_optional": [
                                    ("OthersDesc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OthersAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    }
                },
                "field_optional": [
                    ("TotalComprIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotalComprIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        },
    },
    "CorpScheduleBP": {
        "node_required": {
            "BusinessIncOthThanSpec": {
                "node_required": {
                    "IncRecCredPLOthHeadDtls": {
                        "field_required": [
                            ("HouseProperty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapitalGains", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OtherSources", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Dividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OtherThanDividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("UnderSec115BBF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("UnderSec115BBG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "ProfitLossInclRefrdSec": {
                        "field_required": [
                            ("ProfitLossUs44AE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitLossUs44B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitLossUs44BB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitLossUs44BBA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitLossUs44BBB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitLossUs44D", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitLossUs44DA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitChapterXIIG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FirstSchITActOthr115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "field_optional": [
                            ("ProfitLossUs44BBC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("ProfitLossUs44BBC", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "ProfitFrmActCvrd": {
                        "field_required": [
                            ("ProfitFrmActCvrdUndrRule7", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitFrmActCvrdUndrRule7A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitFrmActCvrdUndrRule7B1", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitFrmActCvrdUndrRule7B1A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ProfitFrmActCvrdUndrRule8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncCredPL": {
                        "field_required": [
                            ("FirmShareInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AOPBOISharInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthExempInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotExempInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        #new add
                        "node_optional1":{
                            "OtherExmptIncDtl":{
                                "field_required":[
                                      ("OperatingDividendName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                      ("OperatingDividendAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "array_optional": {
                                    "OtherExmptIncDtls": {
                                            "field_required": [
                                                    ("OperatingRevenueName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("OperatingRevenueAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                            ],
                                            "cm_field_map": [
                                                    ("OperatingRevenueAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                            ]
                                    }
                                }
                            }

                        }
                         
                    },
                    "ExpDebToPLOthHeadDtls": {
                        "field_required": [
                            ("HouseProperty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapitalGains", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OtherSources", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("UnderSec115BBF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("UnderSec115BBG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DepreciationAllowITAct32": {
                        "field_required": [
                            ("DepreciationAllowUs32_1_ii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DepreciationAllowUs32_1_i", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotDeprAllowITAct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DeemedProfitBusUs": {
                        "field_required": [
                            ("Section44AE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Section44B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Section44BB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Section44BBA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Section44BBB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Section44D", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Section44DA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ChapterXIIG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FirstSchTActOther", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotDeemedProfitBusUs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "field_optional": [
                            ("Section44BBC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Section44BBC", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "field_required": [
                    ("ProfBfrTaxPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetPLFromSpecBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetProfLossSpecifiedBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PLUs44sChapXIIGOthrUs115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PLUs44sChapXIIGUs115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalProfitFrmActCvrd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalancePLOthThanSpecBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpDebToPLExemptInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpDebToPLExemptIncDisAllwUs14A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotExpDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AdjustedPLOthThanSpecBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DepreciationDebPLCosAct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AdjustPLAfterDeprOthSpecInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDebPLDisallowUs36", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDebPLDisallowUs37", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDebPLDisallowUs40", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDebPLDisallowUs40A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDebPLDisallowUs43B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("InterestDisAllowUs23SMEAct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeemIncUs41", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeemIncUs3380HHD80IA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeemIncUs43CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthItemDisallowUs28To44DA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AnyOthIncNotInclInExpDisallowPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SalaryExpDisallowPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BonusExpDisallowPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CommissionExpDisallowPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("InterestExpDisallowPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthersExpDisallowPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncProfDecLossAccICDSAdj", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAfterAddToPLDeprOthSpecInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeductUs32_1_iii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Amt32AC", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DebPLUs35ExcessAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDisallUs40NowAllow", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDisallUs43BNowAllow", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AnyOthAmtAllDeduct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DecProfIncLossAccICDSAdj", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDeductionAmts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PLAftAdjDedBusOthThanSpec", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetPLAftAdjBusOthThanSpec", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetPLBusOthThanSpec7A7B7C", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ChrgblIncUndrRule7", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeemedChrgblIncUndrRule7A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeemedChrgblIncUndrRule7B1", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeemedChrgblIncUndrRule7B1A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeemedChrgblIncUndrRule8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncomeOtherThanRule", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalIncDeemedFrmAgri", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "field_optional": [
                    ("DeemIncUs32AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs32AC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs33AB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs33ABA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs35ABA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs35ABB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs35AC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs40A3A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs33AC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs72A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs80HHD", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeemIncUs80IA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProfitFrmEligBus10TIA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("ProfitFrmEligBus10TIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "SpecBusinessInc": {
                "field_required": [
                    ("NetPLFrmSpecBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AdditionUs28to44DA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeductUs28to44DA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AdjustedPLFrmSpecuBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "IncSpecifiedBusiness": {
                "field_required": [
                    ("NetPLFrmSpecifiedBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AddSec28to44DA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DedSec28to44DAOTDedSec35AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProfitLossSpecifiedBusiness", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DedSec35AD1", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProfitLossSpecifiedBusFinal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "DedUs35ADSubSec5Dtls": {
                        "field_optional": [
                            ("DedUs35ADSubSec5", str, DataTypeTransformation.str_transform, False, str.lower, None, None),
                        ],
                    }
                }
            },
            "BusSetoffCurrYr": {
                "node_optional": {
                    "SpeculativeInc": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SpecifiedInc": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "ProfGainUs115B": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "IncmForeignCompRule10TIA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "field_required": [
                    ("LossSetOffOnBusLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotLossSetOffOnBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("LossRemainSetOffOnBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "ProfGainUs115B": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SpecifiedInc": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SpeculativeInc": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                }
            }
        },
        "field_required": [
            ("IncChrgUnHdProftGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
    },
    "PartB-TI": {
        "node_required": {
            "DeductionsUndSchVIADtl": {
                "field_required": [
                    ("PartBchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PartCchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDeductUndSchVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        },
        "node_optional": {
            "ProfBusGain": {
                "field_optional": [
                    ("ProfGainNoSpecBus", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncmForeignCompRule10TIA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProfGainSpecBus", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProfGainSpecifiedBus", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncChrgblTaxSplRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotProfBusGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("ProfGainNoSpecBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncmForeignCompRule10TIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProfGainSpecBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProfGainSpecifiedBus", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncChrgblTaxSplRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotProfBusGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "CapGain": {
                "node_optional": {
                    "ShortTerm": {
                        "field_optional": [
                            ("ShortTerm15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShortTerm20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShortTerm30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShortTermAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShortTermSplRateDTAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalShortTerm", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("ShortTerm15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTerm20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTerm30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTermAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTermSplRateDTAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalShortTerm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "LongTerm": {
                        "field_optional": [
                            ("LongTerm10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LongTerm12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LongTerm20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LongTermSplRateDTAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLongTerm", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("LongTerm10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LongTerm12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LongTerm20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LongTermSplRateDTAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLongTerm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "cm_node_map": {
                    "ShortTerm": {
                        "field_optional": [
                            ("ShortTerm15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTerm20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTerm30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTermAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ShortTermSplRateDTAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalShortTerm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "LongTerm": {
                        "field_optional": [
                            ("LongTerm10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LongTerm12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LongTerm20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LongTermSplRateDTAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLongTerm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("TotalCapGains", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ShortTermLongTermTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CapGains30Per115BBH", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
               "cm_field_map": [
                    ("TotalCapGains", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ShortTermLongTermTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CapGains30Per115BBH", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "IncFromOS": {
                "field_optional": [
                    ("OtherSrcThanOwnRaceHorse", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncChargblSplRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FromOwnRaceHorse", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotIncFromOS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("OtherSrcThanOwnRaceHorse", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncChargblSplRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FromOwnRaceHorse", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotIncFromOS", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
        },
        "field_required": [
            ("IncomeFromHP", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalTI", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("CurrentYearLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("BalanceAfterSetoffLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("BroughtFwdLossesSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("GrossTotalIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("IncChargeTaxSplRate111A112", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("DeductionsUnder10Aor10AA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("IncChargeableTaxSplRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("NetAgricultureIncomeOrOtherIncomeForRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("LossesOfCurrentYearCarriedFwd", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("IncChargeableTaxNormalRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "field_optional": [
            ("DeemedTotIncSec115JB", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
    },
    "PartB_TTI": {
        "node_required": {
            "ComputationOfTaxLiability": {
                "node_required": {
                    "TaxPayableOnDeemedTI": {
                        "field_required": [
                            ("TaxDeemedTISec115JB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Surcharge", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EducationCess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "TaxPayableOnTI": {
                        "field_required": [
                            ("TaxAtNormalRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxAtSpecialRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableOnTotInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Surcharge25ofSI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SurchargeOnTaxPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSurcharge", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EducationCess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("GrossTaxLiability", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "TaxRelief": {
                        "field_required": [
                            ("Section90", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Section91", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotTaxRelief", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IntrstPay": {
                        "field_required": [
                            ("IntrstPayUs234A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntrstPayUs234B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntrstPayUs234C", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LateFilingFee234F", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalIntrstPay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
                "field_required": [
                    ("GrossTaxPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetTaxLiability", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AggregateTaxInterestLiability", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "field_optional": [
                    ("CredUs115JAATaxPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TaxPayableAfterCredUs115JAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
            },
            "TaxPaid": {
                "node_required": {
                    "TaxesPaid": {
                        "field_required": [
                            ("TotalTaxesPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "field_optional": [
                            ("AdvanceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TDS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TCS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SelfAssessmentTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
                "field_required": [
                    ("BalTaxPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "field_optional":[
                    ("NetTaxPayable115TD", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TaxPayable115TD", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetRefundAdjust", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]

            },
            "Refund": {
                "node_required": {
                    "BankAccountDtls": {
                        "field_optional": [
                            ("BankDtlsFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "array_optional": {
                            "AddtnlBankDetails": {
                                "field_optional": [
                                    ("IFSCCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                    ("BankName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("BankAccountNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("AccountType", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("UseForRefund", str, DataTypeTransformation.str_transform, False, None, None, None),
                                ],
                                "cm_field_map":[
                                    ("IFSCCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                                    ("BankName", str, DataTypeTransformation.str_transform, True, None, None, None),
                                    ("BankAccountNo", str, DataTypeTransformation.str_transform, True, None, None, None),
                                    ("AccountType", str, DataTypeTransformation.str_transform, True, None, None, None),
                                    ("UseForRefund", str, DataTypeTransformation.str_transform, True, None, None, None),
                                ]
                            },
                            "ForeignBankDetails": {
                                "field_optional": [
                                    ("SWIFTCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("BankName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("IBAN", str, DataTypeTransformation.str_transform, False, None, None, None),
                                ],
                            }
                        },
                    }
                },
                "field_required": [
                    ("RefundDue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        },
        "field_optional": [
            ("AssetOutsideIndiaFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
        ],
    },
    "Verification": {
        "node_required": {
            "Declaration": {
                "field_required": [
                    ("AssesseeVerName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FatherName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Place", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AssesseeVerPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("Capacity", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("Date", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                ],
            }
        },
    },
    "ManufacturingAccount": {
        "node_optional": {
            "OpeningInventory": {
                "field_optional": [
                    ("OpngStckRawMat", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OpngStckWrkinPrgrs", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OpngInvntryTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Purchases", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DirectWages", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DirectExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CarriageInward", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PowerAndFuel", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthDirectExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IndirectWages", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryRentAndRates", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryInsurance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryFuelAndPower", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryGeneralExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeprctnOfFactoryMachinery", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalFactoryOverheads", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalDebtsManfctrngAcc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map":[
                    ("OpngInvntryTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalFactoryOverheads", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalDebtsManfctrngAcc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "ClosingStock": {
                "field_optional": [
                    ("ClsngStckRawMaterial", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ClsngStckWrkInPrgrs", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ClsngStckTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "field_required":[
                    ("ClsngStckTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
        },
        "cm_node_map": {
            "OpeningInventory": {
                "field_optional": [
                    ("OpngStckRawMat", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OpngStckWrkinPrgrs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OpngInvntryTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Purchases", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DirectWages", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CarriageInward", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PowerAndFuel", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthDirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IndirectWages", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryRentAndRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryInsurance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryFuelAndPower", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryGeneralExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeprctnOfFactoryMachinery", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalFactoryOverheads", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalDebtsManfctrngAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "ClosingStock": {
                "field_optional": [
                    ("ClsngStckRawMaterial", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ClsngStckWrkInPrgrs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ClsngStckTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
        },
        "field_required": [
            ("CostOfGoodsPrdcd", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
    },
    "TradingAccount": {
        "node_optional": {
            "ExciseCustomsVAT": {
                "field_optional": [
                    ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("VATorSaleTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
            },
            "DutyTaxPay": {
                "node_optional": {
                    "ExciseCustomsVAT": {
                        "field_optional": [
                            ("CustomDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CounterVailDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SplAddDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("VATorSaleTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "field_required": [
                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            }
        },
        "field_optional": [
            ("SaleOfGoods", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("SaleOfServices", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("GrossRcptFromProfession", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("ClsngStckOfFinishedStcks", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("OpngStckOfFinishedStcks", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Purchases", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None), # ADD True AS per discussion
            ("CarriageInward", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("PowerAndFuel", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotOthDirectExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("GoodsCostPrdcdFrmMA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("IntradayTradingTurnOver", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("IntradayTradingIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "field_required" : [
            ("OperatingRevenueTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("SalesGrossReceiptsTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TardingAccTotCred", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("GrossProfitFrmBusProf", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotRevenueFrmOperations", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "OtherOperatingRevenueDtls": {
                "field_optional": [
                    ("OperatingRevenueName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("OperatingRevenueAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("OperatingRevenueAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "OtherDirectExpenses": {
                "field_optional": [
                    ("NatureOfDirectExpense", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        }
    },
    "ManufacturingAccountIndAS": {
        "node_optional": {
            "OpeningInventory": {
                "field_optional": [
                    ("OpngStckRawMat", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OpngStckWrkinPrgrs", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OpngInvntryTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Purchases", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DirectWages", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DirectExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CarriageInward", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PowerAndFuel", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthDirectExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IndirectWages", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryRentAndRates", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryInsurance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryFuelAndPower", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FactoryGeneralExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeprctnOfFactoryMachinery", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalFactoryOverheads", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalDebtsManfctrngAcc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("OpngInvntryTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalFactoryOverheads", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalDebtsManfctrngAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "ClosingStock": {
                "field_optional": [
                    ("ClsngStckRawMaterial", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ClsngStckWrkInPrgrs", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ClsngStckTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "field_required": [
                    ("ClsngStckTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        },
        "field_required": [
            ("CostOfGoodsPrdcd", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "OpeningInventory": {
                "field_optional": [
                    ("OpngStckRawMat", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OpngStckWrkinPrgrs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Purchases", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DirectWages", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CarriageInward", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PowerAndFuel", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthDirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IndirectWages", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryRentAndRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryInsurance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryFuelAndPower", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FactoryGeneralExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeprctnOfFactoryMachinery", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_field_map": [
                    ("OpngInvntryTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalFactoryOverheads", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalDebtsManfctrngAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "ClosingStock": {
                "field_optional": [
                    ("ClsngStckRawMaterial", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ClsngStckWrkInPrgrs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_field_map": [
                    ("ClsngStckTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            }
        }
    },
    "TradingAccountIndAS": {
        "node_optional": {
            "ExciseCustomsVAT": {
                "field_optional": [
                    ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("VATorSaleTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "DutyTaxPay": {
                "node_optional": {
                    "ExciseCustomsVAT": {
                        "field_optional": [
                            ("CustomDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CounterVailDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SplAddDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("VATorSaleTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            }
        },
        "field_optional": [
            ("SaleOfGoods", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("SaleOfServices", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("OperatingRevenueTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("SalesGrossReceiptsTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("GrossRcptFromProfession", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotRevenueFrmOperations", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("ClsngStckOfFinishedStcks", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TardingAccTotCred", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("OpngStckOfFinishedStcks", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Purchases", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DirectExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("CarriageInward", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("PowerAndFuel", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotOthDirectExpenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("GoodsCostPrdcdFrmMA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("GrossProfitFrmBusProf", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("IntradayTradingTurnOver", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("IntradayTradingIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("GrossRcptFromProfession", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("OpngStckOfFinishedStcks", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Purchases", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("DirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("CarriageInward", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("PowerAndFuel", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotOthDirectExpenses", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("OperatingRevenueTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("SalesGrossReceiptsTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TardingAccTotCred", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("GrossProfitFrmBusProf", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotRevenueFrmOperations", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "ExciseCustomsVAT": {
                "field_optional": [
                    ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "DutyTaxPay": {
                "node_optional": {
                    "ExciseCustomsVAT": {
                        "field_optional": [
                            ("CustomDuty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CounterVailDuty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SplAddDuty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("VATorSaleTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            }
        },
        "array_optional": {
            "OtherOperatingRevenueDtls": {
                "field_optional": [
                    ("OperatingRevenueName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("OperatingRevenueAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("OperatingRevenueAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "OtherDirectExpenses": {
                "field_optional": [
                    ("NatureOfDirectExpense", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        }
    },
    "PARTA_OI": {
        "node_optional": {
            "MethodOfValClgStk": {
                "field_optional": [
                    ("ValRawMaterial", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ValFinishedGoods", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ChngStockValMetFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("EffectOnPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DecProOrIncLossUs145_A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("ChngStockValMetFlg", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                    ("EffectOnPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "NoCredToPLAmt": {
                "field_optional": [
                    ("Section28Items", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProformaCreditsDue", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PrevYrEscalClaim", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthItemInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CapReceipt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotNoCredToPLAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("Section28Items", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProformaCreditsDue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PrevYrEscalClaim", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthItemInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CapReceipt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotNoCredToPLAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "AmtDisallUs36": {
                "node_optional": {
                    "NoOfEmployeesEmployed": {
                        "field_optional": [
                            ("DeployedInIndia", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeployedOutSideIndia", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Total", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DeployedInIndia", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeployedOutSideIndia", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("StkInsurPrem", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("EmpHealthInsurPrem", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("EmpBonusCommSum", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntOnBorrCap", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ZeroCoupBondDisc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("RecogPFContribAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AppSuperAnnFundAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PensionSchemeSec80CCD", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AppGratFundAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthFundAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("EmpContributionCredits", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BadDebtDoubtAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BadDebtDoubtProvn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("SpecResrvTranfr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FamPlanPromoExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("SecuritiesPaidAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("MrktLossOthExpLossICDS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AnyOthDisallowance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotAmtDisallUs36", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("StkInsurPrem", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EmpHealthInsurPrem", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EmpBonusCommSum", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntOnBorrCap", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ZeroCoupBondDisc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RecogPFContribAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AppSuperAnnFundAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PensionSchemeSec80CCD", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AppGratFundAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthFundAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EmpContributionCredits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BadDebtDoubtAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BadDebtDoubtProvn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SpecResrvTranfr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FamPlanPromoExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SecuritiesPaidAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("MrktLossOthExpLossICDS", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AnyOthDisallowance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs36", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "AmtDisallUs37": {
                "field_optional": [
                    ("CapitalNatureExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PersonalExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BusOrProfessnExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PoliticPartyExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("LawVoilatPenalExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthPenalFineExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OffenceExp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("SocialRespCSR", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ContigentLiability", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthAmtNotAllowUs37", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotAmtDisallUs37", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("CapitalNatureExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PersonalExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BusOrProfessnExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PoliticPartyExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("LawVoilatPenalExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthPenalFineExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OffenceExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SocialRespCSR", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ContigentLiability", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthAmtNotAllowUs37", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs37", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "AmtDisallUs40": {
                "field_optional": [
                    ("NonCompChapXVIIBAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NonComp40aiaChapXVIIBAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NonComp40aibChapXVIIBAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NonComp40aiiiChapXVIIBAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TaxAmtOnProfits", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("WTAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("RolyatyOrServiceFee", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntSalBonPartner", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AnyOthDisallowance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotAmtDisallUs40", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AnyAmtOfSec40AllowPrevYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("NonCompChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NonComp40aiaChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NonComp40aibChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NonComp40aiiiChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TaxAmtOnProfits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("WTAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RolyatyOrServiceFee", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntSalBonPartner", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs40", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "AmtDisallUs40A": {
                "field_optional": [
                    ("AmtPaidUs40A2b", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtGT20kCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProvPmtGrat", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ContToSetupTrust", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AnyOthDisallowance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotAmtDisallUs40A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmtPaidUs40A2b", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtGT20kCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProvPmtGrat", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ContToSetupTrust", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs40A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "AmtDisallUs43BPyNowAll": {
                "node_optional": {
                    "AmtUs43B": {
                        "field_optional": [
                            ("TaxDutyCesAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ContToEmpPFSFGF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("EmpBonusComm", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntPayaleToFI", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SumPayaleLoanBrToFinComp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntPayaleToFISchBank", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LeaveEncashPayable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("RailwayAsstsPyble", int, DataTypeTransformation.int_transformation, False, None, None, None),
                           ("TotAmtUs43b", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("MSEPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TaxDutyCesAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ContToEmpPFSFGF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EmpBonusComm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SumPayaleLoanBrToFinComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFISchBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LeaveEncashPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RailwayAsstsPyble", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotAmtUs43b", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "AmtDisall43B": {
                "node_optional": {
                    "AmtUs43B": {
                        "field_optional": [
                            ("TaxDutyCesAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ContToEmpPFSFGF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("EmpBonusComm", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntPayaleToFI", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SumPayaleLoanBrToFinComp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntPayaleToFISchBank", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LeaveEncashPayable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("RailwayAsstsPyble", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("MSEPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotAmtUs43b", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TaxDutyCesAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ContToEmpPFSFGF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EmpBonusComm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SumPayaleLoanBrToFinComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFISchBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LeaveEncashPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RailwayAsstsPyble", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotAmtUs43b", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "AmtExciseCustomsVATOutstanding": {
                "node_optional": {
                    "ExciseCustomsVAT": {
                        "field_optional": [
                            ("UnionExciseDuty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("VATorSaleTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CentralGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StateGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntegratedGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("UnionTerrGoodServiceTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthDutyTaxCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            }
        },
        "field_optional": [
            ("MethodOfAcct", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("ChangeInAcctMethFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("ProfDeviatDueAcctMeth", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DecProOrIncLossUs145_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DeemedProfUs33ABs", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DeemedProfUs33AB", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DeemedProfUs33ABA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DeemedProfUs33AC", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("ProfTaxAmtUs41", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("PriorAmtIncCrDrPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AmountOfExpDisAllwUs14A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("ScheduleTPSAFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
        ],
        "cm_field_map": [
            ("MethodOfAcct", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("ChangeInAcctMethFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("ProfDeviatDueAcctMeth", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("DecProOrIncLossUs145_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("DeemedProfUs33ABs", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("ProfTaxAmtUs41", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("PriorAmtIncCrDrPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("AmountOfExpDisAllwUs14A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("ScheduleTPSAFlg", str, DataTypeTransformation.str_transform, False, None, None, None),
        ],
        "cm_node_map": {
            "NoCredToPLAmt": {
                "field_optional": [
                    ("Section28Items", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProformaCreditsDue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PrevYrEscalClaim", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthItemInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CapReceipt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotNoCredToPLAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "AmtDisallUs37": {
                "field_optional": [
                    ("CapitalNatureExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PersonalExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BusOrProfessnExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PoliticPartyExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("LawVoilatPenalExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthPenalFineExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OffenceExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SocialRespCSR", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ContigentLiability", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthAmtNotAllowUs37", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs37", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "AmtDisallUs40": {
                "field_optional": [
                    ("NonCompChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NonComp40aiaChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NonComp40aibChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NonComp40aiiiChapXVIIBAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TaxAmtOnProfits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("WTAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RolyatyOrServiceFee", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntSalBonPartner", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs40", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "AmtDisallUs40A": {
                "field_optional": [
                    ("AmtPaidUs40A2b", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtGT20kCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProvPmtGrat", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ContToSetupTrust", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs40A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "AmtDisallUs43BPyNowAll": {
                "node_optional": {
                    "AmtUs43B": {
                        "field_optional": [
                            ("TaxDutyCesAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ContToEmpPFSFGF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EmpBonusComm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SumPayaleLoanBrToFinComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFISchBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LeaveEncashPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RailwayAsstsPyble", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotAmtUs43b", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("MSEPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "AmtDisall43B": {
                "node_optional": {
                    "AmtUs43B": {
                        "field_optional": [
                            ("TaxDutyCesAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ContToEmpPFSFGF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EmpBonusComm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFI", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SumPayaleLoanBrToFinComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntPayaleToFISchBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LeaveEncashPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RailwayAsstsPyble", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotAmtUs43b", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("MSEPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),

                        ]
                    }
                },
            },
            "AmtExciseCustomsVATOutstanding": {
                "node_optional": {
                    "ExciseCustomsVAT": {
                        "field_optional": [
                            ("TotExciseCustomsVAT", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "AmtDisallUs36": {
                "field_optional": [
                    ("StkInsurPrem", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EmpHealthInsurPrem", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EmpBonusCommSum", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntOnBorrCap", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ZeroCoupBondDisc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RecogPFContribAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AppSuperAnnFundAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PensionSchemeSec80CCD", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AppGratFundAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthFundAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EmpContributionCredits", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BadDebtDoubtAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BadDebtDoubtProvn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SpecResrvTranfr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FamPlanPromoExp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SecuritiesPaidAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("MrktLossOthExpLossICDS", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AnyOthDisallowance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAmtDisallUs36", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
        }
    },
    "PARTA_QD": {
        "node_optional": {
            "TradingConcern": {
                "array_optional": {
                    "QuantitDet": {
                        "field_optional": [
                            ("ItemName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("UnitOfMeasure", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("OpeningStock", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("PurchaseQty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SaleQty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClgStock", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AnyShortExces", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpeningStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("PurchaseQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SaleQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClgStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AnyShortExces", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                }
            },
            "ManfactrConcern": {
                "node_optional": {
                    "RawMaterial": {
                        "array_optional": {
                            "QuantitDet": {
                                "field_optional": [
                                    ("ItemName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("UnitOfMeasure", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OpeningStock", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PurchaseQty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PrevYrConsum", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("SaleQty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ClgStock", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("yldFinisProd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PercentYld", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AnyShortExces", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OpeningStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PurchaseQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SaleQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ClgStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AnyShortExces", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "FinishrByProd": {
                        "array_optional": {
                            "QuantitDet": {
                                "field_optional": [
                                    ("ItemName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("UnitOfMeasure", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OpeningStock", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PurchaseQty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PrevyrManfact", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("SaleQty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ClgStock", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AnyShortExces", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OpeningStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PurchaseQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SaleQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ClgStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AnyShortExces", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    }
                },
                "cm_node_map": {
                    "RawMaterial": {
                        "array_optional": {
                            "QuantitDet": {
                                "field_optional": [
                                    ("OpeningStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PurchaseQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SaleQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ClgStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AnyShortExces", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "FinishrByProd": {
                        "array_optional": {
                            "QuantitDet": {
                                "field_optional": [
                                    ("OpeningStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PurchaseQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SaleQty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ClgStock", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AnyShortExces", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    }
                }
            }
        },
    },
    "PARTA_OL": {
        "node_optional": {
            "OpeningBal": {
                "field_optional": [
                    ("CashInHand", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CashInBank", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalOpenBal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("CashInHand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CashInBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalOpenBal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "Receipts": {
                "node_optional": {
                    "SaleOfAssets": {
                        "array_optional": {
                            "SaleOfAssetsDtls": {
                                "field_optional": [
                                    ("OthNatOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "OthersIncRec": {
                        "array_optional": {
                            "OthersIncDtls": {
                                "field_optional": [
                                    ("OthNatOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("TypeOfIncome", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    }
                },
                "field_optional": [
                    ("Interest", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Dividend", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalSaleofAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("RlznDuesDebtors", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotOthersReceiptsOnly", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalOfReceipts", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("Interest", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Dividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalSaleofAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RlznDuesDebtors", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotOthersReceiptsOnly", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalOfReceipts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "Payments": {
                "node_optional": {
                    "OthersPayments": {
                        "array_optional": {
                            "OthersPaymentsDtls": {
                                "field_optional": [
                                    ("OthNatOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    }
                },
                "field_optional": [
                    ("RepaymentSecuredloan", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("RepaymentUnsecuredloan", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("RepaymentCreditors", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Commission", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalOthersPayments", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalPayments", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("RepaymentSecuredloan", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RepaymentUnsecuredloan", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RepaymentCreditors", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Commission", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalOthersPayments", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalPayments", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "ClosingStock": {
                "field_optional": [
                    ("CashInHand", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CashInBank", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalClBal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("CashInHand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CashInBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalClBal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        },
        "field_optional": [
            ("TotalOpenReceipts", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalClPaymnts", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalOpenReceipts", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalClPaymnts", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "OpeningBal": {
                "field_optional": [
                    ("CashInHand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CashInBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalOpenBal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "Receipts": {
                "field_optional": [
                    ("Interest", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Dividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalSaleofAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RlznDuesDebtors", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotOthersReceiptsOnly", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalOfReceipts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "Payments": {
                "field_optional": [
                    ("RepaymentSecuredloan", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RepaymentUnsecuredloan", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RepaymentCreditors", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Commission", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalOthersPayments", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalPayments", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "ClosingStock": {
                "field_optional": [
                    ("CashInHand", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CashInBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalClBal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        }
    },
    "ScheduleHP": {
        "field_optional": [
            ("PassThroghIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalIncomeChargeableUnHP", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalIncomeChargeableUnHP", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "PropertyDetails": {
                "node_optional": {
                    "AddressDetailWithZipCode": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ]
                    },
                    "Rentdetails": {
                        "field_optional": [
                            ("AnnualLetableValue", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("RentNotRealized", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LocalTaxes", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalUnrealizedAndTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BalanceALV", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AnnualOfPropOwned", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ThirtyPercentOfBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntOnBorwCap", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalDeduct", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ArrearsUnrealizedRentRcvd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncomeOfHP", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AnnualLetableValue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RentNotRealized", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LocalTaxes", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalUnrealizedAndTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceALV", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AnnualOfPropOwned", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ThirtyPercentOfBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntOnBorwCap", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalDeduct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ArrearsUnrealizedRentRcvd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncomeOfHP", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "node_optional": {
                            "Section24B": {
                                "array_optional": {
                                    "Section24BDtls": {
                                        "field_optional": [
                                            ("LoanTknFrom", int, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("BankOrInstnName", int, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("LoanAccNoOfBankOrInstnRefNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("DateofLoan", int, DataTypeTransformation.date_transform, False, None, None, None),
                                            ("TotalLoanAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("LoanOutstndngAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("InterestUs24B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("LoanTknFrom", int, DataTypeTransformation.str_transform, True, None, None, None),
                                            ("BankOrInstnName", int, DataTypeTransformation.str_transform, True, None, None, None),
                                            ("LoanAccNoOfBankOrInstnRefNo", str, DataTypeTransformation.str_transform, True, None, None, None),
                                            ("DateofLoan", int, DataTypeTransformation.date_transform, True, None, None, None),
                                            ("TotalLoanAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LoanOutstndngAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("InterestUs24B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("TotalInterestUs24B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("TotalInterestUs24B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                        },
                    }
                },
                "cm_node_map": {
                    "Rentdetails": {
                        "field_optional": [
                            ("AnnualLetableValue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("RentNotRealized", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LocalTaxes", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalUnrealizedAndTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceALV", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AnnualOfPropOwned", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ThirtyPercentOfBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IntOnBorwCap", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalDeduct", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ArrearsUnrealizedRentRcvd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncomeOfHP", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "node_optional": {
                            "Section24B": {
                                "array_optional": {
                                    "Section24BDtls": {
                                        "field_optional": [
                                            ("LoanTknFrom", int, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("BankOrInstnName", int, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("LoanAccNoOfBankOrInstnRefNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("DateofLoan", int, DataTypeTransformation.date_transform, False, None, None, None),
                                            ("TotalLoanAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("LoanOutstndngAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("InterestUs24B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("LoanTknFrom", int, DataTypeTransformation.str_transform, True, None, None, None),
                                            ("BankOrInstnName", int, DataTypeTransformation.str_transform, True, None, None, None),
                                            ("LoanAccNoOfBankOrInstnRefNo", str, DataTypeTransformation.str_transform, True, None, None, None),
                                            ("DateofLoan", int, DataTypeTransformation.date_transform, True, None, None, None),
                                            ("TotalLoanAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("LoanOutstndngAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("InterestUs24B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("TotalInterestUs24B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("TotalInterestUs24B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                        },
                    }
                },
                "field_optional": [
                    ("HPSNo", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PropertyOwner", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("PropCoOwnedFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AssessePercentShareProp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ifLetOut", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("HPSNo", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AssessePercentShareProp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "array_optional": {
                    "CoOwners": {
                        "field_optional": [
                            ("CoOwnersSNo", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NameCoOwner", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN_CoOwner", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Aadhaar_CoOwner", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PercentShareProperty", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CoOwnersSNo", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "TenantDetails": {
                        "field_optional": [
                            ("TenantSNo", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NameofTenant", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PANofTenant", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("AadhaarofTenant", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PANTANofTenant", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("TenantSNo", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                }
            }
        }
    },
    "ScheduleDPM": {
        "node_optional": {
            "PlantMachinery": {
                "node_optional": {
                    "Rate15": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprOnGT180DayAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprDuringYearAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprOnLessThan180DayAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Rate30": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprOnGT180DayAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprDuringYearAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprOnLessThan180DayAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Rate40": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprOnGT180DayAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprDuringYearAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AddlnDeprOnLessThan180DayAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Rate45": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
            }
        }
    },
    "ScheduleDOA": {
        "node_optional": {
            "Land": {
                "node_optional": {
                    "DepreciationDetail": {
                        "field_optional": [
                            ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "Building": {
                "node_optional": {
                    "Rate5": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Rate10": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Rate40": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
            },
            "FurnitureFittings": {
                "node_optional": {
                    "Rate10": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                },
            },
            "IntangibleAssets": {
                "node_optional": {
                    "Rate25": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
            },
            "Ships": {
                "node_optional": {
                    "Rate20": {
                        "node_optional": {
                            "DepreciationDetail": {
                                "field_optional": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("WDVFirstDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsGrThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationTotalPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AdditionsLessThan180Days", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RealizationPeriodDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("HalfRateDeprAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtFullRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepreciationAtHalfRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DepDisAllowUs38_2", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetAggregateDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ProportionateAggDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpdrOnTrforSaleAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapGainUs50", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("WDVLastDay", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
            }
        },
    },
    "ScheduleDEP": {
        "node_optional": {
            "SummaryFromDeprSch": {
                "node_optional": {
                    "PlantMachinerySummary": {
                        "field_optional": [
                            ("DeprBlockTot15Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot30Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot40Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot45Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotPlntMach", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DeprBlockTot15Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeprBlockTot30Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeprBlockTot40Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeprBlockTot45Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotPlntMach", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "BuildingSummary": {
                        "field_optional": [
                            ("DeprBlockTot5Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot10Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot40Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotBuildng", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DeprBlockTot5Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeprBlockTot10Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeprBlockTot40Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotBuildng", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("FurnitureSummary", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntangibleAssetSummary", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ShipsSummary", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        },
    },
    "ScheduleDCG": {
        "node_optional": {
            "SummaryFromDeprSchCG": {
                "node_optional": {
                    "PlantMachinerySummaryCG": {
                        "field_optional": [
                            ("DeprBlockTot15Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot30Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot40Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot45Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotPlntMach", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    },
                    "BuildingSummaryCG": {
                        "field_optional": [
                            ("DeprBlockTot5Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot10Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeprBlockTot40Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotBuildng", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
                "field_optional": [
                    ("FurnitureSummary", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntangibleAssetSummary", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ShipsSummary", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotalDepreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        },
    },
    "ScheduleESR": {
        "node_optional": {
            "DeductionUs35": {
                "node_optional": {
                    "Section35_1_i": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_ii": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_iia": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_iii": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_iv": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_2AA": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_2AB": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_CCC": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_CCD": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "TotUs35": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
                "cm_node_map": {
                    "Section35_1_i": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_ii": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_iia": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_iii": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_1_iv": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_2AA": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_2AB": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_CCC": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "Section35_CCD": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "TotUs35": {
                        "node_optional": {
                            "DeductUs35": {
                                "field_optional": [
                                    ("AmtDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AmtUs35Allowable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessAmtOverDebPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                }
            }
        },
    },
    "ScheduleCG": {
        "node_optional": {
            "ShortTermCapGain": {
                "node_optional": {
                    "SaleofLandBuild": {
                        "array_optional": {
                            "SaleofLandBuildDtls": {
                                "node_optional": {
                                    "ExemptionOrDednUs54": {
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionSecCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        },
                                    "field_optional": [
                                        ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ],
                                    "cm_field_map": [
                                        ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ]
                                    },
                                    "TrnsfImmblPrprty": {
                                        "array_optional": {
                                            "TrnsfImmblPrprtyDtls": {
                                                "field_optional": [
                                                    ("NameOfBuyer", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("PANofBuyer", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                                    ("AaadhaarOfBuyer", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("PercentageShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("AddressOfProperty", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("PercentageShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                                                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("AddressOfProperty", str, DataTypeTransformation.str_transform, True, None, None, None),
                                                ]
                                            }
                                        }
                                    },
                                },
                                "field_optional": [
                                    ("DateofPurchase", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                                    ("DateofSale", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PropertyValuation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration50C", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Balance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PropertyValuation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration50C", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Balance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "ExemptionOrDednUs54": {
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        }
                                    },
                                }
                            }
                        }
                    },
                    "SlumpSaleInStcg": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRITransacSec48Dtl": {
                        "field_optional": [
                            ("NRItaxSTTPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NRItaxSTTNotPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NRItaxSTTPaidTransferBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NRItaxSTTPaidTransferAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NRItaxSTTPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTNotPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTPaidTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTPaidTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRISecur115AD": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_node_map": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        }
                    },
                    "SaleOnOtherAssets": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "ExemptionOrDednUs54": {
                                "array_optional": {
                                    "ExemptionOrDednUs54Dtls": {
                                        "field_optional": [
                                            ("ExemptionSecCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                            ("ExemptionAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeemedSTCGDeprAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeemedSTCGDeprAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_node_map": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "ExemptionOrDednUs54": {
                                "array_optional": {
                                    "ExemptionOrDednUs54Dtls": {
                                        "field_optional": [
                                            ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "UnutilizedCg": {
                        "array_optional": {
                            "UnutilizedCgPrvYrDtls": {
                                "field_optional": [
                                    ("PrvYrInWhichAsstTrnsfrd", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("SectionClmd", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                    ("YrInWhichAssetAcq", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AmtUtilized", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DateofWithdrawalBE", str, DataTypeTransformation.str_transform, False, None, None, None),                                    
                                    ("AmtUnutilized", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("DateofWithdrawalBE", str, DataTypeTransformation.str_transform, True, None, None, None),
                                    ("AmtUnutilized", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "NRICgDTAA": {
                        "array_optional": {
                            "NRIDTAADtls": {
                                "field_optional": [
                                    ("DTAAamt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ItemNoincl", str, DataTypeTransformation.str_transform, False, str.title, None, None),
                                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("DTAAarticle", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("RateAsPerTreaty", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                    ("TaxRescertifiedFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                    ("SecITAct", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("RateAsPerITAct", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                    ("ApplicableRate", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("DTAAamt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RateAsPerTreaty", float, DataTypeTransformation.float_transformation, True, None, None, None),
                                    ("RateAsPerITAct", float, DataTypeTransformation.float_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "CapitalLossBuyBackShares" :{
                        "array_optional": {
                            "CapitalLossBuyBackSharesDtls": {
                                "field_optional": {
                                    ("Rate", int, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                },
                                "cm_field_map": [
                                    ("Rate", int, DataTypeTransformation.str_transform, True, None, None, None),
                                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_optional": [
                            ("TotalCapitalLossBuyBackShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalCapitalLossBuyBackShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                },
                "array_optional": {
                    "EquityMFonSTT": {
                        "node_optional": {
                            "EquityMFonSTTDtls": {
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            },
                            "EquityMFonSTTDtls_BE": {
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            },
                        },
                        "field_optional": [
                            ("MFSectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("TotalCapGainonassets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("MFSectionCode", str, DataTypeTransformation.str_transform, True, None, None, None),
                            ("TotalCapGainonassets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_node_map": {
                            "EquityMFonSTTDtls": {
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "EquityMFonSTTDtls_BE": {
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                        },
                    },
                },
                "field_optional": [
                    ("UnutilizedStcgFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AmtDeemedStcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtDeemedStcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureSTCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureSTCG15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureSTCG20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureSTCG30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureSTCGAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtNotTaxUsDTAAStcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtTaxUsDTAAStcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalSTCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotalAmtDeemedStcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncNatureSTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtNotTaxUsDTAAStcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtTaxUsDTAAStcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalSTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncNatureSTCG20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "SlumpSaleInStcg": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRITransacSec48Dtl": {
                        "field_optional": [
                            ("NRItaxSTTPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTNotPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTPaidTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTPaidTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRISecur115AD": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SaleOnOtherAssets": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "ExemptionOrDednUs54": {
                                "array_optional": {
                                    "ExemptionOrDednUs54Dtls": {
                                        "field_optional": [
                                            ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeemedSTCGDeprAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                },
            },
            "LongTermCapGain": {
                "node_optional": {
                    "SaleofLandBuild": {
                        "array_optional": {
                            "SaleofLandBuildDtls": {
                                "node_optional": {
                                    "CostOfImprovements": {
                                        "array_required": {
                                            "CostOfImprovementsDtls": {
                                                "field_optional": [
                                                    ("slno", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ImproveDate", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("CostOfImpIndex", int, DataTypeTransformation.int_transformation, False, None, None, None)
                                                ]
                                            },
                                        },
                                        "field_optional": [
                                            ("TotalImprovecost", int, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("TotalindexImprovecost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("TotalImprovecost", int, DataTypeTransformation.str_transform, True, None, None, None),
                                            ("TotalindexImprovecost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                    "ExemptionOrDednUs54": {
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionSecCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        },
                                        "field_optional": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                    "TrnsfImmblPrprty": {
                                        "array_optional": {
                                            "TrnsfImmblPrprtyDtls": {
                                                "field_optional": [
                                                    ("NameOfBuyer", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("PANofBuyer", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                                    ("AaadhaarOfBuyer", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("PercentageShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("AddressOfProperty", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("CountryCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                    ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("PercentageShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                                                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        }
                                    }
                                },
                                "field_optional": [
                                    ("DateofPurchase", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                                    ("DateofSale", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PropertyValuation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration50C", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AquisitCostIndex", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Balance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("PropertyValuation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration50C", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Balance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "ExemptionOrDednUs54": {
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        }
                                    },
                                }
                            },
                        },
                        "field_optional": [
                            ("TotalLTCGImmblPrprty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGImmblPrprtyBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGImmblPrprtyAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalLTCGImmblPrprty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLTCGImmblPrprtyBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLTCGImmblPrprtyAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SlumpSaleInLtcgDtls": {
                        "node_optional": {
                            "SlumpSaleInLtcg_BE": {
                                "field_optional": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "SlumpSaleInLtcg": {
                                "field_optional": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                        },
                        "field_optional": [
                            ("CapgainonAssets_TOTSlump", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CapgainonAssets_TOTSlump", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_node_map": {
                            "SlumpSaleInLtcg_BE": {
                                "field_optional": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "SlumpSaleInLtcg": {
                                "field_optional": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                        }
                    },
                    "SaleofBondsDebntr": {
                        "node_required": {
                            "EquityOrUnitSec54Type": {
                                "field_required": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "node_required": {
                                    "DeductSec48": {
                                        "field_required": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                },
                            },
                        },
                        "field_optional": [
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_node_map": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "Proviso112Applicable": {
                        "node_optional": {
                            "Proviso112Applicabledtls": {
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            },
                            "Proviso112Applicabledtls_BE": {
                                "node_optional": {
                                    "DeductSec48_BE": {
                                        "field_optional": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        },
                        "field_optional": [
                            ("Proviso112SectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_node_map": {
                            "Proviso112Applicabledtls": {
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "Proviso112Applicabledtls_BE": {
                                "node_optional": {
                                    "DeductSec48_BE": {
                                        "field_optional": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        }
                    },
                    "SaleOfEquityShareUs112A": {
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRIProvisoSec48": {
                        "field_optional": [
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LTCGWithoutBenefitTransferBEListDb", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LTCGWithoutBenefitTransferBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LTCGWithoutBenefitTransferAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LTCGWithoutBenefitTransferBEListDb", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LTCGWithoutBenefitTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LTCGWithoutBenefitTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRIOnSec112and115": {
                        "array_optional": {
                            "NRIOnSec112and115Dtls": {
                                "node_optional":{
                                    "NRIOnSec112and115Dtls_BE": {
                                        "field_optional": [
                                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "node_optional": {
                                            "DeductSec48": {
                                                "field_optional": [
                                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        },
                                    },
                                    "NRIOnSec112and115Dtls_AE": {
                                        "field_optional": [
                                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "node_optional": {
                                            "DeductSec48": {
                                                "field_optional": [
                                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        },                                  
                                    },
                                },
                                "field_optional": [
                                    ("SectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("SectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            },
                            "NRIOnSec115ADDtls": {
                            "node_optional": {
                                "DeductSec48": {
                                    "field_optional": [
                                        ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ],
                                    "cm_field_map": [
                                        ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ]
                                }
                            },
                            "field_optional": [
                                ("SectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ],
                            "cm_field_map": [
                                ("SectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ],
                            "cm_node_map": {
                                "DeductSec48": {
                                    "field_optional": [
                                        ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ]
                                }
                            }
                        }
                        },
                        "field_optional": [
                            ("TotalNRIOnSec112and115", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalNRIOnSec112and115", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "NRISaleOfEquityShareUs112A": {
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "SaleofAssetNADtls":{
                        "node_optional": {
                            "SaleofAssetNA_BE":{
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                    "ExemptionOrDednUs54": {
                                        "field_optional": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionSecCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        }
                                    }
                                },
                                "field_optional": [
                                    ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                    "ExemptionOrDednUs54": {
                                        "field_optional": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        }
                                    }
                                }
                            },
                            "SaleofAssetNA": {
                                "node_optional": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                    "ExemptionOrDednUs54": {
                                        "field_optional": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionSecCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                                ],
                                                "cm_field_map": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        }
                                    }
                                },
                                "field_optional": [
                                    ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                    "ExemptionOrDednUs54": {
                                        "field_optional": [
                                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                        "array_optional": {
                                            "ExemptionOrDednUs54Dtls": {
                                                "field_optional": [
                                                    ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                                ]
                                            }
                                        }
                                    }
                                }
                            },
                            "TotalCapgainonAssets": {
                                "field_optional": [
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                        }
                    },
                    "NRICgDTAA": {
                        "array_optional": {
                            "NRIDTAADtls": {
                                "field_optional": [
                                    ("DTAAamt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ItemNoincl", str, DataTypeTransformation.str_transform, False, str.title, None, None),
                                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("DTAAarticle", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("RateAsPerTreaty", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                    ("TaxRescertifiedFlag", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("SecITAct", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("RateAsPerITAct", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                    ("ApplicableRate", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("DTAAamt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("RateAsPerTreaty", float, DataTypeTransformation.float_transformation, True, None, None, None),
                                    ("RateAsPerITAct", float, DataTypeTransformation.float_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "CapitalLossBuyBackShares" :{
                        "array_optional": {
                            "CapitalLossBuyBackSharesDtls": {
                                "field_optional": {
                                    ("Rate", int, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                },
                                "cm_field_map": [
                                    ("Rate", int, DataTypeTransformation.str_transform, True, None, None, None),
                                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_optional": [
                            ("TotalCapitalLossBuyBackShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalCapitalLossBuyBackShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "UnutilizedCg": {
                            "array_optional": {
                                "UnutilizedCgPrvYrDtls": {
                                    "field_optional": [
                                        ("PrvYrInWhichAsstTrnsfrd", str, DataTypeTransformation.str_transform, False, None, None, None),
                                        ("SectionClmd", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                                        ("YrInWhichAssetAcq", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ("AmtUtilized", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ("AmtUnutilized", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ("DateofWithdrawalBE", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ],
                                    "cm_field_map": [
                                        ("AmtUnutilized", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ("DateofWithdrawalBE", str, DataTypeTransformation.str_transform, True, None, None, None),
                                    ]
                                }
                            }
                        },
                },
                "field_optional": [
                    ("UnutilizedLtcgFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AmtDeemedLtcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtDeemedLtcgTransferBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtDeemedLtcgTransferAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtDeemedLtcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtDeemedLtcgTransferBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtDeemedLtcgTransferAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureLTCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureLTCGUs112A12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureLTCGUs112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureLTCG10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureLTCG12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncNatureLTCG20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtNotTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAmtTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalLTCG", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotalAmtDeemedLtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncNatureLTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncNatureLTCGUs112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtNotTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalLTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "SlumpSaleInLtcg": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SaleofBondsDebntr": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_optional": [
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SaleOfEquityShareUs112A": {
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRISaleOfEquityShareUs112A": {
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "SaleofAssetNA": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "ExemptionOrDednUs54": {
                                "field_optional": [
                                    ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_optional": {
                                    "ExemptionOrDednUs54Dtls": {
                                        "field_optional": [
                                            ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SlumpSaleInLtcgDtls": {
                        "node_optional": {
                            "SlumpSaleInLtcg_BE": {
                                "field_optional": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "SlumpSaleInLtcg": {
                                "field_optional": [
                                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                        },
                        "field_optional": [
                            ("CapgainonAssets_TOTSlump", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },  
                },
            },
            "DeducClaimInfo": {
                "field_optional": [
                    ("TotDeductClaim", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotDeductClaim", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "DeducClaimDtlsUs54D": {
                        "field_optional": [
                            ("DateofAcquisition", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("CostofNewLandBuilding", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DateofPurchase", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AmtDeposited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DepositDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AccountNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("IFSC", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "DeducClaimDtlsUs54EC": {
                        "field_optional": [
                            ("DateofTransfer", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AmtInvested", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DateofInvestment", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "DeducClaimDtlsUs54G": {
                        "field_optional": [
                            ("DateofTransfer", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("CostofNewAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DateofPurchase", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AmtDeposited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DepositDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AccountNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("IFSC", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "DeducClaimDtlsUs54GA": {
                        "field_optional": [
                            ("DateofTransfer", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("CostofNewAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DateofPurchase", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AmtDeposited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DepositDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AccountNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("IFSC", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmtDeducted", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                }
            },
            "CurrYrLosses": {
                "node_optional": {
                    "InLossSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg15Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg20Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg30Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcgAppRate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcgDTAARate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg10Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg12_5Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg20Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcgDTAARate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "TotLossSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "LossRemainSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "cm_node_map": {
                    "InLossSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg15Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg20Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg30Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcgAppRate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcgDTAARate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg10Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg12_5Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg20Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcgDTAARate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "TotLossSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "LossRemainSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "AccruOrRecOfCG": {
                "node_optional": {
                    "ShortTermUnder15Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnder20Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnder30Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnderAppRate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnderDTAARate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder10Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder12_5Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder20Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnderDTAARate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "VDATrnsfGainsUnder30Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
                "cm_node_map": {
                    "ShortTermUnder15Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnder20Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnder30Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnderAppRate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnderDTAARate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder10Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder12_5Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder20Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnderDTAARate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "VDATrnsfGainsUnder30Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
            }
        },
        "field_required": [
            ("IncChargeableHeadCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("SumOfCGIncm", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("IncmFromVDATrnsf", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "ShortTermCapGain": {
                "node_optional": {
                    "SlumpSaleInStcg": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRITransacSec48Dtl": {
                        "field_optional": [
                            ("NRItaxSTTPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTNotPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTPaidTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NRItaxSTTPaidTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRISecur115AD": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SaleOnOtherAssets": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "ExemptionOrDednUs54": {
                                "array_optional": {
                                    "ExemptionOrDednUs54Dtls": {
                                        "field_optional": [
                                            ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossSec94of7Or94of8", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeemedSTCGDeprAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                },
                "field_optional": [
                    ("TotalAmtDeemedStcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncNatureSTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtNotTaxUsDTAAStcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtTaxUsDTAAStcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalSTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "LongTermCapGain": {
                "node_optional": {
                    "SlumpSaleInLtcg": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SaleofBondsDebntr": {
                         "node_required": {
                            "EquityOrUnitSec54Type": {
                                "field_required": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "node_required": {
                                    "DeductSec48": {
                                        "field_required": [
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    },
                                },
                            },
                        },
                        "field_optional": [
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SaleOfEquityShareUs112A": {
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "NRISaleOfEquityShareUs112A": {
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "SaleofAssetNA": {
                        "node_optional": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                            "ExemptionOrDednUs54": {
                                "field_optional": [
                                    ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_optional": {
                                    "ExemptionOrDednUs54Dtls": {
                                        "field_optional": [
                                            ("ExemptionAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        },
                        "field_optional": [
                            ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "Proviso112Applicabledtls_BE": {
                        "node_optional": {
                            "EquityOrUnitSec54Type_BE": {
                                "node_optional": {
                                    "DeductSec48_BE": {
                                        "field_optional": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                },
                                "field_optional": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExcessTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_node_map": {
                                    "DeductSec48": {
                                        "field_optional": [
                                            ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ]
                                    }
                                }
                            }
                        }
                    }
                },
                "field_optional": [
                    ("TotalAmtDeemedLtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncNatureLTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncNatureLTCGUs112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtNotTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAmtTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalLTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "CurrYrLosses": {
                "node_optional": {
                    "InLossSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg15Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg20Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcg30Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcgAppRate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InStcgDTAARate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg10Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg12_5Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcg20Per": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "InLtcgDTAARate": {
                        "field_optional": [
                            ("CurrYearIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrCapGain", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "TotLossSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "LossRemainSetOff": {
                        "field_optional": [
                            ("StclSetoff15Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoff30Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("StclSetoffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff10Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff12_5Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOff20Per", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LtclSetOffDTAARate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "AccruOrRecOfCG": {
                "node_optional": {
                    "ShortTermUnder15Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnder20Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnder30Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnderAppRate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "ShortTermUnderDTAARate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder10Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder12_5Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnder20Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "LongTermUnderDTAARate": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    },
                    "VDATrnsfGainsUnder30Per": {
                        "node_optional": {
                            "DateRange": {
                                "field_optional": [
                                    ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                    }
                },
            }
        }
    },
    "LongTermCapGain": {
        "node_optional": {
            "SlumpSaleInLtcg": {
                "field_optional": [
                    ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "SlumpSaleInLtcgDtls": {
                "node_optional": {
                    "SlumpSaleInLtcg_BE": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SlumpSaleInLtcg": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                },
                "field_optional": [
                    ("CapgainonAssets_TOTSlump", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("CapgainonAssets_TOTSlump", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "SlumpSaleInLtcg_BE": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets_BE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "SlumpSaleInLtcg": {
                        "field_optional": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FMV11UAEii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FMV11UAEiii", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetWorthOfDivision", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("SlumpBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DeductionUnderSec54", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                }
            },
            "SaleofBondsDebntr": {
                    "node_required": {
                    "EquityOrUnitSec54Type": {
                        "field_required": [
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "node_required": {
                            "DeductSec48": {
                                "field_required": [
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            },
                        },
                    },
                },
                "field_optional": [
                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "SaleOfEquityShareUs112A": {
                "field_optional": [
                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CapgainonAssetsTransferBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CapgainonAssetsTransferAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "NRISaleOfEquityShareUs112A": {
                "field_optional": [
                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "node_optional": {
                    "CapgainonAssetsTransferBE":{
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "CapgainonAssetsTransferAE": {
                        "field_optional": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                }
            },
            "SaleofAssetNA": {
                "node_optional": {
                    "DeductSec48": {
                        "field_optional": [
                            ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "ExemptionOrDednUs54": {
                        "field_optional": [
                            ("ExemptionGrandTotal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("FullValueConsdRecvUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FairMrktValueUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FullValueConsdSec50CA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FullValueConsdOthUnqshr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalanceCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "Proviso112Applicabledtls_BE": {
                "node_optional": {
                    "EquityOrUnitSec54Type_BE": {
                        "node_optional": {
                            "DeductSec48_BE": {
                                "field_optional": [
                                    ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        },
                        "field_optional": [
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ExcessTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("FullConsideration", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssets", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CapgainonAssetsForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Tax_S1121_20", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Tax_S1121P_10", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ExcessTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_node_map": {
                            "DeductSec48": {
                                "field_optional": [
                                    ("AquisitCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("AquisitCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCostIndexed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ImproveCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("ExpOnTrans", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDedn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TotalDednForExcess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    }
                }
            }
        },
        "field_optional": [
            ("TotalAmtDeemedLtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("PassThrIncNatureLTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("PassThrIncNatureLTCGUs112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalAmtNotTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalAmtTaxUsDTAALtcg", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalLTCG", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ]
    },
    "Schedule112A": {
        "field_optional": [
            ("SaleValue112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("CostAcqWithoutIndx112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AcquisitionCost112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("LTCGBeforelowerB1B2112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("FairMktValueCapAst112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("ExpExclCnctTransfer112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Deductions112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Balance112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Balance112ABE", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Balance112AAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalBalance112A", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("SaleValue112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("CostAcqWithoutIndx112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("AcquisitionCost112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("LTCGBeforelowerB1B2112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("FairMktValueCapAst112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("ExpExclCnctTransfer112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Deductions112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Balance112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Balance112ABE", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Balance112AAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalBalance112A", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "Schedule112ADtls": {
                "field_optional": [
                    ("ShareOnOrBefore", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ShareTransferredOnOrBefore", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ISINCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ShareUnitName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NumSharesUnits", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("SalePricePerShareUnit", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("TotSaleValue", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CostAcqWithoutIndx", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("LTCGBeforelower6and11", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FairMktValuePerShareunit", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("TotFairMktValueCapAst", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ExpExclCnctTransfer", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("TotalDeductions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Balance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotSaleValue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CostAcqWithoutIndx", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AcquisitionCost", float, DataTypeTransformation.float_transformation, True, None, None, None),
                    ("ExpExclCnctTransfer", float, DataTypeTransformation.float_transformation, True, None, None, None),
                    ("TotalDeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Balance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        }
    },
    "Schedule115AD": {
        "field_optional": [
            ("SaleValue115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("CostAcqWithoutIndx115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AcquisitionCost115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("LTCGBeforelowerB1B2115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("FairMktValueCapAst115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("ExpExclCnctTransfer115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Deductions115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Balance115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Balance115ADBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Balance115ADAE", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalBalance115AD", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("SaleValue115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("CostAcqWithoutIndx115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("AcquisitionCost115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("LTCGBeforelowerB1B2115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("FairMktValueCapAst115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("ExpExclCnctTransfer115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Deductions115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Balance115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Balance115ADBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Balance115ADAE", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalBalance115AD", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "Schedule115ADDtls": {
                "field_optional": [
                    ("ShareOnOrBefore", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ShareTransferredOnOrBefore", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ISINCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ShareUnitName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NumSharesUnits", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("SalePricePerShareUnit", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("TotSaleValue", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CostAcqWithoutIndx", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("LTCGBeforelower6and11", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FairMktValuePerShareunit", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("TotFairMktValueCapAst", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ExpExclCnctTransfer", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("TotalDeductions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Balance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotSaleValue", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CostAcqWithoutIndx", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AcquisitionCost", float, DataTypeTransformation.float_transformation, True, None, None, None),
                    ("ExpExclCnctTransfer", float, DataTypeTransformation.float_transformation, True, None, None, None),
                    ("TotalDeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Balance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        }
    },
    "ScheduleVDA":{
        "array_required": {
            "ScheduleVDADtls":{
                "field_required": [
                    ("DateofAcquisition", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("DateofTransfer", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("HeadUndIncTaxed", int, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ConsidReceived", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncomeFromVDA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
            },
            "field_required": [
                    ("TotIncBusiness", int, DataTypeTransformation.str_transform, False, None, None, None),
                    ("TotIncCapGain", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
        },
    },
    "ScheduleOS": {
        "node_optional": {
            "IncOthThanOwnRaceHorse": {
                "node_optional": {
                    "OthersInc": {
                        "array_optional": {
                            "OthersIncDtls": {
                                "field_optional": [
                                    ("OthNatOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("OthAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ]
                            }
                        }
                    },
                    "IncChargblSplRateOS": {
                        "node_optional": {
                            "NRIOsDTAA": {
                                "array_optional": {
                                    "NRIDTAADtlsSchOS": {
                                        "field_optional": [
                                            ("DTAAamt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("NatureOfIncome", str, DataTypeTransformation.str_transform, False, str.lower, None, None),
                                            ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("DTAAarticle", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("RateAsPerTreaty", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                            ("TaxRescertifiedFlag", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                            ("SecITAct", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("RateAsPerITAct", float, DataTypeTransformation.float_transformation, False, DataTypeTransformation.float_transformation, None, None),
                                            ("ApplicableRate", float, DataTypeTransformation.float_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("DTAAamt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("RateAsPerTreaty", float, DataTypeTransformation.float_transformation, True, None, None, None),
                                            ("RateAsPerITAct", float, DataTypeTransformation.float_transformation, True, DataTypeTransformation.float_transformation, None, None),
                                        ]
                                    }
                                }
                            }
                        },
                        "field_optional": [
                            ("TotalAmtTaxUsDTAASchOs", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalAmtTaxUsDTAASchOs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "Deductions": {
                        "field_optional": [
                            ("Expenses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("UsrIntExp57", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IntExp57", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Depreciation", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotDeductions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Depreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotDeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "cm_node_map": {
                    "Deductions": {
                        "field_optional": [
                            ("Depreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotDeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
                "field_optional": [
                    ("GrossIncChrgblTaxAtAppRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DividendGross", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DividendOthThan22e", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Dividend22e", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Dividend22f", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("InterestGross", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntrstFrmSavingBank", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntrstFrmTermDeposit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntrstFrmIncmTaxRefund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NatofPassThrghIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntrstFrmOthers", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("RentFromMachPlantBldgs", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Tot562x", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Aggrtvaluewithoutcons562x", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Immovpropwithoutcons562x", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Immovpropinadeqcons562x", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Anyotherpropwithoutcons562x", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Anyotherpropinadeqcons562x", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AnyOtherIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncChargeableSpecialRates", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("SumRecdPrYrBusTRU562xii", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("LtryPzzlChrgblUs115BB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncChrgblUs115BBJ", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncChrgblUs115BBE", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CashCreditsUs68", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("UnExplndInvstmntsUs69", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("UnExplndMoneyUs69A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("UnDsclsdInvstmntsUs69B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("UnExplndExpndtrUs69C", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtBrwdRepaidOnHundiUs69D", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthersGross", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PassThrIncOSChrgblSplRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtNotDeductibleUs58", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProfitChargTaxUs59", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BalanceNoRaceHorse", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("GrossIncChrgblTaxAtAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DividendGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DividendOthThan22e", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Dividend22e", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Dividend22f", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("InterestGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmSavingBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmTermDeposit", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmIncmTaxRefund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NatofPassThrghIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmOthers", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RentFromMachPlantBldgs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Tot562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Aggrtvaluewithoutcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Immovpropwithoutcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Immovpropinadeqcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Anyotherpropwithoutcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Anyotherpropinadeqcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AnyOtherIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncChargeableSpecialRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("LtryPzzlChrgblUs115BB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncChrgblUs115BBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CashCreditsUs68", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnExplndInvstmntsUs69", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnExplndMoneyUs69A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnDsclsdInvstmntsUs69B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnExplndExpndtrUs69C", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtBrwdRepaidOnHundiUs69D", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthersGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncOSChrgblSplRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalanceNoRaceHorse", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "OthersGrossDtls": {
                        "field_optional": [
                            ("SourceDescription", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("SourceAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("SourceAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    },
                    "PTIOthersGrossDtls": {
                        "field_optional": [
                            ("SourceDescription", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("SourceAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("SourceAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                }
            },
            "IncFromOwnHorse": {
                "field_optional": [
                    ("Receipts", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DeductSec57", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtNotDeductibleUs58", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProfitChargTaxUs59", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BalanceOwnRaceHorse", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("Receipts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DeductSec57", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalanceOwnRaceHorse", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "IncFrmLottery": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "IncFrmOnGames": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115BBDA": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115BBDAaiii": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115A1ai": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115A1aA": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115AC": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115AD1iDiv": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115AD1IBd": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendDTAA": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            }
        },
        "field_optional": [
            ("TotOthSrcNoRaceHorse", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("IncChargeableFrmOthSrc", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotOthSrcNoRaceHorse", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("IncChargeableFrmOthSrc", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "IncOthThanOwnRaceHorse": {
                "node_optional": {
                    "Deductions": {
                        "field_optional": [
                            ("Depreciation", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotDeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
                "field_optional": [
                    ("GrossIncChrgblTaxAtAppRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DividendGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DividendOthThan22e", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Dividend22e", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("InterestGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmSavingBank", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmTermDeposit", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmIncmTaxRefund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NatofPassThrghIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstFrmOthers", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("RentFromMachPlantBldgs", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Tot562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Aggrtvaluewithoutcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Immovpropwithoutcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Immovpropinadeqcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Anyotherpropwithoutcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Anyotherpropinadeqcons562x", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AnyOtherIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncChargeableSpecialRates", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("LtryPzzlChrgblUs115BB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncChrgblUs115BBE", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CashCreditsUs68", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnExplndInvstmntsUs69", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnExplndMoneyUs69A", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnDsclsdInvstmntsUs69B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnExplndExpndtrUs69C", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtBrwdRepaidOnHundiUs69D", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthersGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PassThrIncOSChrgblSplRate", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalanceNoRaceHorse", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "IncFrmLottery": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115BBDA": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115A1ai": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115BBDAaiii": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115AC": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115AD1iDiv": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendIncUs115AD1IBd": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "DividendDTAA": {
                "node_optional": {
                    "DateRange": {
                        "field_optional": [
                            ("Upto15Of6", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of6To15Of9", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of9To15Of12", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of12To15Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Up16Of3To31Of3", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            }
        }
    },
    "ScheduleCYLA": {
        "node_optional": {
            "field_optional": [
                ("CYLAEditFlag", int, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ],
            "TotalCurYr": {
                "field_required": [
                    ("TotHPlossCurYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotBusLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotOthSrcLossNoRaceHorse", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "HP": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "BusProfExclSpecProf": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "ProfGainUs115B": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "SpeculationIncome": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "SpecifiedBusIncome": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG15Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG20Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG30Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGAppRate": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGDTAARate": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG10Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG12_5Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG20Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCGDTAARate": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "OthSrcExclRaceHorseLottery": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "ProfitFrmRaceHorse": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "IncOSDTAA": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("HPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BusLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "TotalLossSetOff": {
                "field_required": [
                    ("TotHPlossCurYrSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotBusLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotOthSrcLossNoRaceHorseSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "LossRemAftSetOff": {
                "field_required": [
                    ("BalHPlossCurYrAftSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalBusLossAftSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalOthSrcLossNoRaceHorseAftSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        },
        "cm_node_map": {
            "STCG30Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG15Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG20Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGAppRate": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGDTAARate": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG10Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG12_5Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG20Per": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCGDTAARate": {
                "node_optional": {
                    "IncCYLA": {
                        "field_optional": [
                            ("IncOfCurYrUnderThatHead", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
        }
    },
    "ScheduleBFLA": {
        "node_optional": {
            "field_optional": [
                ("BFLAEditFlag", int, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ],
            "HP": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "BusProfExclSpecProf": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "ProfGainUs115B": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "SpeculationIncome": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "SpecifiedBusIncome": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG15Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG20Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG30Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGAppRate": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGDTAARate": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG10Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG12_5Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG20Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCGDTAARate": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "OthSrcExclRaceHorse": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "ProfitFrmRaceHorse": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFlossPrevYrUndSameHeadSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "IncOSDTAA": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BFUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BFAllUs35Cl4Setoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "TotalBFLossSetOff": {
                "field_optional": [
                    ("TotBFLossSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotAllUs35cl4Setoff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotBFLossSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotUnabsorbedDeprSetoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAllUs35cl4Setoff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        },
        "field_optional": [
            ("IncomeOfCurrYrAftCYLABFLA", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("IncomeOfCurrYrAftCYLABFLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "STCG15Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG20Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCG30Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGAppRate": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "STCGDTAARate": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG10Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG12_5Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCG20Per": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "LTCGDTAARate": {
                "node_optional": {
                    "IncBFLA": {
                        "field_optional": [
                            ("IncOfCurYrUndHeadFromCYLA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("IncOfCurYrAfterSetOffBFLosses", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
        }
    },
    "ScheduleCFL": {
        "node_optional": {
            "LossCFFromPrev9thYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFFromPrev8thYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFFromPrev7thYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFFromPrev6thYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFFromPrev5thYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFFromPrev4thYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                           
                        ],
                    }
                },
            },
            "LossCFFromPrev3rdYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFFromPrev2ndYearFromAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFFromPrevYrToAY": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFCurrentAssmntYear": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFCurrentAssmntYear2021": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFCurrentAssmntYear2022": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFCurrentAssmntYear2023": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFCurrentAssmntYear2023": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFCurrentAssmntYear2024": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "LossCFCurrentAssmntYear2025": {
                "node_optional": {
                    "CarryFwdLossDetail": {
                        "field_optional": [
                            ("DateOfFiling", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwrdBusLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtAdjAccOptTaxUs115BAA_115BA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                    }
                },
            },
            "TotalOfBFLossesEarlierYrs": {
                "node_optional": {
                    "LossSummaryDetail": {
                        "field_optional": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            },
            "AdjTotBFLossInBFLA": {
                "node_optional": {
                    "LossSummaryDetail": {
                        "field_optional": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "CurrentAYloss": {
                "node_optional": {
                    "LossSummaryDetail": {
                        "field_optional": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "CurrentYearDistrUnitHolder": {
                "node_optional": {
                    "LossSummaryDetail": {
                        "field_optional": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ]
                    }
                },
            },
            "CurrentYearLossCF": {
                "node_optional": {
                    "LossSummaryDetail": {
                        "field_optional": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
            "TotalLossCFSummary": {
                "node_optional": {
                    "LossSummaryDetail": {
                        "field_optional": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalHPPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("BroughtFrwdBusLossSetOffDrYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmSpecifiedBusCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("LossFrmLifeInsBusUs115B", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalSTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotalLTCGPTILossCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OthSrcLossRaceHorseCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ]
                    }
                },
            },
        },
    },
    "ITRScheduleUD": {
        "field_optional": [
            ("CurrAssYr", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("CurBalCFNY", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("CurAllowBalCFNY", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotAmtAdjOptTaxUs115BAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotCurYrdepritSetoffInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotDepritBalCFNY", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotBFUAllowAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotCurYrAllowSetoffInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalBalCFNY", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotBFUDepritAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("CurBalCFNY", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("CurAllowBalCFNY", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotAmtAdjOptTaxUs115BAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotCurYrdepritSetoffInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotDepritBalCFNY", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotBFUAllowAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotCurYrAllowSetoffInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalBalCFNY", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotBFUDepritAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "ScheduleUD": {
                "field_optional": [
                    ("AssYr", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AmtBFUD", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtAdjOptTaxUs115BAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtDeprSOCY", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BalCFNY", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtBFUAllow", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtAllowSOCY", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AllowBalCFNY", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmtAdjOptTaxUs115BAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtDeprSOCY", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalCFNY", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtBFUD", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtBFUAllow", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtAllowSOCY", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AllowBalCFNY", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        }
    },
    "ScheduleICDS": {
        "node_optional":{
            "AccPolicyAmtDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "InventoriesValueDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "ConstContractsAmtDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "RevenueRcgAmtDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "TangibleFixedAssetDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "ForeignExgRatesDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "GovtGrantsDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "SecuritiesDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "BorrowingCostsDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
            "ProvAssetsDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("NetEffect", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
        },
        "node_required":{
            "TotalNetAmtDetl":{
                "field_optional":[
                      ("IncreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                      ("DecreaseInProfit", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ]
            },
        },
    },
    "Schedule10AA": {
        "node_optional": {
            "DeductSEZ": {
                "node_optional": {
                    "DedUs10Detail": {
                        "node_optional": {
                            "Undertaking": {
                                "array_optional": {
                                    "DedFromUndertakingWithAy": {
                                        "field_optional": [
                                            ("AssmtYrUnit", str, DataTypeTransformation.str_transform, False, None, None, None),
                                            ("DedUs10Sub", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("DedUs10Sub", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                }
                            }
                        },
                        "field_optional": [
                            ("TotalDedUs10Sub", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TotalDedUs10Sub", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "cm_node_map": {
                            "Undertaking": {
                                "array_optional": {
                                    "DedFromUndertakingWithAy": {
                                        "field_optional": [
                                            ("DedUs10Sub", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                }
                            }
                        }
                    }
                },
            }
        },
    },
    "Schedule80G": {
        "node_optional": {
            "Don100Percent": {
                "field_optional": [
                    ("TotDon100PercentCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon100PercentOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon100Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotElgDon100Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotDon100PercentCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon100PercentOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon100Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotElgDon100Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "DoneeDetail": {
                        "node_optional": {
                            "AddressDetail": {
                                "field_optional": [
                                    ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_required": {}
                            }
                        },
                        "field_optional": [
                            ("DoneeName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("DoneePAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ArnNbr", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            },
            "Don50PercentNoApprReqd": {
                "field_optional": [
                    ("TotDon50PercentNoApprReqdCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon50PercentNoApprReqdOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon50PercentNoApprReqd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotElgDon50PercentNoApprReqd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotDon50PercentNoApprReqdCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon50PercentNoApprReqdOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon50PercentNoApprReqd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotElgDon50PercentNoApprReqd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "DoneeDetail": {
                        "node_optional": {
                            "AddressDetail": {
                                "field_optional": [
                                    ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_required": {}
                            }
                        },
                        "field_optional": [
                            ("DoneeName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("DoneePAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ArnNbr", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            },
            "Don100PercentApprReqd": {
                "field_optional": [
                    ("TotDon100PercentApprReqdCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon100PercentApprReqdOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon100Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotElgDon100Percent", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotDon100PercentApprReqdCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon100PercentApprReqdOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon100Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotElgDon100Percent", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "DoneeDetail": {
                        "node_optional": {
                            "AddressDetail": {
                                "field_optional": [
                                    ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_required": {}
                            }
                        },
                        "field_optional": [
                            ("DoneeName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("DoneePAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ArnNbr", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            },
            "Don50PercentApprReqd": {
                "field_optional": [
                    ("TotDon50PercentApprReqdCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon50PercentApprReqdOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDon50PercentApprReqd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotElgDon50PercentApprReqd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotDon50PercentApprReqdCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon50PercentApprReqdOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDon50PercentApprReqd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotElgDon50PercentApprReqd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "DoneeDetail": {
                        "node_optional": {
                            "AddressDetail": {
                                "field_optional": [
                                    ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                                "array_required": {}
                            }
                        },
                        "field_optional": [
                            ("DoneeName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("DoneePAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ArnNbr", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DonationAmtCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("DonationElgAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            }
        },
        "field_optional": [
            ("TotalDonationsUs80GCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalDonationsUs80GOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalDonationsUs80G", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalEligibleDonationsUs80G", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalDonationsUs80GCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalDonationsUs80GOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalDonationsUs80G", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalEligibleDonationsUs80G", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
    },
    "Schedule80GGA": {
        "field_optional": [
            ("TotalDonationAmtCash80GGA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalDonationAmtOtherMode80GGA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalDonationsUs80GGA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalEligibleDonationAmt80GGA", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalDonationAmtCash80GGA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalDonationAmtOtherMode80GGA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalDonationsUs80GGA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalEligibleDonationAmt80GGA", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "DonationDtlsSciRsrchRuralDev": {
                "node_optional": {
                    "AddressDetail": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_required": {}
                    }
                },
                "field_optional": [
                    ("RelevantClauseUndrDedClaimed", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfDonee", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("DoneePAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DonationAmtCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("EligibleDonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                
                "cm_field_map": [
                    ("DonationAmtCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EligibleDonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "Schedule80RA": {
        "field_optional": [
            ("TotalDonationAmtCash80RA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalDonationAmtOtherMode80RA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalDonationsUs80RA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalEligibleDonationAmt80RA", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalDonationAmtCash80RA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalDonationAmtOtherMode80RA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalDonationsUs80RA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalEligibleDonationAmt80RA", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "DonationDtlsRsrchAssctn": {
                "node_optional": {
                    "AddressDetail": {
                        "field_optional": [
                            ("AddrDetail", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CityOrTownOrDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("StateCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "array_required": {}
                    }
                },
                "field_optional": [
                    ("NameOfDonee", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("DoneePAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DonationAmtCash", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("EligibleDonationAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("DonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EligibleDonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "Schedule80_IA": {
        "node_optional": {
            "DeductUs80_IA_4_i": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            },
            "DeductUs80_IA_4_iv": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            },
            "DeductUs80_IA_4_v": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            }
        },
        "field_optional": [
            ("Sch80SectionCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("TotSchedule80_IA", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotSchedule80_IA", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "DeductUs80_IA_4_i": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductUs80_IA_4_iv": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductUs80_IA_4_v": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            }
        },
    },
    "Schedule80_IB": {
        "node_optional": {
            "DeductMinOilUs80_IB_9_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            },
            "DeductHousUs80_IB_10_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            },
            "DeductFruitVegUs80_IB_11A_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            },
            "DeductFoodGrainUs80_IB_11A_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            }
        },
        "field_optional": [
            ("Sch80SectionCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("TotSchedule80_IB", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotSchedule80_IB", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "DeductJKLocUs80_IB_4_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductMinOilUs80_IB_9_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductHousUs80_IB_10_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductFruitVegUs80_IB_11A_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductFoodGrainUs80_IB_11A_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            }
        },
    },
    "Schedule80_IC": {
        "node_optional": {
            "DeductInSikkim_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            },
            "DeductInHimachalP_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            },
            "DeductInUttaranchal_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "Sch80DeductAmtDtls": {
                        "field_optional": [
                            ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            },
            "DeductInNorthEast": {
                "node_optional": {
                    "Assam_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    },
                    "ArunachalPradesh_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    },
                    "Manipur_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    },
                    "Mizoram_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    },
                    "Meghalaya_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    },
                    "Nagaland_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    },
                    "Tripura_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    },
                    "Sikkim_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [],
                        "array_optional": {
                            "Sch80DeductAmtDtls": {
                                "field_optional": [
                                    ("DeductAmountSec80", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        }
                    }
                },
                "field_optional": [
                    ("TotDeductInNorthEast", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotDeductInNorthEast", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "Assam_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "ArunachalPradesh_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Manipur_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Mizoram_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Meghalaya_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Nagaland_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Tripura_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Sikkim_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    }
                },
            }
        },
        "field_optional": [
            ("Sch80SectionCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("TotSchedule80_IC", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotSchedule80_IC", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "DeductInSikkim_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductInHimachalP_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductInUttaranchal_Und": {
                "field_optional": [
                    ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                ]
            },
            "DeductInNorthEast": {
                "node_optional": {
                    "Assam_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "ArunachalPradesh_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Manipur_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Mizoram_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Meghalaya_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Nagaland_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    },
                    "Tripura_Und": {
                        "field_optional": [
                            ("Sch80LocOrDescCode", str, DataTypeTransformation.str_transform, True, str.upper, None, None),
                        ]
                    }
                },
                "cm_field_map": [
                    ("TotDeductInNorthEast", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        },
    },
    "ScheduleVIA": {
        "node_optional": {
            "UsrDeductUndChapVIA": {
                "field_optional": [
                    ("Section80G", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80GGA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80GGB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80GGC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotPartBchapterVIA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IAB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IAC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IBA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80JJA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80JJAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80LA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80LA_1A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80M", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80M_OS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80M_BP", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80PA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotPartCchapterVIA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalChapVIADeductions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotPartBchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotPartCchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalChapVIADeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "array_optional": {
                    "Section80MDtls": {
                        "field_optional": [
                            ("Section80MDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("Section80MAmnt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Section80MType", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [],
                    }
                }
            },
            "DeductUndChapVIA": {
                "field_optional": [
                    ("Section80G", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80GGA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80GGB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80GGC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotPartBchapterVIA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IAB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IAC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IBA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80IC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80JJA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80JJAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80LA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80LA_1A", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80M", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80M_OS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80M_BP", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Section80PA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotPartCchapterVIA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalChapVIADeductions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotPartBchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotPartCchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalChapVIADeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },

        },
        "cm_field_map": [],
        "cm_node_map": {
            "UsrDeductUndChapVIA": {
                "field_optional": [
                    ("TotPartBchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotPartCchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalChapVIADeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            },
            "DeductUndChapVIA": {
                "field_optional": [
                    ("TotPartBchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotPartCchapterVIA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalChapVIADeductions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        },
    },                      
    "Schedule80GGC":{
        "array_optional":{
            "Schedule80GGCDetails":{
                "field_required":[
                    ("DonationDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("DonationAmtCash", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DonationAmtOtherMode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("EligibleDonationAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ],
                "field_optional":[
                    ("IFSCCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("TransactionRefNum", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ]
            },

        },
        "field_required":[
                      ("TotalDonationAmtCash80GGC",int, DataTypeTransformation.int_transformation, True, None, None, None),
                      ("TotalDonationAmtOtherMode80GGC", int, DataTypeTransformation.int_transformation, True, None, None, None),
                      ("TotalDonationsUs80GGC", int, DataTypeTransformation.int_transformation, True, None, None, None),
                      ("TotalEligibleDonationAmt80GGC", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ]

    },
    "Schedule80IAC":{
        "field_required":{
            ("DateIncrpStrup", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
            ("NatureOfBusiness", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("InterMnstBoardCertNum", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("FstAYDeduction", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("AmtDedCurAY", int, DataTypeTransformation.int_transformation, True, None, None, None),

        }

    },

    "Schedule80LA":{
        "array_optional":{
            "Schedule80LADtls":{
                "field_optional":[
                    ("SubSecDedClmd", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("EntityType", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("IncmTypeUnt", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("RegGNTAuth", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("RegDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("RegNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FstAYDeduction", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AmtDedCurAY", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]
            }
        },
        "field_optional":{
            ("Total", int, DataTypeTransformation.int_transformation, True, None, None, None),
        }
     },
    "ScheduleSI": {
        "field_optional": [
            ("TotSplRateInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotSplRateIncTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotSplRateInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotSplRateIncTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "SplCodeRateTax": {
                "field_optional": [
                    ("SecCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("SplRatePercent", int, DataTypeTransformation.float_transformation_without_roundof, False, None, None, None),
                    ("SplRateInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("SplRateIncTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("SplRateInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("SplRateIncTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "ScheduleIF": {
        "field_optional": [
            ("TotalProfitShareAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalFirmCapBalOn31Mar", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalProfitShareAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalFirmCapBalOn31Mar", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "PartnerFirmDetails": {
                "field_optional": [
                    ("FirmName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FirmType", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FirmPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IsLiableToAudit", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("Sec92EFirmFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("ProfitSharePercent", float, DataTypeTransformation.float_transformation, False, None, None, None),
                    ("ProfitShareAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("FirmCapBalOn31Mar", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("ProfitSharePercent", float, DataTypeTransformation.float_transformation, True, None, None, None),
                    ("ProfitShareAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("FirmCapBalOn31Mar", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "ScheduleEI": {
        "node_optional": {
            "ExcNetAgriInc": {
                "cm_field_map": [],
                "array_optional": {
                    "ExcNetAgriIncDtls": {
                        "field_optional": [
                            ("NameOfDistrict", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("MeasurementOfLand", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("AgriLandOwnedFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("AgriLandIrrigatedFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("MeasurementOfLand", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                    }
                }
            },
            "OthersInc": {
                "cm_field_map": [],
                "array_optional": {
                    "OthersIncDtls": {
                        "field_optional": [
                            # ("NatureExempt", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            # ("OthNatOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                            # ("OthAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NatureExempt", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OthAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcknowledgementNum", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FormFiled", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("DateofFormFiled", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("OthNatOfInc", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("OthAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NatureExempt", int, DataTypeTransformation.str_transform, True, None, None, None),
                        ],
                    }
                },
                "field_required":[
                      ("NatureofDescDivName", str, DataTypeTransformation.str_transform, False, None, None, None),
                      ("OthDividendAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ]

            },
            "IncNotChrgblAsPerDTAA": {
                "cm_field_map": [],
                "array_optional": {
                    "IncNotChrgblAsPerDTAADtls": {
                        "field_optional": [
                            ("AmountOfIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NatureOfIncome", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ArticleOfDTAA", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("HeadOfIncome", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TRCFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("AmountOfIncome", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            }
        },
        "field_required": [
            ("InterestInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("GrossAgriRecpt", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("ExpIncAgri", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("UnabAgriLossPrev8", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("NetAgriIncRelateToRule7", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("NetAgriIncOrOthrIncRule7", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Others", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("IncChrgblAsPerDTAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("PassThrIncNotChrgblTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalExemptInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalExemptInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("NetAgriIncOrOthrIncRule7", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("IncChrgblAsPerDTAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
    },
    "SchedulePTI": {
        "cm_field_map": [],
        "array_optional": {
            "SchedulePTIDtls": {
                "node_optional": {
                    "IncFromHP": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "CapitalGainsPTI": {
                        "node_optional": {
                            "ShortTermCG": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "STCG_Sec111A": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "STCG_Others": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LongTermCG": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LTCG_Sec112A": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LTCG_Others": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                        "cm_field_map": [],
                        "cm_node_map": {
                            "ShortTermCG": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "STCG_Sec111A": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "STCG_Others": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LongTermCG": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LTCG_Sec112A": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LTCG_Others": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        },
                    },
                    "IncOthSrc": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "OS_Dividend": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "OS_Others": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncClmdPTI": {
                        "node_optional": {
                            "TotalSec23FBB": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "Sec23FBB": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                                "cm_field_map": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "SecBIncExmptDtl": {
                                "node_optional": {
                                    "SecBCIncExmptDtl": {
                                        "field_optional": [
                                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_optional": [
                                    ("SectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            },
                            "SecCIncExmptDtl": {
                                "node_optional": {
                                    "SecBCIncExmptDtl": {
                                        "field_optional": [
                                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                            ("TDSAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                        ],
                                        "cm_field_map": [
                                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                        ],
                                    }
                                },
                                "field_optional": [
                                    ("SectionCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        },
                        "cm_field_map": [],
                        "cm_node_map": {
                            "TotalSec23FBB": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "Sec23FBB": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                        }
                    }
                },
                "field_optional": [
                    ("InvstmntCvrdUs115UA115UB", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("BusinessName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("BusinessPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "cm_node_map": {
                    "IncFromHP": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "CapitalGainsPTI": {
                        "node_optional": {
                            "ShortTermCG": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "STCG_Sec111A": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "STCG_Others": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LongTermCG": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LTCG_Sec112A": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "LTCG_Others": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("CurrYrLossShareByInvstFund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        }
                    },
                    "IncOthSrc": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "OS_Dividend": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "OS_Others": {
                        "field_optional": [
                            ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncClmdPTI": {
                        "node_optional": {
                            "TotalSec23FBB": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            },
                            "Sec23FBB": {
                                "field_optional": [
                                    ("AmountOfInc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("NetIncomeLoss", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                    ("TDSAmount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                                ],
                            }
                        }
                    }
                },
            }
        }
    },
    "ScheduleMAT": {
        "node_optional": {
            "Additions": {
                "field_optional": [
                    ("ITPaidInclDefTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ResvrNo33AC", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProvUncertainLiab", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProvLossOfSubsComp", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DividendPaidOrProposed", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ExpendExempIncUs10s", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ExpAopBoi", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ExpClauseFb", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NotLossClauseFc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NotLossUs115bbf", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("DepreciatAttribToRevalAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("GainClauseK", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Others", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("ITPaidInclDefTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ResvrNo33AC", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProvUncertainLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProvLossOfSubsComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DividendPaidOrProposed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpendExempIncUs10s", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpAopBoi", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpClauseFb", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NotLossClauseFc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NotLossUs115bbf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DepreciatAttribToRevalAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("GainClauseK", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAdditions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "Deducts": {
                "field_optional": [
                    ("AmtWithdrawFromResvrIfCredPL", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncExempIncUs10s", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtWithdrawFromResvrIfCredPLNoAttrib", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ShareIncAopBoi", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncClauseiid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NotGainClauseiie", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("LossTrnsClauseiif", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("LossTrnsClauseiig", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("UnAbsorbedDepreciat", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ProSickIndustryOrExcedAccumLos", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Others", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotDeducts", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmtWithdrawFromResvrIfCredPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncExempIncUs10s", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtWithdrawFromResvrIfCredPLNoAttrib", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ShareIncAopBoi", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncClauseiid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NotGainClauseiie", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("LossTrnsClauseiif", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnAbsorbedDepreciat", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProSickIndustryOrExcedAccumLos", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDeducts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "AdditionsProfUs115JB": {
                "field_optional": [
                    ("AmountsCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmountsDebited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OneFifthTransitionAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthersInclResidualAdjust", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmountsCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmountsDebited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OneFifthTransitionAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthersInclResidualAdjust", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAdditions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DeductionsProfUs115JB": {
                "field_optional": [
                    ("AmountsCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmountsDebited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OneFifthTransitionAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("OthersInclResidualAdjust", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalAdditions", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmountsCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmountsDebited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OneFifthTransitionAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("OthersInclResidualAdjust", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalAdditions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        },
        "field_optional": [
            ("PLAcntPrepSchedVICompAct", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("PLAcctFlg", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("PLAcntPrepAsperAGM", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("ProfAfterTaxPLAcnt", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("BookProfUs115JB", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("FinancialStamentFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("DeemedTotalIncUs115JB", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DeemedTotalIncUs115JBIFSC", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("DeemedTotalIncUs115JBOther", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TaxPayableUs115JB", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("ProfAfterTaxPLAcnt", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("BookProfUs115JB", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("DeemedTotalIncUs115JB", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("DeemedTotalIncUs115JBIFSC", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("DeemedTotalIncUs115JBOther", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TaxPayableUs115JB", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "cm_node_map": {
            "Additions": {
                "field_optional": [
                    ("ITPaidInclDefTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ResvrNo33AC", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProvUncertainLiab", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProvLossOfSubsComp", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DividendPaidOrProposed", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpendExempIncUs10s", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpAopBoi", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ExpClauseFb", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NotLossClauseFc", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NotLossUs115bbf", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("DepreciatAttribToRevalAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("GainClauseK", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotAdditions", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "Deducts": {
                "field_optional": [
                    ("AmtWithdrawFromResvrIfCredPL", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncExempIncUs10s", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtWithdrawFromResvrIfCredPLNoAttrib", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ShareIncAopBoi", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncClauseiid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NotGainClauseiie", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("LossTrnsClauseiif", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("UnAbsorbedDepreciat", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ProSickIndustryOrExcedAccumLos", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Others", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotDeducts", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
        }
    },
    "ScheduleMATC": {
        "field_optional": [
            ("TaxUs115JBCurrAssYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TaxOthProvCurrAssYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AmtOfTaxWithCred", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("CurAssYr", str, DataTypeTransformation.str_transform, False, None, None, None),
            ("MATCredGrossCurAY", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("BalMATCredCFCurAY", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotMatCredGross", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotMatCredSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotMatCredBF", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotMatCredUtilCurrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotBalMATCredCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AmtTaxCredUs115JAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AmtMATLiabAllAssYrAvailSubseqYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TaxUs115JBCurrAssYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TaxOthProvCurrAssYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("AmtOfTaxWithCred", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("MATCredGrossCurAY", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("BalMATCredCFCurAY", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotMatCredGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotMatCredSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotMatCredBF", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotMatCredUtilCurrYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotBalMATCredCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("AmtTaxCredUs115JAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("AmtMATLiabAllAssYrAvailSubseqYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "UtilMATCredAvl": {
                "field_optional": [
                    ("AssYr", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("MATCredGross", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("MATCredSetOff", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("MATCredBF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("MATCredUtilCurrYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BalMATCredCF", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("MATCredGross", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("MATCredSetOff", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("MATCredBF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("MATCredUtilCurrYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("BalMATCredCF", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "ScheduleBBS": {
        "cm_field_map": [],
        "array_optional": {
            "BBS": {
                "node_optional": {
                    "TaxPayOnDividDeclarOrPaid": {
                        "field_optional": [
                            ("AddLITPayUs115QA", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Surcharge", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("EducationCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TotBBSPayable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AddLITPayUs115QA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Surcharge", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EducationCess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotBBSPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
                "field_optional": [
                    ("DateOfDeclareDividProfDomesComp", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("CmpBuyBckShrAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CmpRecShrAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("CmpDistIncm", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntPayUs115QB", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AddLITPlusIntrestPayable", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotalOfBBS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TaxAndInterestPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NetBBSPayableOrRefund", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("CmpBuyBckShrAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CmpRecShrAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("CmpDistIncm", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntPayUs115QB", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AddLITPlusIntrestPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotalOfBBS", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TaxAndInterestPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NetBBSPayableOrRefund", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "TaxPayOnDividDeclarOrPaid": {
                        "field_optional": [
                            ("AddLITPayUs115QA", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Surcharge", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("EducationCess", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TotBBSPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                },
                "array_optional": {
                    "TaxPaymentOnDDTndBBS": {
                        "node_optional": {
                            "NameOfBankAndBranch": {
                                "field_optional": [
                                    ("NameOfBank", str, DataTypeTransformation.str_transform, False, None, None, None),
                                    ("NameOfBranch", str, DataTypeTransformation.str_transform, False, None, None, None),
                                ],
                                "cm_field_map": [],
                            }
                        },
                        "field_optional": [
                            ("DateDep", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("BSRCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("SrlNoOfChaln", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Amt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("SrlNoOfChaln", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Amt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                }
            }
        }
    },
    "ScheduleTPSA": {
        "field_optional": [
            ("AmtPrimaryAdjUs92CE_2A", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AdditionalIncTax18PercAbove", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("Surcharge12Perc", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("HealthEducationCess", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalAdditionalTax", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TaxesPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("NetTaxPayable", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalAmountDeposited", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("AmtPrimaryAdjUs92CE_2A", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("AdditionalIncTax18PercAbove", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("Surcharge12Perc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("HealthEducationCess", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalAdditionalTax", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TaxesPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("NetTaxPayable", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalAmountDeposited", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "DtlsTaxesPaid": {
                "field_optional": [
                    ("BSRCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("BankBranchName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("DateDep", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("SrlNoOfChaln", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("SrlNoOfChaln", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "Schedule115TD":{
        "node_optional":{
            "DepositofTaxAccInc":{
                "array_optional":{
                    "DepositofTaxAccIncDtls":{
                       "field_optional":{
                           ("DateDep",str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                           ("NameBankBranch", str, DataTypeTransformation.str_transform, False, None, None, None),
                           ("BSRCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                           ("SrlNoOfChaln", int, DataTypeTransformation.int_transformation, False, None, None, None),
                           ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                       } 
                    }

                }

            },
        },
        "field_optional":[
             ("FMVTotTrustInst", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("LessTotLiaTrustInst", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("NetValAsst", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("FMVAsstAcqrdRfrdSec101", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("FMVAsstAcqPeriodFromDateCrtn", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("FMVAsstTrnfsrdSec115TD2", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("FMVTotal", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("LiabilityRespectofAsset4Above", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("AccretedIncomeSection115TD", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("AddIncPay115TDMarginalRate", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("InterestPayable115TE", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("SpecifiedDateUs115TD",str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
             ("AddIncIntstPayb", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("TaxIntstPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
             ("NetPaybleRefble", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ]
    },
    "ScheduleFSI": {
        "cm_field_map": [],
        "array_optional": {
            "ScheduleFSIDtls": {
                "node_optional": {
                    "IncFromHP": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DTAAReliefUs90or90A", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncFromBusiness": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DTAAReliefUs90or90A", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncCapGain": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DTAAReliefUs90or90A", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncOthSrc": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DTAAReliefUs90or90A", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "TotalCountryWise": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("DTAAReliefUs90or90A", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("TaxIdentificationNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [],
                "cm_node_map": {
                    "IncFromHP": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncFromBusiness": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncCapGain": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "IncOthSrc": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "TotalCountryWise": {
                        "field_optional": [
                            ("IncFrmOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPaidOutsideInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxPayableinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("TaxReliefinInd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            }
        }
    },
    "ScheduleTR1": {
        "field_optional": [
            ("TotalTaxOutsideIndia", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TotalTaxReliefOutsideIndia", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TaxReliefOutsideIndiaDTAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TaxReliefOutsideIndiaNotDTAA", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("TaxPaidOutsideIndFlg", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
            ("AmtTaxRefunded", int, DataTypeTransformation.int_transformation, False, None, None, None),
            ("AssmtYrTaxRelief", str, DataTypeTransformation.str_transform, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalTaxOutsideIndia", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TotalTaxReliefOutsideIndia", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TaxReliefOutsideIndiaDTAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("TaxReliefOutsideIndiaNotDTAA", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "ScheduleTR": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("TaxIdentificationNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("TaxPaidOutsideIndia", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TaxReliefOutsideIndia", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ReliefClaimedUsSection", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [
                    ("TaxPaidOutsideIndia", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TaxReliefOutsideIndia", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "ScheduleFA": {
        "cm_field_map": [],
        "array_optional": {
            "DetailsForiegnBank": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Bankname", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfBank", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ForeignAccountNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("OwnerStatus", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AccOpenDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("PeakBalanceDuringYear", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IntrstAccured", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("PeakBalanceDuringYear", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IntrstAccured", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DtlsForeignCustodialAcc": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FinancialInstName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FinancialInstAddress", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AccountNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Status", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AccOpenDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("PeakBalanceDuringPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("GrossAmtPaidCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NatureOfAmount", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [
                    ("PeakBalanceDuringPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("GrossAmtPaidCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DtlsForeignEquityDebtInterest": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfEntity", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfEntity", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NatureOfEntity", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("InterestAcquiringDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("InitialValOfInvstmnt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("PeakBalanceDuringPeriod", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotGrossAmtPaidCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotGrossProceeds", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("InitialValOfInvstmnt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("PeakBalanceDuringPeriod", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotGrossAmtPaidCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotGrossProceeds", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DtlsForeignCashValueInsurance": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FinancialInstName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("FinancialInstAddress", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ContractDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("CashValOrSurrenderVal", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TotGrossAmtPaidCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("CashValOrSurrenderVal", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TotGrossAmtPaidCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DetailsFinancialInterest": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NatureOfEntity", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfEntity", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfEntity", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NatureOfInt", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateHeld", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("TotalInvestment", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncFromInt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NatureOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("IncTaxAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncTaxSch", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncTaxSchNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotalInvestment", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncFromInt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncTaxAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
            },
            "DetailsImmovableProperty": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfProperty", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Ownership", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateOfAcq", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("TotalInvestment", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncDrvProperty", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NatureOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("IncTaxAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncTaxSch", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncTaxSchNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TotalInvestment", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncDrvProperty", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("IncTaxAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DetailsOthAssets": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NatureOfAsset", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("Ownership", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateOfAcq", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("TotalInvestment", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncDrvAsset", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NatureOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("IncTaxAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncTaxSch", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncTaxSchNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("IncDrvAsset", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("NatureOfInc", str, DataTypeTransformation.str_transform, True, None, None, None),
                    ("IncTaxAmt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DetailsOfAccntsHvngSigningAuth": {
                "field_optional": [
                    ("NameOfInstitution", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfInstitution", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameMentionedInAccnt", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("InstitutionAccountNumber", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("PeakBalanceOrInvestment", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncAccuredTaxFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncAccuredInAcc", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncOfferedAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncOfferedSch", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncOfferedSchNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [
                    ("PeakBalanceOrInvestment", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            },
            "DetailsOfTrustOutIndiaTrustee": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfTrust", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfTrust", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfOtherTrustees", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfOtherTrustees", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfSettlor", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfSettlor", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfBeneficiaries", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfBeneficiaries", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("DateHeld", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("IncDrvTaxFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncDrvFromTrust", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncOfferedAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncOfferedSch", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncOfferedSchNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [],
            },
            "DetailsOfOthSourcesIncOutsideIndia": {
                "field_optional": [
                    ("CountryName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("CountryCodeExcludingIndia", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("ZipCode", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("NameOfPerson", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AddressOfPerson", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("IncDerived", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("NatureOfInc", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("IncDrvTaxFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncOfferedAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("IncOfferedSch", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("IncOfferedSchNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                ],
                "cm_field_map": [],
            }
        }
    },
    "ScheduleSH": {
        "node_optional": {
            "ShrhldngUnlistedCompany": {
                "field_optional": [
                    ("SHUnlistedCompanyFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "DtlsSHEndPreviousYearUC": {
                        "field_optional": [
                            ("ShareholderName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ResidentialStatus", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareTypeOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("AllotmentDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("NumberOfSharesHeld", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("AmountReceived", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NumberOfSharesHeld", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("AmountReceived", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsEquityShareEndPrvYr": {
                        "field_optional": [
                            ("ApplicantName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ResidentialStatus", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareTypeOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ApplicationDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("NumberOfSharesApplied", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ApplicationMoneyReceived", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ProposedIssuePrice", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NumberOfSharesApplied", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("ApplicationMoneyReceived", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("ProposedIssuePrice", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "SHDtlsAnyTimePrevYearUC": {
                        "field_optional": [
                            ("ShareholderName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ResidentialStatus", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("NumberOfSharesHeld", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("AmountReceived", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("AllotmentDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("CeaseShareholderDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("CessationMode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("NewShareholderPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("NewShareholderAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NumberOfSharesHeld", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("AmountReceived", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    }
                }
            },
            "ShrhldngStartUps": {
                "cm_field_map": [],
                "array_optional": {
                    "DtlsSHEndPreviousYearSU": {
                        "field_optional": [
                            ("ShareholderName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ShareholderCategory", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareTypeOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("AllotmentDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("NumberOfSharesHeld", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("PaidUpValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("SharePremium", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NumberOfSharesHeld", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("PaidUpValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("SharePremium", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsShareAppMoneyAlltEndPrvYr": {
                        "field_optional": [
                            ("ApplicantName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ApplicantCategory", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareTypeOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ApplicationDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("NumberOfSharesApplied", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ProposedIssuePrice", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ShareApplicationMoney", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ShareApplicationPremium", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NumberOfSharesApplied", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("ProposedIssuePrice", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("ShareApplicationMoney", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("ShareApplicationPremium", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "SHDtlsAnyTimePrevYearSU": {
                        "field_optional": [
                            ("ShareholderName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ShareholderCategory", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Aadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("AllotmentDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("NumberOfSharesHeld", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("PaidUpValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("CeaseShareholderDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("CessationMode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("NewShareholderPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("NewShareholderAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NumberOfSharesHeld", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("PaidUpValuePerShare", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    }
                }
            },
        },
        "cm_field_map": [],
    },
    "ScheduleAL": {
        "node_optional": {
            "AsstLiabilitiesUnlistedCompany": {
                "field_optional": [
                    ("ALUnlistedCompanyFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "DtlsBldLandResHouseUC": {
                        "field_optional": [
                            ("Address", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsBldLandNotResHouseUC": {
                        "field_optional": [
                            ("Address", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsListedEquitySharesUC": {
                        "field_optional": [
                            ("OpenBalNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OpenBalShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OpenBalAcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ShrsAcqNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShrsAcqShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShrsAcqAcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ShrsTrsNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShrsTrsShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ShrsTrsSaleConsdr", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ClBalNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClBalShareType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("ClBalAcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpenBalNumberOfShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OpenBalAcquisitionCost", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsUnListedEquitySharesUC": {
                        "field_optional": [
                            ("CompanyName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OpenBalNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OpenBalAcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ShrsAcqNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SubscriptionPurchaseDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("IssuePricePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("PurchasePricePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ShrsTrsNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SaleConsideration", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ClBalNumberOfShares", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClBalAcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpenBalNumberOfShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OpenBalAcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClBalNumberOfShares", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClBalAcquisitionCost", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsOtherSecuritiesUC": {
                        "field_optional": [
                            ("SecuritiesType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("SecuritiesTypeOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("ListedUnlistedFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OpenBalNumberOfSecurities", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("OpenBalAcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ShrsAcqNumberOfSecurities", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SubscriptionPurchaseDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("FaceValuePerShare", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("IssuePriceSecurity", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("PurchasePricePerSecurity", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("ShrsTrsNumberOfSecurities", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("SaleConsideration", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClBalNumberOfSecurities", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClBalAcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpenBalNumberOfSecurities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("OpenBalAcquisitionCost", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("ClBalNumberOfSecurities", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClBalAcquisitionCost", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsCapitalContributionOthEntityUC": {
                        "field_optional": [
                            ("EntityName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtContributedDrgTheYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtWithdrawnDrgTheYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtprofitLossDividend", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmtContributedDrgTheYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmtWithdrawnDrgTheYr", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmtprofitLossDividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsLoansAdvancesUC": {
                        "field_optional": [
                            ("PersonName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmountReceived", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmountPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("InterestCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmountReceived", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmountPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsVehiclestransportUC": {
                        "field_optional": [
                            ("AssetParticulars", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("AssetParticularsOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("RegNumVehicle", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsJewelleryArchCollectionsUC": {
                        "field_optional": [
                            ("AssetParticulars", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("AssetParticularsOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("Quantity", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("Quantity", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsLiabilitiesUC": {
                        "field_optional": [
                            ("PersonName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmountReceived", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmountPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("InterestCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmountReceived", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmountPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    }
                }
            },
            "AsstLiabilitiesStartUps": {
                "field_optional": [
                    ("ALStartUpsFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                ],
                "cm_field_map": [],
                "array_optional": {
                    "DtlsBldLandResHouseSU": {
                        "field_optional": [
                            ("Address", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                        ],
                        "cm_field_map": [
                            ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsBldLandNotResHouseSU": {
                        "field_optional": [
                            ("Address", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PinCode", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TransferFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                        "cm_field_map": [
                            ("PinCode", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsLoansAdvancesSU": {
                        "field_optional": [
                            ("PersonName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("LoansAdvancesDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AmtLoansAdvances", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("Amount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("LoansAdvancesFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("RepaymentDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmtLoansAdvances", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("Amount", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsCapitalContributionSU": {
                        "field_optional": [
                            ("EntityName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("CapitalContributionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("AmtContribution", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtWithdrawn", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmtprofitLossDividend", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("AmtContribution", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmtWithdrawn", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmtprofitLossDividend", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsAcqustSharesSecuritiesSU": {
                        "field_optional": [
                            ("EntityCompanyName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("SharesSecuritiesType", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("SharesSecuritiesTypeOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("NumSharesSecuritiesAcq", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionCost", float, DataTypeTransformation.float_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("TransferFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("NumSharesSecuritiesAcq", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", float, DataTypeTransformation.float_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsVehiclestransportSU": {
                        "field_optional": [
                            ("AssetParticulars", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("AssetParticularsOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("RegNumVehicle", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                        ],
                        "cm_field_map": [
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsJewelleryAcquiredSU": {
                        "field_optional": [
                            ("AssetParticulars", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("Quantity", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Quantity", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsArchaeologicalCollctSU": {
                        "field_optional": [
                            ("AssetParticulars", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("AssetParticularsOthers", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("Quantity", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AcquisitionDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("Purpose", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferFlag", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TransferDate", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("Quantity", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AcquisitionCost", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "DtlsLiabilitiesSU": {
                        "field_optional": [
                            ("PersonName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmountReceived", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("AmountPaid", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("InterestCredited", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("OpeningBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmountReceived", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("AmountPaid", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestCredited", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("ClosingBalance", int, DataTypeTransformation.int_transformation, True, None, None, None),
                            ("InterestRate", float, DataTypeTransformation.float_transformation, True, None, None, None),
                        ],
                    }
                }
            },
        },
        "cm_field_map": [],
    },
    "ScheduleGST": {
        "cm_field_map": [],
        "array_optional": {
            "TurnoverGrsRcptForGSTIN": {
                "field_optional": [
                    ("GSTINNo", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("AmtTurnGrossRcptGSTIN", int, DataTypeTransformation.int_transformation_single, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmtTurnGrossRcptGSTIN", int, DataTypeTransformation.int_transformation_single, True, None, None, None),
                ],
            }
        }
    },
    "ScheduleFD": {
        "field_required": [
            ("PaymntMadeOnCapitalAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("PaymntMadeOnRevenueAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("ReceiptsOnCapitalAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
            ("ReceiptsOnRevenueAcc", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
    },
    "ScheduleIT": {
        "field_optional": [
            ("TotalTaxPayments", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalTaxPayments", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "TaxPayment": {
                "field_optional": [
                    ("BSRCode", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DateDep", str, DataTypeTransformation.str_transform, False, DataTypeTransformation.date_transform, None, None),
                    ("SrlNoOfChaln", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("Amt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("SrlNoOfChaln", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("Amt", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    },
    "ScheduleTDS2": {
        "field_optional": [
            ("TotalTDSonOthThanSals", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalTDSonOthThanSals", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "TDSOthThanSalaryDtls": {
                "node_optional": {
                    "TaxDeductCreditDtls": {
                        "field_optional": [
                            ("TaxDeductedOwnHands", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxDeductedIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxDeductedTDS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedOwnHands", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedTDS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedSpouseOthPrsnPAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("SpouseOthPrsnAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TaxClaimedOwnHands", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
                "field_optional": [
                    ("TDSCreditName", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("PANofOtherPerson", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AadhaarOfOtherPerson", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("TANOfDeductor", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("TDSSection", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("DeductedYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BroughtFwdTDSAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("GrossAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("HeadOfIncome", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AmtCarriedFwd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmtCarriedFwd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "TaxDeductCreditDtls": {
                        "field_optional": [
                            ("TaxClaimedOwnHands", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            }
        }
    },
    "ScheduleTDS3": {
        "field_optional": [
            ("TotalTDS3OnOthThanSal", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalTDS3OnOthThanSal", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "TDS3onOthThanSalDtls": {
                "node_optional": {
                    "TaxDeductCreditDtls": {
                        "field_optional": [
                            ("TaxDeductedOwnHands", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxDeductedIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxDeductedTDS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedOwnHands", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedIncome", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedTDS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TaxClaimedSpouseOthPrsnPAN", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("SpouseOthPrsnAadhaar", str, DataTypeTransformation.str_transform, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TaxClaimedOwnHands", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
                "field_optional": [
                    ("TDSCreditName", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("PANofOtherPerson", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AadhaarOfOtherPerson", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("PANOfBuyerTenant", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AadhaarOfBuyerTenant", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("TDSSection", str, DataTypeTransformation.str_transform, False, None, None, None),
                    ("DeductedYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BroughtFwdTDSAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("GrossAmount", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("HeadOfIncome", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                    ("AmtCarriedFwd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("AmtCarriedFwd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
                "cm_node_map": {
                    "TaxDeductCreditDtls": {
                        "field_optional": [
                            ("TaxClaimedOwnHands", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    }
                },
            }
        }
    },
    "ScheduleTCS": {
        "field_optional": [
            ("TotalSchTCS", int, DataTypeTransformation.int_transformation, False, None, None, None),
        ],
        "cm_field_map": [
            ("TotalSchTCS", int, DataTypeTransformation.int_transformation, True, None, None, None),
        ],
        "array_optional": {
            "TCSDetails": {
                "node_optional": {
                    "TCSCurrFYDtls": {
                        "field_optional": [
                            ("TCSAmtCollOwnHands", int, DataTypeTransformation.int_transformation, False, None, None, None),
                            ("TCSAmtCollOthrHands",int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TCSAmtCollOwnHands", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                    },
                    "TCSClaimedThisYearDtls": {
                        "field_optional": [
                            ("TCSAmtCollOwnHands", int, DataTypeTransformation.int_transformation, False, None, None, None),
                        ],
                        "cm_field_map": [
                            ("TCSAmtCollOwnHands", int, DataTypeTransformation.int_transformation, True, None, None, None),
                        ],
                        "node_optional": {
                            "TCSAmtCollOthrHands": {
                                "field_optional": [
                                    ("TaxClaimedTCS", int, DataTypeTransformation.int_transformation, False, None, None, None),
                                    ("PANOfOthrPrsn",int, DataTypeTransformation.int_transformation, False, None, None, None),
                                ],
                            },
                        },
                    },
                    "EmployerOrDeductorOrCollectDetl": {
                        "field_optional": [
                            ("TAN", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                            ("TCSCreditName", str, DataTypeTransformation.str_transform, False, None, None, None),
                            ("PANofOtherPerson", str, DataTypeTransformation.str_transform, False, str.upper, None, None),
                        ],
                    }
                },
                "field_optional": [
                    ("DeductedYr", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("BroughtFwdTCSAmt", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("AmtCarriedFwd", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TCSClaimedThisYearDtls", int, DataTypeTransformation.int_transformation, False, None, None, None),
                    ("TCSCurrFYDtls", int, DataTypeTransformation.int_transformation, False, None, None, None),
                ],
                "cm_field_map": [
                    ("TCSClaimedThisYearDtls", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("TCSCurrFYDtls", int, DataTypeTransformation.int_transformation, True, None, None, None),
                    ("AmtCarriedFwd", int, DataTypeTransformation.int_transformation, True, None, None, None),
                ],
            }
        }
    }
}