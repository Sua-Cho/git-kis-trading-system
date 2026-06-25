


# Git-KIS-trading system 
한국투자증권 API를 활용하여 구축한 자동매매 시스템입니다. 

## Project Structure 
```text
.
├── main.py                    # 자동매매 실행
│   ├── get_approval_key.py    # Approval Key 발급
│   ├── get_token.py           # Access Token 발급
│   ├── price.py               # 현재가 조회
│   ├── account.py             # 잔고 조회 및 매수 가능 금액 조회
│   └── order.py               # 모의투자 주문
├── .gitignore
└── README.md

```

## Summary 

``` text
한국투자증권 API에서 발급받은 App Key, App Secret을 활용하여 Approval Key와 Access Token을 발급받은 후, 
API에 접속하여 현재가를 조회하고, 각 개인이 확보하고 있는 잔고와 매수 가능한 주식 수를 확인한 뒤, 
사용자가 설정한 타겟 가격보다 시장가가 낮을 경우 자동으로 매매할 수 있도록 구축하였습니다.

거래 결과는 자동으로 trade_log에 csv 형태로 저장되며,
거래가 성사될 경우는 "매수 조건 충족", 거래가 성사되지 않았을 경우는 "HOLD, 매수 조건 미충족"이라고 저장됩니다. 
```



