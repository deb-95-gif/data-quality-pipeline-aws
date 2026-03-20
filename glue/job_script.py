from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, dayofmonth, current_date

spark = SparkSession.builder.appName("DataQualityPipeline").getOrCreate()

INPUT_PATH = "s3://debanjan-data-pipeline-project/raw/"
OUTPUT_PATH = "s3://debanjan-data-pipeline-project/processed/"

df = spark.read.option("header", True).csv(INPUT_PATH, inferSchema=True)

total_records = df.count()

clean_df = (
    df.dropDuplicates(["timestamp"])
      .dropna()
      .filter((col("temperature") > -50) & (col("temperature") < 60))
)

clean_records = clean_df.count()

print(f"Total records: {total_records}")
print(f"Clean records: {clean_records}")

clean_df = clean_df.withColumn("ingestion_date", current_date())
clean_df = clean_df.withColumn("year", year(col("ingestion_date")))
clean_df = clean_df.withColumn("month", month(col("ingestion_date")))
clean_df = clean_df.withColumn("day", dayofmonth(col("ingestion_date")))

clean_df.write.mode("overwrite") \
    .partitionBy("year", "month", "day") \
    .parquet(OUTPUT_PATH)
