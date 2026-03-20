# 🚀 Data Quality & Observability Pipeline (AWS)

## 📌 Overview
This project demonstrates a production-grade serverless data pipeline using AWS with real-time API ingestion and built-in data quality validation.

## 🏗 Architecture
Lambda → S3 (Raw) → Glue → S3 (Processed - Parquet) → Athena

## 💡 Problem Statement
In real-world systems, data from APIs can be inconsistent, duplicated, or invalid. This project ensures only clean, validated data is stored for analytics.

## 🛠 Tech Stack
- Python
- AWS Lambda
- AWS S3
- AWS Glue (PySpark)
- AWS Athena
- CloudWatch

## 📂 Data Lake Structure
s3://debanjan-data-pipeline-project/
 ├── raw/
 ├── processed/year=YYYY/month=MM/day=DD/
 └── logs/

## ⚙️ Data Quality Checks
- Removed null values
- Removed duplicates
- Applied range validation on temperature

## 📊 Observability
- Record count tracking
- Logs available in CloudWatch

## ▶️ How to Run
1. Deploy Lambda (API ingestion)
2. Run Glue job (transformation + validation)
3. Query using Athena

## 📊 Sample Query
SELECT city, temperature FROM processed_data WHERE year = 2026;

## 💡 Why this project?
- Simulates real-world data engineering pipeline
- Handles unreliable API data
- Ensures data quality before analytics
- Uses scalable serverless architecture
