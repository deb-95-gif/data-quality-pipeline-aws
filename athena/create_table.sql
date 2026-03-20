CREATE EXTERNAL TABLE IF NOT EXISTS processed_data (
  city STRING,
  temperature DOUBLE,
  humidity INT,
  pressure INT,
  weather STRING,
  timestamp STRING
)
PARTITIONED BY (year INT, month INT, day INT)
STORED AS PARQUET
LOCATION 's3://debanjan-data-pipeline-project/processed/';
