# Database Migrations

**Who this is for:** anyone changing the warehouse schema (adding/removing a
column, a table, a constraint) or setting up a fresh database locally.

**How it should be maintained:** every schema change goes through a new
Alembic revision, generated from the ORM models in `app/models/`, reviewed by
a human, and committed alongside the model change in the same PR. Never edit
a table in Postgres by hand and never hand-write DDL outside this workflow -
see "Why this exists" below for why that matters.

## Why this exists

Earlier versions of this repository had two disconnected descriptions of the
warehouse schema: `app/warehouse/schema.sql` (which only ran
`CREATE SCHEMA IF NOT EXISTS streaming_dw;` and defined no tables) and the
real schema, which only existed as SQLAlchemy models in `app/models/`. There
was no tool reconciling the two, so `schema.sql` silently went stale the
first time a model changed. It has been removed - **Alembic migrations under
`migrations/versions/` are now the single source of truth for warehouse DDL.**

## Quick reference

All commands assume the same `POSTGRES_*` environment variables the app
already uses (see `.env.example`) are exported, or that you have a `.env`
file in the repo root (loaded automatically by `app/config/settings.py`).

```bash
# Apply every migration that hasn't run yet against the current database
alembic upgrade head

# Roll back the most recent migration
alembic downgrade -1

# Roll back everything (drops all warehouse tables, keeps the tracking table)
alembic downgrade base

# See what's pending / what's already applied
alembic current
alembic history
```

## Changing the schema

1. Edit (or add) a model in `app/models/`. If it's a new model file, import
   it in `app/models/__init__.py` too - that's the single place
   `Base.metadata` (and therefore Alembic) learns a table exists.
2. Generate a draft migration by diffing your models against a real,
   up-to-date database:
   ```bash
   alembic revision --autogenerate -m "add loudness column to fact_content_performance"
   ```
3. **Open the generated file in `migrations/versions/` and read it.**
   Autogenerate is a diffing tool, not an oracle - it reliably detects added/
   removed tables and columns, but it cannot tell a column rename from a
   "drop one column, add a different one" (you'll see a spurious drop +
   add - fix it into a rename if that's what actually happened), and it
   never writes data migrations (backfilling a new NOT NULL column, for
   example) for you.
4. Run it locally and confirm both directions work:
   ```bash
   alembic upgrade head
   alembic downgrade -1   # should cleanly undo it
   alembic upgrade head   # and this should cleanly redo it
   ```
5. Commit the migration file together with the model change that caused it.

## Why a non-default Postgres schema (`streaming_dw`), and the one gotcha it creates

All warehouse tables live in the `streaming_dw` Postgres schema rather than
the default `public` schema (`app/core/database.py` sets this once via
`MetaData(schema="streaming_dw")`, so every model inherits it automatically).
This mirrors how real warehouses are organized - separate schemas per
domain/team/environment inside one database, rather than one flat
`public` namespace.

The one consequence: Alembic's own bookkeeping table (`alembic_version`,
which records which migrations have run) is configured to live inside
`streaming_dw` too, for the same "keep everything about this schema together"
reason. On a **brand new, empty database**, that schema doesn't exist yet,
so Alembic would fail trying to create its own tracking table before any
migration has run. `migrations/env.py` handles this by issuing
`CREATE SCHEMA IF NOT EXISTS streaming_dw` once, directly, before handing
control to Alembic - every actual table still only ever comes from a
versioned migration.

## Local bootstrap (no history needed)

For a throwaway local database where you don't care about migration
history - e.g. a fresh CI Postgres container - `app/warehouse/create_tables.py`
still works as a one-shot `Base.metadata.create_all()`. It is **not** a
substitute for Alembic on any database that already has data or has been
deployed anywhere, since `create_all()` can only create missing tables, never
alter or safely evolve an existing one.
