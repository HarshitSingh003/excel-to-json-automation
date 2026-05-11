import json

from payload_generator_one_form import generate_payload
from structure_service import get_active_structure


def main():
    active = get_active_structure("ITR6_BASIC")
    schema_json = active["schema_json"]

    source_payload = {
        "CreationInfo": {
            "SWVersionNo": "1.0.0",
            "SWCreatedBy": "mobifly",
        },
        "Form_ITR6": {
            "FormName": "itr6",
            "AssessmentYear": "2025-26",
        },
        "PartA_GEN1": {
            "OrgFirmInfo": {
                "PAN": "aabca1111k",
                "Address": {
                    "CityOrTownOrDistrict": "Pune",
                    "CountryCode": "in",
                },
            }
        },
    }

    payload = generate_payload(schema_json, source_payload)
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
