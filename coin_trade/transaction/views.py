# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#add
from django.http import HttpResponse, JsonResponse
import requests
import json
import sys
sys.path.append('../')
# from coin_trade.api import *

# Create your views here.

def index(request):

    base_url = 'https://api.bitflyer.jp'
    endpoint = '/v1/board?product_code='
    pair = 'FX_BTC_JPY'

    result = requests.get(base_url + endpoint+pair, timeout=5).text

    print(result)

    # path_balance = '/api/accounts/balance'
    # result = coincheck.get(path_balance)
    # print(result)

    # path_orders_transactions = '/api/exchange/orders/transactions'
    # result = coincheck.get(path_orders_transactions)
    # print(result)

    # path_orders_transactions_pagination = '/api/exchange/orders/transactions_pagination'
    # result = coincheck.get(path_orders_transactions_pagination)
    # print(result)

    return JsonResponse(result, safe=False)
