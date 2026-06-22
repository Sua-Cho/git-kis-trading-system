from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

APP_KEY = os.getenv("VTS_APPKEY")
APP_SECRET = os.getenv("VTS_APPSECRET")

url = "https://openapivts.koreainvestment.com:29443/oauth2/Approval"

payload = {
    "grant_type": "client_credentials",
    "appkey": APP_KEY,
    "secretkey": APP_SECRET
}

headers = {
    "content-type": "application/json"
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

print(response.json())

