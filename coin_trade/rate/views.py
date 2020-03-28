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
from coin_trade.config import getSlackToken

def index(request):
    coins = {'BTC': 'btc_jpy', 'ETH': 'eth_jpy', 'ETC': 'etc_jpy', 'LSK': 'lsk_jpy', 'FCT': 'fct_jpy', 'XRP': 'xrp_jpy',
             'XEM': 'xem_jpy', 'LTC': 'ltc_jpy', 'BCH': 'bch_jpy', 'MONA': 'mona_jpy', 'XLM': 'xlm_jpy'}

    URL = 'https://coincheck.com/api/rate/'

    # Slackのトークン取得
    SLACK_TOKEN = getSlackToken()

    # Slack 通知の処理
    url = "https://slack.com/api/chat.postMessage"
    data = {
    "token": SLACK_TOKEN,
    "channel": "CV17C6MC4",
    "text": '計測開始'
    }
    requests.post(url, data=data)
 
    # 1分間ごとにチェックする
    time_count = 0 #時間計測(s)
    limit = 180 #動かす最大時間(s)
    difference = 0 #前のスパンからの差分
    rate_previous = 0 #前のスパンの値
    rate_now = 0 #取得した値

    while time_count < limit:
        #BTCの値を取得
        rate_now = int(requests.get(URL+'btc_jpy').json()["rate"][:-2])
        #前回との値の差分を抽出
        if rate_previous != 0: 
            difference = rate_now - rate_previous
        #通知文作成
        text = 'BTC：' + str(rate_now) + ' ' + '前スパンより' + str(difference) 
        # Slack 通知の処理
        url = "https://slack.com/api/chat.postMessage"
        data = {
        "token": SLACK_TOKEN,
        "channel": "CV17C6MC4",
        "text": text
        }
        requests.post(url, data=data)
        #取得した値を保存
        rate_previous = rate_now
        #処理を一定時間停止(一定時間ごとに起動)
        time.sleep(20)
        #累計計測時間を調整
        time_count += 20
        #計測時間を超えた場合、処理中止
        if time_count > limit:
            break
    
    # Slack 通知の処理
    url = "https://slack.com/api/chat.postMessage"
    data = {
    "token": SLACK_TOKEN,
    "channel": "CV17C6MC4",
    "text": '計測終了'
    }
    requests.post(url, data=data)

    # 画面表示に使う
    dispList = []
    # for key, item in coins.items():
    #     coincheck = (key,requests.get(URL+item).json())
    #     dispList.append(coincheck)

    return JsonResponse(dispList, safe=False)
