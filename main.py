from datetime import datetime
import csv
import os
import time

from get_token import get_access_token
from price import get_price
from order import buy_stock
from account import get_balance, get_buyable_cash

CODE = "005930"
TARGET_BUY_PRICE = 300000
QTY = 1
LOG_FILE = "trade_log.csv"
INTERVAL = 30
MAX_BUY_COUNT = 1

ACCESS_TOKEN = get_access_token()


def save_log(code, price, target_price, signal, result):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "time", "code", "current_price",
                "target_buy_price", "signal", "result"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            code, price, target_price, signal, result
        ])


def run_strategy():
    buy_count = 0

    print("자동매매 시작")

    while True:
        current_price = get_price(CODE, ACCESS_TOKEN)

        print("현재가:", current_price)
        print("목표 매수가:", TARGET_BUY_PRICE)

        balance = get_balance(ACCESS_TOKEN)
        buyable = get_buyable_cash(ACCESS_TOKEN, CODE)

        if current_price <= TARGET_BUY_PRICE and buy_count < MAX_BUY_COUNT:
            print("매수 조건 충족")
            order_result = buy_stock(CODE, QTY, ACCESS_TOKEN)
            result_msg = order_result.get("msg1", str(order_result))
            save_log(CODE, current_price, TARGET_BUY_PRICE, "BUY", result_msg)
            buy_count += 1
            print(order_result)
        else:
            print("매수 조건 미충족 또는 중복매수 방지")
            save_log(CODE, current_price, TARGET_BUY_PRICE, "HOLD", "조건 미충족 또는 중복매수 방지")

        print(f"{INTERVAL}초 후 다시 실행")
        time.sleep(INTERVAL)


if __name__ == "__main__":
    run_strategy()