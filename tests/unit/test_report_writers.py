import json

from app.silver.quality_report import create_report
from app.warehouse.reconciliation import generate_reconciliation
from app.warehouse.warehouse_audit import create_audit_report


def test_create_report_creates_missing_parent_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_report(dataset="spotify_silver", row_count=1000, score=97.5)

    output_file = tmp_path / "reports" / "silver" / "spotify_silver_quality.json"
    assert output_file.exists()

    contents = json.loads(output_file.read_text())
    assert contents == {
        "dataset": "spotify_silver",
        "rows": 1000,
        "quality_score": 97.5,
    }


def test_generate_reconciliation_creates_missing_parent_directory(
    tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)

    generate_reconciliation(source_rows=1000, loaded_rows=998)

    output_file = tmp_path / "reports" / "warehouse" / "reconciliation.json"
    assert output_file.exists()

    contents = json.loads(output_file.read_text())
    assert contents == {
        "source_rows": 1000,
        "loaded_rows": 998,
        "difference": 2,
    }


def test_create_audit_report_creates_missing_parent_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    create_audit_report(
        table_name="fact_content_performance", rows_loaded=5000, quality_score=98.2
    )

    output_file = (
        tmp_path / "reports" / "warehouse" / "audit" / "fact_content_performance.json"
    )
    assert output_file.exists()

    contents = json.loads(output_file.read_text())
    assert contents == {
        "table_name": "fact_content_performance",
        "rows_loaded": 5000,
        "quality_score": 98.2,
    }
