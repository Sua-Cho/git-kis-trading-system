from dotenv import load_dotenv
import os
import requests

load_dotenv()

APP_KEY = os.getenv("VTS_APPKEY")
APP_SECRET = os.getenv("VTS_APPSECRET")


def get_access_token():
    url = "https://openapivts.koreainvestment.com:29443/oauth2/tokenP"

    body = {
        "grant_type": "client_credentials",
        "appkey": APP_KEY,
        "appsecret": APP_SECRET
    }

    headers = {
        "content-type": "application/json"
    }

    response = requests.post(url, headers=headers, json=body)
    data = response.json()

    print(data)

    if "access_token" not in data:
        raise Exception(f"토큰 발급 실패: {data}")

    return data["access_token"]


if __name__ == "__main__":
    print(get_access_token())
