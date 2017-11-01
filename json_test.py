# -*- coding: utf-8 -*-
import urllib
import requests
import json
import sys

def dataGet():
	url = 'http://www.land.mlit.go.jp/webland/api/TradeListSearch?from=20101&to=20134&station=02590'
	r = requests.get(url)
	response = r.json()
	data_values = response['data']

#datas = []
	for i in data_values:
		for j in i.values():
			print(j)
			return j



#dictTest = {'threeKey': 3, 'twoKey': 2, 'oneKey': 1}
#a = []
#for i in dictTest.values():
#	data = []
#	data.append(i)
#	a.append(data)