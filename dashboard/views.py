import json

from django.http import Http404, HttpResponse
from django.shortcuts import render
import requests


def index(request):
    context = {}

    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiIxMDIiLCJjbGllbnRJZCI6ImhhY2thdGhvbiIsImlhdCI6MTUzOTA3MTMwMCwiZXhwIjoxNTQwMzY3MzAwfQ.HsTV7fIKNFMCh_xjoQvH4jch6pTwgsjOsnFp4VWCq_I'  # insert your bearer token
    }
    gateway_id = '015fad1422b700000000000100100219'  # insert your gateway_id
    sensor_id = 'number-015fad1422b700000000000100100219-0'  # insert your sensor_id
    url = 'https://api.sandbox.thingplus.net/v2/gateways/{gateway_id}/sensors/{sensor_id}/series'.format(
        gateway_id=gateway_id, 
        sensor_id=sensor_id
        )

    # query string option
    # params = {
    #     'interval': '5m',
    #     'dataStart': '2018-10-11T03:00:00.000Z',
    #     'dataEnd': '2018-10-11T03:00:00.000Z',
    # }
    params = {}
    
    response = requests.get(url, headers=headers, params=params)  # request sensor series data -  GET method
    
    print(response.json())  # for debug
    ### print sample
    #     {'data': {'_meta': {'count': 1},
    #           'data': ['26.10', 1513226803332],
    #           'latest': {'ctime': '1510455034158',
    #                      'mtime': '1513226832468',
    #                      'time': '1513226803332',
    #                      'type': 'series',
    #                      'value': '26.10'}},
    #      'message': 'OK',
    #      'statusCode': 200}
    ###

    context = {
        'lastest': response.json()['data']['latest'],
        'data': response.json()['data']['data'],
    }

    return render(request, 'dashboard/index.html', context)
