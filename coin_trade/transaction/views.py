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
 
    # 1分間ごとにチェックする
    time_count = 0 #時間計測(s)
    limit = 300 #動かす最大時間(s)
    difference = 0 #前のスパンからの差分
    rate_previous = 0 #前のスパンの値
    rate_now = 0 #取得した値

    # 初期値を取得
    rate_start = int(requests.get(URL+'btc_jpy').json()["rate"][:-2])
    # 通知値
    notice_rate = 0
    # 通知フラグを設定
    flg = 0 #(通知なし：0　高値通知：1 低値通知：2)
    # 通知文
    text = ''
    print(rate_start)
    while time_count < limit:
        #BTCの値を取得
        rate_now = int(requests.get(URL+'btc_jpy').json()["rate"][:-2])
        #前回との値の差分を抽出
        difference = rate_now - rate_start
        # 通知フラグを更新
        if difference > 5000:
            flg = 1
            if rate_now > notice_rate:
                notice_rate = rate_now
                print(notice_rate)
        elif difference < -5000:
            flg = 2
            if rate_now < notice_rate:
                notice_rate = rate_now
                print(notice_rate)
        #処理を一定時間停止(一定時間ごとに起動)
        time.sleep(1)
        #累計計測時間を調整
        time_count += 1
        #計測時間を超えた場合、処理中止
        if time_count > limit:
            break
    if flg == 1 and rate_start > rate_now:
        #通知文作成
        text = '開始値：' + str(rate_start) + ' 高値：' + str(notice_rate) + ' 終値：' + str(rate_now) 
    elif flg == 2 and rate_now > rate_start:
        #通知文作成
        text = '開始値：' + str(rate_start) + ' 低値：' + str(notice_rate) + ' 終値：' + str(rate_now) 
    
    if text != '':
        # Slack 通知の処理
        url = "https://slack.com/api/chat.postMessage"
        data = {
        "token": SLACK_TOKEN,
        "channel": "CV17C6MC4",
        "text": text
        }
        requests.post(url, data=data)

    # 画面表示に使う
    dispList = []
    # for key, item in coins.items():
    #     coincheck = (key,requests.get(URL+item).json())
    #     dispList.append(coincheck)

    return JsonResponse(dispList, safe=False)
