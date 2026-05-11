BEGIN;

WITH inserted AS (
    INSERT INTO payload_structure (
        form_type,
        version_major,
        version_minor,
        status,
        is_active,
        schema_json,
        schema_hash,
        validation_report,
        created_by,
        updated_by
    )
    VALUES (
        'ITR6_BASIC',
        1,
        0,
        'active',
        TRUE,
        '{
          "CreationInfo": {
            "field_required": [
              {
                "name": "SWVersionNo",
                "type": "str",
                "cast": "to_str",
                "allow_blank": false,
                "transform": null,
                "default_enabled": false,
                "default_value": null
              },
              {
                "name": "SWCreatedBy",
                "type": "str",
                "cast": "to_str",
                "allow_blank": false,
                "transform": "to_upper",
                "default_enabled": false,
                "default_value": null
              }
            ]
          },
          "Form_ITR6": {
            "field_required": [
              {
                "name": "FormName",
                "type": "str",
                "cast": "to_str",
                "allow_blank": false,
                "transform": "to_upper",
                "default_enabled": false,
                "default_value": null
              },
              {
                "name": "AssessmentYear",
                "type": "str",
                "cast": "to_str",
                "allow_blank": false,
                "transform": null,
                "default_enabled": false,
                "default_value": null
              }
            ]
          },
          "PartA_GEN1": {
            "node_required": {
              "OrgFirmInfo": {
                "field_required": [
                  {
                    "name": "PAN",
                    "type": "str",
                    "cast": "to_str",
                    "allow_blank": false,
                    "transform": "to_upper",
                    "default_enabled": false,
                    "default_value": null
                  }
                ],
                "node_required": {
                  "Address": {
                    "field_required": [
                      {
                        "name": "CityOrTownOrDistrict",
                        "type": "str",
                        "cast": "to_str",
                        "allow_blank": false,
                        "transform": null,
                        "default_enabled": false,
                        "default_value": null
                      },
                      {
                        "name": "CountryCode",
                        "type": "str",
                        "cast": "to_str",
                        "allow_blank": false,
                        "transform": "to_upper",
                        "default_enabled": false,
                        "default_value": null
                      }
                    ]
                  },
                  "ContactInfo": {
                    "field_optional": [
                      {
                        "name": "EmailAddress",
                        "type": "str",
                        "cast": "to_str",
                        "allow_blank": false,
                        "transform": "to_upper",
                        "default_enabled": false,
                        "default_value": null
                      }
                    ]
                  },
                  "AddressContact": {
                    "field_optional": [
                      {
                        "name": "MobileNo",
                        "type": "str",
                        "cast": "to_str",
                        "allow_blank": false,
                        "transform": null,
                        "default_enabled": false,
                        "default_value": null
                      }
                    ]
                  }
                }
              }
            }
          }
        }'::jsonb,
        'seed_v1_0_itr6_basic',
        '{"valid": true, "errors": []}'::jsonb,
        'seed_script',
        'seed_script'
    )
    RETURNING id, form_type, version_major, version_minor
)
INSERT INTO payload_structure_audit (
    structure_id,
    form_type,
    version_major,
    version_minor,
    change_type,
    json_path,
    old_value,
    new_value,
    changed_by,
    request_id
)
SELECT
    id,
    form_type,
    version_major,
    version_minor,
    'create',
    '$',
    NULL,
    '{"seed": true}'::jsonb,
    'seed_script',
    'seed_001'
FROM inserted;

COMMIT;
