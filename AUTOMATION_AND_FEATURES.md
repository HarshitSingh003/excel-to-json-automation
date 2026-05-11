# What this repo automates (short)

## What you automated

- **Single point**: You automated the full flow by taking values from Excel config, generating payload from DB-driven structure, and exposing it through API endpoints (draft → validate → activate → generate).
- **Excel → JSON**: Read the workbook and build data from the sheet config (like the old excel flow), then turn it into the final payload.
- **Rules from DB**: The shape of the output (nodes, fields, types) comes from the database, not only from code.
- **Versions**: You can work in **draft**, **validate**, then **activate** so changes are controlled.
- **Business checks**: After building the payload, the same style of **business error** checks as before can run on the file. (NOT CHECKED PROPERLY)

## Main features (simple list)

| Feature | What it does |
|--------|----------------|
| **API** | Create drafts, update nodes, validate, activate, generate JSON from data or from Excel. |
| **Form type** | You can pass **`form_type`** on requests (default is still `ITR6_BASIC`). |
| **Excel path** | **`/generate-from-excel`** and **`/excel-to-json`** use your Excel file path. |
| **Dynamic extras** | New keys or small nodes from Excel that are not yet in the DB schema can still appear in the output (pass-through), until you model them properly in DB. |
| **Outputs** | Generated JSON can be saved under **`outputs/`** (that folder is ignored by git). |
| **Bundles** | Tools to build / load **missing nodes** bundles for syncing structure. |

## One line summary

**This repo automates: Excel in → payload generation using structure picked from DB → validation/business checks/version flow (draft, validate, activate) → final structured JSON out.**



main path -> generate-from-excel

{
"file_path":"D:/Mobifly2/main_excel.xlsx",
"form_type":"ITR6_BASIC"
}