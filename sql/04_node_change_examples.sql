-- Run in demo_one_form database (public schema).
SET search_path TO public;

-- ============================================
-- A) Create draft from current active version
-- ============================================
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
    'draft_hash_manual_change',
    '{"valid": false, "errors": ["Draft not validated yet"]}'::jsonb,
    'pgadmin_user',
    'pgadmin_user'
FROM public.payload_structure
WHERE form_type = 'ITR6_BASIC'
  AND is_active = TRUE
ON CONFLICT (form_type, version_major, version_minor) DO NOTHING;

-- ============================================
-- B) Example change: add new node
-- Path: PartA_GEN1.OrgFirmInfo.AddressContact
-- ============================================
UPDATE public.payload_structure
SET schema_json = jsonb_set(
    schema_json,
    '{PartA_GEN1,node_required,OrgFirmInfo,node_required,AddressContact}',
    '{
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
    }'::jsonb,
    true
),
updated_by = 'pgadmin_user',
updated_at = NOW()
WHERE form_type = 'ITR6_BASIC'
  AND status = 'draft';

-- ============================================
-- C) Mark draft validated
-- ============================================
UPDATE public.payload_structure
SET status = 'validated',
    validation_report = '{"valid": true, "errors": []}'::jsonb,
    updated_by = 'pgadmin_user',
    updated_at = NOW()
WHERE form_type = 'ITR6_BASIC'
  AND status = 'draft';

-- ============================================
-- D) Activate latest validated version
-- ============================================
BEGIN;
UPDATE public.payload_structure
SET is_active = FALSE
WHERE form_type = 'ITR6_BASIC';

UPDATE public.payload_structure
SET is_active = TRUE,
    status = 'active',
    updated_by = 'pgadmin_user',
    updated_at = NOW()
WHERE id = (
    SELECT id
    FROM public.payload_structure
    WHERE form_type = 'ITR6_BASIC' AND status = 'validated'
    ORDER BY version_major DESC, version_minor DESC
    LIMIT 1
);
COMMIT;

-- ============================================
-- E) Verify active structure version
-- ============================================
SELECT id, form_type, version_major, version_minor, status, is_active
FROM public.payload_structure
WHERE form_type = 'ITR6_BASIC'
ORDER BY version_major DESC, version_minor DESC;
