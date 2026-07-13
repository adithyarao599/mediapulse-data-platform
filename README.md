# MediaPulse Data Platform

<p align="center">
  <img src="assets/banners/mediapulse-banner.png" alt="MediaPulse Data Platform Banner" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-red?logo=apacheairflow)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-yellow?logo=powerbi)
![PyTest](https://img.shields.io/badge/PyTest-Tested-success?logo=pytest)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

<h3 align="center">
Enterprise Data Engineering & Analytics Platform for Multi-Platform Entertainment Intelligence
</h3>

---

## Overview

MediaPulse Data Platform is an enterprise-style data engineering project that demonstrates the complete lifecycle of modern analytical data processing—from raw data ingestion to business-ready dashboards.

The platform ingests entertainment datasets from multiple sources, validates and standardizes incoming data, applies Medallion Architecture transformations (Bronze, Silver, and Gold), loads curated datasets into a PostgreSQL dimensional warehouse, and prepares analytics-ready data for business intelligence using Power BI.

Rather than being a simple ETL pipeline, the project is designed to showcase production-inspired engineering practices including orchestration, modular architecture, testing, monitoring, data quality validation, and warehouse design.

---

## Business Problem

Entertainment platforms generate data from multiple independent systems.

These datasets often contain:

* Different schemas
* Missing values
* Duplicate records
* Inconsistent genre names
* Different date formats
* Platform-specific metadata

Without proper engineering, analysts spend significant time cleaning data instead of generating business insights.

MediaPulse solves this problem by building a reusable, automated analytics platform that transforms raw entertainment data into trusted, analytics-ready datasets.

---

## Business Objectives

The platform enables organizations to:

* Build reliable ETL pipelines
* Standardize heterogeneous datasets
* Improve data quality before analysis
* Create a scalable dimensional warehouse
* Generate executive KPIs
* Support business intelligence dashboards
* Prepare data for future machine learning workloads

---

## Key Features

* End-to-End ETL Pipeline
* Medallion Architecture (Bronze → Silver → Gold)
* PostgreSQL Dimensional Data Warehouse
* Apache Airflow Workflow Orchestration
* Automated Data Quality Validation
* Metadata Tracking
* Data Lineage Support
* Incremental Loading Framework
* Warehouse Monitoring
* Modular Python Architecture
* Automated Testing with PyTest
* Docker Support
* Power BI Integration
* Analytics-ready Data Models
* Feature Engineering Foundation for Machine Learning

---

## Architecture

MediaPulse Data Platform follows a layered enterprise data architecture inspired by modern analytics platforms used across media and entertainment organizations. The platform separates ingestion, transformation, orchestration, storage, and analytics into independent layers to improve scalability, maintainability, and data quality.

The architecture is built around the Medallion Architecture (Bronze, Silver, Gold), orchestrated with Apache Airflow and backed by a PostgreSQL dimensional warehouse.

---

## System Architecture

<p align="center">
<img src="assets/architecture/system-architecture.svg" width="100%">
</p>

The platform ingests entertainment datasets from multiple sources, processes them through a modular ETL pipeline, stores analytics-ready datasets in a PostgreSQL dimensional warehouse, and exposes business insights through Power BI dashboards.

### Architecture Highlights

* Multi-source batch data ingestion
* Layered Medallion Architecture
* Metadata-driven ETL
* Automated validation and quality checks
* Modular transformation pipeline
* PostgreSQL star-schema warehouse
* Workflow orchestration using Apache Airflow
* Analytics-ready Power BI integration

---

## End-to-End Data Flow

<p align="center">
<img src="assets/architecture/data-flow.svg" width="100%">
</p>

The MediaPulse pipeline follows a structured flow to ensure raw entertainment data is transformed into trusted business intelligence.

### Pipeline Stages

**1. Data Sources**

Entertainment datasets are collected from multiple publicly available platforms including Spotify, Netflix, YouTube, Movies, and Music Charts.

**2. Data Ingestion**

The ingestion engine validates files, records metadata, verifies checksums, and prepares raw datasets for downstream processing.

**3. Bronze Layer**

Raw data is preserved in its original structure while ingestion metadata and validation information are captured.

**4. Silver Layer**

Business rules, schema validation, standardization, deduplication, null handling, and quality checks produce clean analytical datasets.

**5. Gold Layer**

Business metrics, KPIs, aggregations, feature engineering, recommendation features, and executive analytics are generated.

**6. Data Warehouse**

Curated datasets are loaded into a PostgreSQL dimensional warehouse optimized for analytical queries.

**7. Business Intelligence**

Power BI consumes warehouse tables to produce interactive executive dashboards and analytical reports.

---

## Medallion Architecture

<p align="center">
<img src="assets/architecture/medallion-architecture.svg" width="100%">
</p>

MediaPulse adopts the Medallion Architecture to progressively improve data quality while maintaining traceability throughout the ETL lifecycle.

### Bronze Layer

Purpose:

* Preserve raw source data
* Capture ingestion metadata
* Validate incoming datasets
* Archive original files
* Enable reproducibility

Primary Modules

* Bronze Loader
* Metadata Writer
* Validation Services

---

### Silver Layer

Purpose:

* Standardize schemas
* Clean invalid records
* Remove duplicates
* Handle missing values
* Apply business rules
* Improve overall data quality

Primary Modules

* Standardizer
* Deduplicator
* Schema Validator
* Genre Mapper
* Date Standardizer
* Null Handler
* Quality Engine

---

### Gold Layer

Purpose:

* Generate business KPIs
* Produce analytical datasets
* Create feature engineering outputs
* Support dashboard reporting
* Prepare machine learning features

Primary Modules

* Executive KPIs
* Revenue Metrics
* Trend Intelligence
* Recommendation Features
* Dashboard Products
* Feature Store

---

## Data Warehouse Design

<p align="center">
<img src="assets/architecture/warehouse-schema.svg" width="100%">
</p>

The analytical warehouse follows a dimensional star schema designed to optimize reporting performance while simplifying business analysis.

### Fact Table

**Fact_Content_Performance**

Stores measurable business events and performance metrics used for reporting and analytics.

---

### Dimension Tables

* Dim_Artist
* Dim_Genre
* Dim_Country
* Dim_Platform
* Dim_Date
* Dim_Content

These dimensions provide descriptive context for analytical queries while reducing redundancy and improving query performance.

---

### Why a Star Schema?

MediaPulse uses a star schema because it:

* Simplifies analytical queries
* Improves Power BI performance
* Reduces join complexity
* Supports scalable business reporting
* Aligns with enterprise data warehouse best practices

---

## Technology Stack

| Layer                       | Technologies                      |
| --------------------------- | --------------------------------- |
| Programming Language        | Python 3                          |
| Data Processing             | Pandas, NumPy                     |
| Database                    | PostgreSQL                        |
| Data Warehouse              | Dimensional Star Schema           |
| Workflow Orchestration      | Apache Airflow                    |
| Data Quality                | Custom Validation Framework       |
| Machine Learning Foundation | Scikit-learn, Feature Engineering |
| Containerization            | Docker                            |
| Testing                     | PyTest                            |
| Version Control             | Git & GitHub                      |
| Business Intelligence       | Power BI                          |
| SQL                         | PostgreSQL                        |

---

## Architectural Principles

MediaPulse was designed around several engineering principles commonly used in enterprise data platforms:

* Modular and reusable ETL components
* Separation of ingestion, transformation, and analytics
* Layered data quality enforcement
* Metadata-driven processing
* Scalable dimensional warehouse design
* Automated workflow orchestration
* Testable and maintainable codebase
* Business-focused analytics delivery

---

# Enterprise ETL Pipeline

MediaPulse implements a modular Extract, Transform, Load (ETL) architecture designed around enterprise data engineering best practices. Rather than relying on a single monolithic script, each stage of the pipeline is independently responsible for ingestion, validation, transformation, analytics generation, and warehouse loading.

The pipeline follows a layered Medallion Architecture to progressively improve data quality while preserving traceability throughout the data lifecycle.

---

## Pipeline Workflow

The ETL process consists of the following stages:

### Step 1 — Data Ingestion

The ingestion engine reads entertainment datasets from multiple sources and performs initial validation before processing begins.

Primary Responsibilities:

* Source discovery
* File validation
* Metadata generation
* Checksum verification
* Version tracking
* Archive management

Key Modules

```text
app/ingestion/

base_ingestor.py

spotify_ingestor.py

netflix_ingestor.py

ingestion_engine.py

checksum.py

metadata_service.py

archive_manager.py

version_manager.py
```

---

### Step 2 — Bronze Layer

The Bronze layer stores raw source data while preserving the original structure.

Objectives

* Preserve source fidelity
* Track ingestion metadata
* Enable reproducibility
* Maintain audit history

Key Modules

```text
app/bronze/

bronze_loader.py

bronze_report.py
```

---

### Step 3 — Silver Layer

The Silver layer transforms raw data into standardized, validated datasets suitable for analytics.

Transformations include:

* Schema validation
* Null handling
* Duplicate removal
* Date normalization
* Genre mapping
* Business rule enforcement
* Standardization

Key Modules

```text
app/silver/

silver_pipeline.py

standardizer.py

schema_validator.py

deduplicator.py

genre_mapper.py

date_standardizer.py

null_handler.py

business_rules.py
```

---

### Step 4 — Gold Layer

The Gold layer generates analytics-ready datasets that power dashboards and downstream machine learning workflows.

Outputs include:

* Executive KPIs
* Trend analysis
* Revenue metrics
* Artist analytics
* Country analytics
* Recommendation features
* Feature engineering

Key Modules

```text
app/gold/

gold_pipeline.py

executive_kpis.py

genre_metrics.py

country_metrics.py

trend_intelligence.py

dashboard_products.py

feature_store.py
```

---

### Step 5 — Warehouse Loading

The transformed datasets are loaded into a PostgreSQL dimensional warehouse using surrogate keys and optimized relationships.

Responsibilities

* Dimension loading
* Fact loading
* Referential integrity
* Incremental loading
* Warehouse auditing
* Index management

Key Modules

```text
app/warehouse/

dimension_loader.py

fact_loader.py

incremental_loader.py

key_resolver.py

foreign_key_mapper.py

warehouse_validator.py

warehouse_monitor.py
```

---

### Step 6 — Business Intelligence

Curated warehouse tables serve as the single source of truth for interactive dashboards built in Power BI.

Business users consume:

* Executive KPIs
* Geographic insights
* Artist analytics
* Genre performance
* Trend analysis
* Platform comparison

---

## Repository Structure

The project is organized into independent modules to improve maintainability, scalability, and ease of development.

| Directory     | Purpose                           |
| ------------- | --------------------------------- |
| app/ingestion | Data ingestion framework          |
| app/bronze    | Raw data loading                  |
| app/silver    | Data cleansing and transformation |
| app/gold      | Business analytics generation     |
| app/warehouse | Warehouse loading and management  |
| app/models    | Warehouse schema definitions      |
| airflow       | Workflow orchestration            |
| tests         | Automated testing                 |
| sql           | Dashboard queries                 |
| deployment    | Deployment documentation          |
| docs          | Technical documentation           |
| assets        | Images, diagrams, and screenshots |

---

## Data Quality Framework

Reliable analytics require trustworthy data.

MediaPulse applies multiple validation layers before data reaches the warehouse.

Quality checks include:

* Schema validation
* Duplicate detection
* Missing value handling
* Checksum verification
* Business rule validation
* Metadata tracking
* Referential integrity validation
* Warehouse quality monitoring

This layered validation strategy improves confidence in downstream analytics and minimizes manual data correction.

---

## Metadata Management

Every ingestion cycle records operational metadata including:

* Dataset version
* Load timestamp
* File checksum
* Processing status
* Validation results
* Pipeline execution history

Metadata enables traceability, auditing, reproducibility, and future incremental loading strategies.

---

## Scalability Considerations

Although MediaPulse currently operates as a batch-processing platform, its modular architecture has been designed with future scalability in mind.

Potential production enhancements include:

* Streaming ingestion using Apache Kafka
* Cloud object storage integration
* Distributed processing with Apache Spark
* Cloud-native orchestration
* Data lake integration
* Automated lineage tracking
* Real-time analytics

---

## Technology Stack

| Category         | Technologies                |
| ---------------- | --------------------------- |
| Programming      | Python                      |
| Database         | PostgreSQL                  |
| Data Processing  | Pandas, NumPy               |
| Orchestration    | Apache Airflow              |
| Data Quality     | Custom Validation Framework |
| Testing          | PyTest                      |
| Containerization | Docker                      |
| Version Control  | Git & GitHub                |
| Visualization    | Power BI                    |
| SQL              | PostgreSQL                  |

---

# Engineering Decisions

MediaPulse was designed to reflect architectural patterns commonly found in modern enterprise data platforms. Every major technology and design decision was selected to balance simplicity, maintainability, scalability, and business value while remaining appropriate for a portfolio-scale implementation.

---

## Why Python?

Python was selected as the primary programming language due to its mature ecosystem for data engineering and analytics.

### Benefits

* Extensive data processing libraries
* Excellent PostgreSQL support
* Strong ecosystem for ETL development
* Readable and maintainable syntax
* Widely adopted across data engineering teams

Alternative Considered

* Java

Reason for choosing Python:

Python significantly reduces development complexity while providing excellent support for data processing, orchestration, and analytics workflows.

---

## Why PostgreSQL?

PostgreSQL serves as the analytical warehouse because it provides enterprise-grade relational database capabilities together with powerful SQL support.

### Benefits

* Mature relational database
* Strong analytical SQL capabilities
* ACID compliance
* Excellent compatibility with Power BI
* Reliable indexing and query optimization

Alternative Considered

* MySQL

Reason for choosing PostgreSQL:

PostgreSQL offers richer SQL functionality and is commonly used for analytical workloads and dimensional data warehouses.

---

## Why Apache Airflow?

Modern data platforms require workflow orchestration rather than manually executing scripts.

Apache Airflow was selected because it provides:

* Workflow scheduling
* Dependency management
* Retry mechanisms
* Monitoring
* Logging
* Scalable pipeline orchestration

Alternative Considered

* Cron jobs

Reason for choosing Airflow:

Cron is effective for simple scheduled tasks but lacks dependency management, monitoring, retries, and visualization. Airflow is purpose-built for complex data pipelines.

---

## Why Medallion Architecture?

The platform adopts a Bronze → Silver → Gold architecture to progressively improve data quality while preserving traceability.

### Bronze

Preserves raw source data.

### Silver

Applies validation, cleaning, standardization, and business rules.

### Gold

Produces trusted datasets optimized for reporting and analytics.

Benefits

* Clear separation of responsibilities
* Easier debugging
* Improved maintainability
* Reproducible processing
* Enterprise-aligned architecture

---

## Why a Star Schema?

Business intelligence workloads typically perform better when analytical data is organized using dimensional modeling.

The warehouse follows a star schema consisting of one central fact table surrounded by descriptive dimension tables.

Benefits

* Simplified SQL queries
* Faster analytical reporting
* Reduced join complexity
* Optimized Power BI performance
* Widely adopted enterprise design

---

## Why Modular ETL?

Instead of implementing a single monolithic pipeline, MediaPulse separates responsibilities into independent modules.

Benefits

* Improved maintainability
* Easier testing
* Better code reuse
* Independent development
* Simplified debugging
* Clear ownership of each processing stage

---

## Why Docker?

Containerization ensures that the platform can be executed consistently across different development environments.

Benefits

* Reproducible environments
* Simplified onboarding
* Dependency isolation
* Deployment consistency

---

## Design Principles

The platform was developed around the following engineering principles:

* Modularity over monolithic design
* Automation over manual execution
* Reproducibility over environment-specific configuration
* Data quality before analytics
* Scalability through layered architecture
* Maintainability through separation of concerns
* Business value through analytics-ready datasets

## Current Project Status

| Component              | Status         |
| ---------------------- | -------------- |
| Data Ingestion         | ✅ Complete     |
| Bronze Layer           | ✅ Complete     |
| Silver Layer           | ✅ Complete     |
| Gold Layer             | ✅ Complete     |
| PostgreSQL Warehouse   | ✅ Complete     |
| Airflow Pipelines      | ✅ Complete     |
| Data Quality Framework | ✅ Complete     |
| Automated Testing      | ✅ Complete     |
| Documentation          | 🚧 In Progress |
| Power BI Dashboard     | 🚧 In Progress |

---

## Repository Structure

> Repository structure documentation will be expanded with architecture diagrams and implementation details.

---

## Documentation Roadmap

The following sections will be added as the project documentation progresses:

* System Architecture
* Medallion Architecture
* ETL Pipeline Walkthrough
* Airflow Orchestration
* PostgreSQL Warehouse Design
* Star Schema
* SQL Analytics
* Power BI Dashboard
* Testing Strategy
* Deployment Guide
* Engineering Decisions
* Production Readiness
* Lessons Learned
* Future Enhancements

---

## Project Vision

MediaPulse is designed as a portfolio project that demonstrates enterprise data engineering principles commonly used in modern analytics platforms.

The long-term roadmap includes support for cloud-native deployment, streaming ingestion, infrastructure as code, and advanced analytics capabilities while maintaining a strong focus on software engineering best practices.

---

> **This README is actively being expanded as the project reaches production-ready status.**
