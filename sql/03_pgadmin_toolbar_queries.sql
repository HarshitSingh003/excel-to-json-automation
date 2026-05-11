-- Run this full script in pgAdmin Query Tool.
-- It creates/uses DB demo_one_form and objects in public schema only.

-- 1) Create DB once (ignore error if already exists).
-- NOTE: In pgAdmin, run this section while connected to postgres DB.
CREATE DATABASE demo_one_form;

-- 2) Reconnect Query Tool to demo_one_form, then run below.
SET search_path TO public;

CREATE TABLE IF NOT EXISTS public.payload_structure (
    id BIGSERIAL PRIMARY KEY,
    form_type TEXT NOT NULL,
    version_major INT NOT NULL CHECK (version_major >= 1),
    version_minor INT NOT NULL CHECK (version_minor >= 0),
    status TEXT NOT NULL CHECK (status IN ('draft', 'validated', 'active', 'deprecated')),
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    schema_json JSONB NOT NULL,
    schema_hash TEXT NOT NULL,
    validation_report JSONB,
    created_by TEXT NOT NULL,
    updated_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE (form_type, version_major, version_minor)
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_payload_structure_one_active_per_form
ON public.payload_structure (form_type)
WHERE is_active = TRUE;

CREATE INDEX IF NOT EXISTS ix_payload_structure_form_status
ON public.payload_structure (form_type, status);

CREATE TABLE IF NOT EXISTS public.payload_structure_audit (
    id BIGSERIAL PRIMARY KEY,
    structure_id BIGINT NOT NULL REFERENCES public.payload_structure(id),
    form_type TEXT NOT NULL,
    version_major INT NOT NULL,
    version_minor INT NOT NULL,
    change_type TEXT NOT NULL,
    json_path TEXT NOT NULL,
    old_value JSONB,
    new_value JSONB,
    changed_by TEXT NOT NULL,
    changed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    request_id TEXT
);

CREATE INDEX IF NOT EXISTS ix_payload_structure_audit_structure_id
ON public.payload_structure_audit (structure_id);

CREATE INDEX IF NOT EXISTS ix_payload_structure_audit_form_version
ON public.payload_structure_audit (form_type, version_major, version_minor);

CREATE TABLE IF NOT EXISTS public.generated_payload (
    id BIGSERIAL PRIMARY KEY,
    form_type TEXT NOT NULL,
    structure_id BIGINT NOT NULL REFERENCES public.payload_structure(id),
    version_major INT NOT NULL,
    version_minor INT NOT NULL,
    payload_json JSONB NOT NULL,
    generated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS ix_generated_payload_form_time
ON public.generated_payload (form_type, generated_at DESC);

-- 3) Seed one active version for one form.
INSERT INTO public.payload_structure (
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
          {"name":"SWVersionNo","type":"str","cast":"to_str","allow_blank":false,"transform":null,"default_enabled":false,"default_value":null},
          {"name":"SWCreatedBy","type":"str","cast":"to_str","allow_blank":false,"transform":"to_upper","default_enabled":false,"default_value":null}
        ]
      },
      "Form_ITR6": {
        "field_required": [
          {"name":"FormName","type":"str","cast":"to_str","allow_blank":false,"transform":"to_upper","default_enabled":false,"default_value":null},
          {"name":"AssessmentYear","type":"str","cast":"to_str","allow_blank":false,"transform":null,"default_enabled":false,"default_value":null}
        ]
      },
      "PartA_GEN1": {
        "node_required": {
          "OrgFirmInfo": {
            "field_required": [
              {"name":"PAN","type":"str","cast":"to_str","allow_blank":false,"transform":"to_upper","default_enabled":false,"default_value":null}
            ],
            "node_required": {
              "Address": {
                "field_required": [
                  {"name":"CityOrTownOrDistrict","type":"str","cast":"to_str","allow_blank":false,"transform":null,"default_enabled":false,"default_value":null},
                  {"name":"CountryCode","type":"str","cast":"to_str","allow_blank":false,"transform":"to_upper","default_enabled":false,"default_value":null}
                ]
              },
              "ContactInfo": {
                "field_optional": [
                  {"name":"EmailAddress","type":"str","cast":"to_str","allow_blank":false,"transform":"to_upper","default_enabled":false,"default_value":null}
                ]
              },
              "AddressContact": {
                "field_optional": [
                  {"name":"MobileNo","type":"str","cast":"to_str","allow_blank":false,"transform":null,"default_enabled":false,"default_value":null}
                ]
              }
            }
          }
        }
      }
    }'::jsonb,
    'seed_v1_0_itr6_basic',
    '{"valid": true, "errors": []}'::jsonb,
    'pgadmin_seed',
    'pgadmin_seed'
)
ON CONFLICT (form_type, version_major, version_minor) DO NOTHING;

-- 4) Audit seed create row.
INSERT INTO public.payload_structure_audit (
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
    ps.id,
    ps.form_type,
    ps.version_major,
    ps.version_minor,
    'create',
    '$',
    NULL,
    '{"seed":true}'::jsonb,
    'pgadmin_seed',
    'seed_001'
FROM public.payload_structure ps
WHERE ps.form_type = 'ITR6_BASIC'
  AND ps.version_major = 1
  AND ps.version_minor = 0
  AND NOT EXISTS (
      SELECT 1
      FROM public.payload_structure_audit a
      WHERE a.structure_id = ps.id
        AND a.change_type = 'create'
  );

-- 5) Create a draft copy from active version (v1.1).
INSERT INTO public.payload_structure (
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
SELECT
    form_type,
    version_major,
    version_minor + 1,
    'draft',
    FALSE,
    schema_json,
    'draft_hash_v1_1',
    '{"valid": false, "errors": ["Draft not validated yet"]}'::jsonb,
    'pgadmin_user',
    'pgadmin_user'
FROM public.payload_structure
WHERE form_type = 'ITR6_BASIC'
  AND is_active = TRUE
ON CONFLICT (form_type, version_major, version_minor) DO NOTHING;

-- 6) Example: Update one node in draft (Form_ITR6 -> add SchemaVer field).
UPDATE public.payload_structure
SET schema_json = jsonb_set(
    schema_json,
    '{Form_ITR6,field_required}',
    (
      schema_json #> '{Form_ITR6,field_required}'
    ) || '[{"name":"SchemaVer","type":"str","cast":"to_str","allow_blank":false,"transform":null,"default_enabled":false,"default_value":null}]'::jsonb,
    true
),
updated_by = 'pgadmin_user',
updated_at = NOW()
WHERE form_type = 'ITR6_BASIC'
  AND version_major = 1
  AND version_minor = 1
  AND status = 'draft';

-- 7) Mark draft validated.
UPDATE public.payload_structure
SET status = 'validated',
    validation_report = '{"valid": true, "errors": []}'::jsonb,
    updated_by = 'pgadmin_user',
    updated_at = NOW()
WHERE form_type = 'ITR6_BASIC'
  AND version_major = 1
  AND version_minor = 1
  AND status = 'draft';

-- 8) Activate validated draft (transaction-safe).
BEGIN;
UPDATE public.payload_structure
SET is_active = FALSE
WHERE form_type = 'ITR6_BASIC';

UPDATE public.payload_structure
SET is_active = TRUE,
    status = 'active',
    updated_by = 'pgadmin_user',
    updated_at = NOW()
WHERE form_type = 'ITR6_BASIC'
  AND version_major = 1
  AND version_minor = 1
  AND status = 'validated';
COMMIT;

-- 9) Quick verify.
SELECT id, form_type, version_major, version_minor, status, is_active
FROM public.payload_structure
WHERE form_type = 'ITR6_BASIC'
ORDER BY version_major DESC, version_minor DESC;

-- 10) View generated JSON rows.
SELECT id, form_type, structure_id, version_major, version_minor, generated_at
FROM public.generated_payload
ORDER BY id DESC;
