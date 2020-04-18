# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#add
from django.http import HttpResponse, JsonResponse
import requests
import json
import os
import slack
import time
import hashlib
import hmac
import datetime
import pybitflyer
from coin_trade.config import getSlackToken
from coin_trade.api import getApiKey
from coin_trade.api import getApiSecret

def index(request):

    # # 取得先のURL設定
    # base_url = 'https://api.bitflyer.jp'
    # endpoint = '/v1/board?product_code='
    # pair = 'FX_BTC_JPY'

    # # 1分間ごとにチェックする
    # time_count = 0 #時間計測(s)
    # limit = 3 #動かす最大時間(s)

    # while time_count < limit:

    #     # 値を取得
    #     data = requests.get(base_url + endpoint+pair, timeout=5).json()
    #     bids = data["bids"]
    #     asks = data["asks"]

    #      # 売り注文
    #     asks = asks[0]["price"] - 1
    #     print('売り注文：' + str(asks))

    #     # 買い注文
    #     bids = bids[0]["price"] + 1
    #     print('買い注文：' + str(bids))

    #     # 差額
    #     difference = asks - bids
    #     print('差額：' + str(difference))

    #     #処理を一定時間停止(一定時間ごとに起動)
    #     # time.sleep(0.1)
    #     #累計計測時間を調整
    #     time_count += 0.1
    #     #計測時間を超えた場合、処理中止
    #     if time_count > limit:
    #         break

    API_KEY = getApiKey()
    API_SECRET = getApiSecret()

    api = pybitflyer.API(api_key = API_KEY, api_secret = API_SECRET)

    balances = api.getbalance(product_code="BTC_JPY")
    print(balances)
    
    # buy_btc = api.sendchildorder(product_code="BTC_JPY",
    #                          child_order_type="MARKET",
    #                          side="SELL",
    #                          size=0.001,
    #                          minute_to_expire=10000,
    #                          time_in_force="GTC"
    # )

    dispList = []

    return JsonResponse(dispList, safe=False)
