#주식잔고조회 
from dotenv import load_dotenv
import os

load_dotenv()

APP_KEY = os.getenv("VTS_APPKEY")
APP_SECRET = os.getenv("VTS_APPSECRET")
CANO = os.getenv("VTS_CANO")
ACNT_PRDT_CD = os.getenv("VTS_ACNT_PRDT_CD")

import requests
import json

url = "https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/trading/inquire-balance?CANO=" + CANO + "&ACNT_PRDT_CD=" + ACNT_PRDT_CD + "&AFHR_FLPR_YN=N&OFL_YN=&INQR_DVSN=01&UNPR_DVSN=01&FUND_STTL_ICLD_YN=N&FNCG_AMT_AUTO_RDPT_YN=N&PRCS_DVSN=00&CTX_AREA_FK100=&CTX_AREA_NK100="

payload = ""
headers = {
  'content-type': 'application/json',
  'authorization': 'Bearer YOUR_ACCESS_TOKEN',
  'appkey': APP_KEY,
  'appsecret': APP_SECRET,
  'tr_id': 'VTTC8434R'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

#매수가능조회 

import requests
import json

url = "https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/trading/inquire-psbl-order?CANO=" + CANO + "&ACNT_PRDT_CD=" + ACNT_PRDT_CD + "&PDNO=005930&ORD_UNPR=55000&ORD_DVSN=01&OVRS_ICLD_YN=N&CMA_EVLU_AMT_ICLD_YN=N"

payload = ""
headers = {
  'content-type': 'application/json',
  'authorization': 'Bearer YOUR_ACCESS_TOKEN'  
  'appsecret': APP_SECRET,
  'tr_id': 'VTTC8908R'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
