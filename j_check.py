#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import pprint
import json
import sys


def Dataget():
	url = 'http://www.land.mlit.go.jp/webland/api/TradeListSearch?from=20101&to=20134&station=02590'
	r = requests.get(url)
	response = r.json()
	print(type(response))
	data_values = response['data']
	#print(type(data_values))

	key_list = []
	datas = []
	h = len(data_values)
	j = 0

	
	for s in data_values[1].keys():
		key_list.append(s)
	datas.append(key_list)

	while h>=j:
		data = []
		if h <= j:
			break
		else:
			for i in data_values[j].values():
				data.append(i)
			datas.append(data)
			j += 1

	#pprint.pprint(datas)
	#print(type(datas))
	return datas