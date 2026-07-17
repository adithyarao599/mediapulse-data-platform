import json
from pathlib import Path


def create_report(dataset, row_count, score):

    report = {"dataset": dataset, "rows": row_count, "quality_score": score}

    output_path = Path("reports/silver") / f"{dataset}_quality.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:

        json.dump(report, file, indent=4)
