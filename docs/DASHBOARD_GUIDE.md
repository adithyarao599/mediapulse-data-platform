# Dashboard Guide

## Executive Dashboard

Audience:

Executive Leadership

Purpose:

Provide a high-level overview of business performance.

KPIs:

* Revenue
* Views
* Streams
* Engagement Score
* Top Artist
* Top Genre

Refresh Frequency:

Daily

Data Source:

PostgreSQL Warehouse

Fact Table:

fact_content_performance

Dimensions:

* dim_artist
* dim_genre
* dim_country
* dim_date

## Artist Performance Dashboard

Audience:

Content Team

Purpose:

Identify top-performing artists.

KPIs:

* Artist Revenue
* Artist Streams
* Artist Engagement

Refresh:

Daily

## Genre Intelligence Dashboard

Audience:

Marketing Team

Purpose:

Analyze genre growth and revenue contribution.

KPIs:

* Genre Revenue
* Genre Streams
* Genre Engagement

## Geographic Analytics Dashboard

Audience:

Regional Teams

Purpose:

Analyze global consumption trends.

KPIs:

* Country Views
* Country Revenue
* Country Streams

## Revenue Dashboard

Audience:

Finance Team

Purpose:

Monitor monetization performance.

KPIs:

* Revenue
* RPM
* Revenue Growth

## Recommendation Dashboard

Audience:

ML Team

Purpose:

Monitor recommendation engine outputs.

KPIs:

* Recommendation Score
* Trend Score
* Engagement Score
