# one_form_repo

Minimal optimized repository for **one form** JSON payload generation with DB-managed structure.

## What this contains

- Versioned structure storage in PostgreSQL (`jsonb`)
- Draft -> validate -> activate workflow
- Safe transform registry (no dynamic eval)
- Recursive payload generation for one form (`ITR6_BASIC`)
- SQL scripts for create + insert + activation

## Project tree

- `sql/01_create_tables.sql`
- `sql/02_seed_data.sql`
- `src/db.py`
- `src/transform_registry.py`
- `src/schema_validator.py`
- `src/structure_service.py`
- `src/payload_generator_one_form.py`
- `src/demo_run.py`

## Dependencies

```powershell
pip install psycopg2-binary jsonschema fastapi uvicorn
```

## Environment variables

Set these in PowerShell before running:

```powershell
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="postgres"
$env:PGUSER="postgres"
$env:PGPASSWORD="your_password"
```

## Run DB scripts

```powershell
cd D:\Mobifly2\one_form_repo
psql -h $env:PGHOST -p $env:PGPORT -U $env:PGUSER -d $env:PGDATABASE -f .\sql\01_create_tables.sql
psql -h $env:PGHOST -p $env:PGPORT -U $env:PGUSER -d $env:PGDATABASE -f .\sql\02_seed_data.sql
```

## Run demo

```powershell
python .\src\demo_run.py
```

## Run API server

```powershell
cd D:\Mobifly2\one_form_repo
uvicorn src.api_server:app --reload --host 127.0.0.1 --port 8000
```

Swagger:
- http://127.0.0.1:8000/docs

## Excel to JSON flow

Use endpoint `POST /excel-to-json` (single API) with:

```json
{
  "file_path": "D:\\Mobifly2\\one_form_repo\\sample.xlsx"
}
```

Excel reads named ranges first:
- `SWVersionNo`, `SWCreatedBy`, `FormName`, `AssessmentYear`, `PAN`, `CityOrTownOrDistrict`, `CountryCode`, `EmailAddress`

Fallback (if named ranges not present):
- `Sheet1!B1..B8` in the same order.

## Where generated JSON is saved

When you call `POST /generate`, JSON is saved in:

- DB table: `public.generated_payload.payload_json`
- File (latest): `D:\Mobifly2\one_form_repo\outputs\latest_payload.json`
- File (archive): `D:\Mobifly2\one_form_repo\outputs\payload_<id>_<timestamp>.json`

The same save behavior applies to `POST /excel-to-json`.

## One API you need

- `POST /excel-to-json`
  - Reads Excel
  - runs legacy-exact extraction and payload generation flow
  - stores JSON in DB + files

## Move legacy nodes one-by-one

Use this flow:
1. `POST /draft` (create draft)
2. `POST /migrate-root-node` (move one root node from old repo)
3. repeat step 2 for each node you want
4. `POST /validate`
5. `POST /activate`
6. `POST /excel-to-json`

`POST /migrate-root-node` body example:

```json
{
  "draft_id": 12,
  "node_name": "PartA_GEN2For6",
  "legacy_repo_path": "D:\\Mobifly2\\excelToJson\\excelToJson\\excelToJson\\excelToJson"
}
```

Current migrator notes:
- Converts old tuple fields to object-based schema
- Maps common cast/transform names to current registry
- Includes legacy `cm_field_map` and `cm_node_map`
- Includes legacy rules from `transform_settings.CHECK_DEF_AND_SET` via `__rules__.check_def_and_set`

## Missing nodes bundle (full-fidelity)

Build missing nodes file (legacy roots not yet in active DB schema):

```json
POST /build-missing-nodes-bundle
{
  "legacy_repo_path": "D:\\Mobifly2\\excelToJson\\excelToJson\\excelToJson\\excelToJson",
  "form_type": "ITR6_BASIC",
  "output_file": "D:\\Mobifly2\\one_form_repo\\missing_nodes_bundle.json"
}
```

Load file into DB as a new draft and activate:

```powershell
cd D:\Mobifly2\one_form_repo
python -m src.load_missing_nodes_to_db --bundle-file "D:\Mobifly2\one_form_repo\missing_nodes_bundle.json" --form-type ITR6_BASIC --actor bundle_loader --activate
```

Or use one API endpoint:

```json
POST /load-missing-nodes-bundle
{
  "bundle_file": "D:\\Mobifly2\\one_form_repo\\missing_nodes_bundle.json",
  "form_type": "ITR6_BASIC",
  "actor": "bundle_loader",
  "activate": true
}
```

## Parity check with legacy

```json
POST /parity-check
{
  "excel_file_path": "D:\\Mobifly2\\excelToJson\\excelToJson\\excelToJson\\excelToJson\\excel_file.xlsx",
  "legacy_repo_path": "D:\\Mobifly2\\excelToJson\\excelToJson\\excelToJson\\excelToJson",
  "form_type": "ITR6_BASIC"
}
```

## Full legacy sync (no missing/partial)

This endpoint overwrites root nodes from legacy `payload_config` into a new draft and can activate it:

```json
POST /sync-full-legacy
{
  "legacy_repo_path": "D:\\Mobifly2\\excelToJson\\excelToJson\\excelToJson\\excelToJson",
  "form_type": "ITR6_BASIC",
  "actor": "legacy_sync",
  "activate": true
}
```

## Change/add node process (without code changes)

Run SQL examples from:
- `sql/04_node_change_examples.sql`

Then call `POST /excel-to-json` again. Output JSON changes automatically based on active schema version.
