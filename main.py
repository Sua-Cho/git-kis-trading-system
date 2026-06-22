from datetime import datetime
import csv
import os 

from price import get_price
from order import buy_stock

CODE = "005930"


TARGET_BUY_PRICE = 300000

QTY = 1
LOG_FILE = "trade_log.csv"


def save_log(code, price, target_price, signal, result):
    file_exists = os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "time",
                "code",
                "current_price",
                "target_buy_price",
                "signal",
                "result"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            code,
            price,
            target_price,
            signal,
            result
        ])

def run_strategy():
    current_price = get_price(CODE)

    print("현재가:", current_price)
    print("목표 매수가:", TARGET_BUY_PRICE)

    if current_price <= TARGET_BUY_PRICE:
        print("매수 조건 충족")
        order_result = buy_stock(CODE, QTY)
        result_msg = order_result.get("msg1", str(order_result))
        save_log(CODE, current_price, TARGET_BUY_PRICE, "BUY", result_msg)
        print(order_result)

    else:
        print("매수 조건 미충족")
        save_log(
            CODE,
            current_price,
            TARGET_BUY_PRICE,
            "HOLD",
            "조건 미충족"
        )


if __name__ == "__main__":
    run_strategy()