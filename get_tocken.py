from dotenv import load_dotenv
import os

load_dotenv()

APP_KEY = os.getenv("VTS_APPKEY")
APP_SECRET = os.getenv("VTS_APPSECRET")
CANO = os.getenv("VTS_CANO")
ACNT_PRDT_CD = os.getenv("VTS_ACNT_PRDT_CD")


import requests
import json

url = "https://openapivts.koreainvestment.com:29443/oauth2/tokenP"

payload = json.dumps({
  "grant_type": "client_credentials",
  "appkey": APP_KEY,
  "appsecret": APP_SECRET
})
headers = {
  'content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
