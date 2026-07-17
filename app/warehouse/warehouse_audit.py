import json
from pathlib import Path


def create_audit_report(table_name, rows_loaded, quality_score):

    report = {
        "table_name": table_name,
        "rows_loaded": rows_loaded,
        "quality_score": quality_score,
    }

    output_path = Path("reports/warehouse/audit") / f"{table_name}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:

        json.dump(report, file, indent=4)
