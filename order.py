from dotenv import load_dotenv
import os
import requests

load_dotenv()

APP_KEY = os.getenv("VTS_APPKEY")
APP_SECRET = os.getenv("VTS_APPSECRET")
CANO = os.getenv("VTS_CANO")
ACNT_PRDT_CD = os.getenv("VTS_ACNT_PRDT_CD")

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  


def buy_stock(code="005930", qty=1):
    url = "https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/trading/order-cash"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "VTTC0802U"
    }

    body = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": code,
        "ORD_DVSN": "01",
        "ORD_QTY": str(qty),
        "ORD_UNPR": "0"
    }

    response = requests.post(url, headers=headers, json=body)
    return response.json()


if __name__ == "__main__":
    print(buy_stock("005930", 1))