#현재가 조회 

from dotenv import load_dotenv
import os
import requests

load_dotenv()

APP_KEY = os.getenv("VTS_APPKEY")
APP_SECRET = os.getenv("VTS_APPSECRET")

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"


def get_price(code="005930"):
    url = "https://openapivts.koreainvestment.com:29443/uapi/domestic-stock/v1/quotations/inquire-price"

    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET,
        "tr_id": "FHKST01010100"
    }

    params = {
        "fid_cond_mrkt_div_code": "J",
        "fid_input_iscd": code
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    price = int(data["output"]["stck_prpr"])
    return price


if __name__ == "__main__":
    print(get_price("005930"))
