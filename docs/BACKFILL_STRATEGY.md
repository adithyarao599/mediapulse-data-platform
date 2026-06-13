# Backfill Strategy

Purpose:

Recover historical data.

Use Cases:

- DAG failure
- Reprocessing
- Historical loads

Command:

airflow dags backfill \
streaming_platform \
-s 2026-01-01 \
-e 2026-01-31
