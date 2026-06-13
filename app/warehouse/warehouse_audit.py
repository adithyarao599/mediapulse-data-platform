import json


def create_audit_report(table_name, rows_loaded, quality_score):

    report = {
        "table_name": table_name,
        "rows_loaded": rows_loaded,
        "quality_score": quality_score,
    }

    with open(f"reports/warehouse/" f"audit/" f"{table_name}.json", "w") as file:

        json.dump(report, file, indent=4)
