# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#add
from django.http import HttpResponse, JsonResponse
import requests
import json

# Create your views here.

def index(request):
    URL = 'https://coincheck.com/api/ticker/'
    coincheck = requests.get(URL).json() 
    for key, item in coincheck.items():
        print("%-9s : %-10.9s " % (key, item))

    return JsonResponse(coincheck, safe=False)
