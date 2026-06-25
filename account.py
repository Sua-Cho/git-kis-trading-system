from dotenv import load_dotenv
import os
import requests

load_dotenv()

APP_KEY = os.getenv("VTS_APPKEY")
APP_SECRET = os.getenv("VTS_APPSECRET")
CANO = os.getenv("VTS_CANO")
ACNT_PRDT_CD = os.getenv("VTS_ACNT_PRDT_CD")

#주식 잔고 조회 
def get_balance(token):
    url = "https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/trading/inquire-balance"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "VTTC8434R"
    }

    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "AFHR_FLPR_YN": "N",
        "OFL_YN": "",
        "INQR_DVSN": "01",
        "UNPR_DVSN": "01",
        "FUND_STTL_ICLD_YN": "N",
        "FNCG_AMT_AUTO_RDPT_YN": "N",
        "PRCS_DVSN": "00",
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": ""
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()

# 매수 가능 조회 
def get_buyable_cash(token, code="005930", price="0"):
    url = "https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/trading/inquire-psbl-order"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "VTTC8908R"
    }

    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": code,
        "ORD_UNPR": price,
        "ORD_DVSN": "01",
        "OVRS_ICLD_YN": "N",
        "CMA_EVLU_AMT_ICLD_YN": "N"
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()
