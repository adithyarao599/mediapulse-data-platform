# reports/

**Who this is for:** anyone running the MediaPulse pipeline locally, or reviewing this repo.

Everything under `reports/` other than this file is **generated output**, written at
pipeline run time by code such as:

- `app/silver/quality_report.py::create_report()` → `reports/silver/<dataset>_quality.json`
- `app/warehouse/reconciliation.py::generate_reconciliation()` → `reports/warehouse/reconciliation.json`
- `app/warehouse/warehouse_audit.py::create_audit_report()` → `reports/warehouse/audit/<table>.json`

## Why nothing else is committed here

Earlier versions of this repository committed two **hand-written, static** JSON files
(`reports/gold/gold_quality_report.json`, `reports/ml/model_metrics.json`) that looked
like real pipeline output but were never produced by any code in the repo — no gold or
ML report-writer function existed. That's a trust problem: a report file is a claim
about what a pipeline run actually measured, and a fabricated one is indistinguishable
from a real one until someone checks.

The rule going forward: **if a JSON file under `reports/` is meaningful, there must be
a function in `app/` that produces it, and the file itself is `.gitignore`d** — regenerate
it by running the pipeline, don't hand-edit or commit it. See `.gitignore` for the rule
enforcing this.

## How to maintain this doc

Add a bullet above whenever a new report-writer function is added anywhere in `app/`,
so this file stays an accurate index of "what generates what."
