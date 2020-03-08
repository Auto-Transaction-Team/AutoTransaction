# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#add
from django.http import HttpResponse, JsonResponse
import requests
import json

# Create your views here.

def index(request):
    coins = {'BTC': 'btc_jpy', 'ETH': 'eth_jpy', 'ETC': 'etc_jpy', 'LSK': 'lsk_jpy', 'FCT': 'fct_jpy', 'XRP': 'xrp_jpy',
             'XEM': 'xem_jpy', 'LTC': 'ltc_jpy', 'BCH': 'bch_jpy', 'MONA': 'mona_jpy', 'XLM': 'xlm_jpy'}

    URL = 'https://coincheck.com/api/rate/'

    dispList = []

    for key, item in coins.items():
        coincheck = (key,requests.get(URL+item).json())
        dispList.append(coincheck)

    return JsonResponse(dispList, safe=False)
