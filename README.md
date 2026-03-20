# Data Quality & Observability Pipeline (AWS)

## Overview
Production-grade serverless data pipeline with real-time API ingestion.

## Architecture
Lambda → S3 → Glue → S3 → Athena

## Tech Stack
- Python
- AWS Lambda
- S3
- Glue (PySpark)
- Athena

## Features
- Real-time API ingestion (weather)
- Data validation
- Partitioned Parquet storage
- Query-ready dataset

## How to Run
1. Deploy Lambda
2. Run Glue job
3. Query via Athena
