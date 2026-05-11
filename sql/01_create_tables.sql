BEGIN;

CREATE TABLE IF NOT EXISTS payload_structure (
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
ON payload_structure (form_type)
WHERE is_active = TRUE;

CREATE INDEX IF NOT EXISTS ix_payload_structure_form_status
ON payload_structure (form_type, status);

CREATE TABLE IF NOT EXISTS payload_structure_audit (
    id BIGSERIAL PRIMARY KEY,
    structure_id BIGINT NOT NULL REFERENCES payload_structure(id),
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
ON payload_structure_audit (structure_id);

CREATE INDEX IF NOT EXISTS ix_payload_structure_audit_form_version
ON payload_structure_audit (form_type, version_major, version_minor);

CREATE TABLE IF NOT EXISTS generated_payload (
    id BIGSERIAL PRIMARY KEY,
    form_type TEXT NOT NULL,
    structure_id BIGINT NOT NULL REFERENCES payload_structure(id),
    version_major INT NOT NULL,
    version_minor INT NOT NULL,
    payload_json JSONB NOT NULL,
    generated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS ix_generated_payload_form_time
ON generated_payload (form_type, generated_at DESC);

COMMIT;
