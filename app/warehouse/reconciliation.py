import json
from pathlib import Path


def generate_reconciliation(source_rows, loaded_rows):

    report = {
        "source_rows": source_rows,
        "loaded_rows": loaded_rows,
        "difference": source_rows - loaded_rows,
    }

    output_path = Path("reports/warehouse/reconciliation.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:

        json.dump(report, file, indent=4)
