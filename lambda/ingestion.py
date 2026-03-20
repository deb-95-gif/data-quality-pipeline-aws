import boto3
import requests
import pandas as pd
from datetime import datetime
import os

s3 = boto3.client("s3")

BUCKET = "debanjan-data-pipeline-project"
API_KEY = os.getenv("API_KEY")
CITY = "Guwahati"

def lambda_handler(event, context):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    record = {
        "city": CITY,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    df = pd.DataFrame([record])

    file_name = f"raw/weather_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    df.to_csv("/tmp/data.csv", index=False)
    s3.upload_file("/tmp/data.csv", BUCKET, file_name)

    return {"statusCode": 200, "body": "Weather data ingested"}
