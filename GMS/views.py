from django.shortcuts import render
import requests
from json import dumps

def index(request):
	data = requests.get("https://api.thingspeak.com/channels/1699059/feeds.json?api_key=8J0UBF269PG0OSKH&results=4")
	data = data.json()

	hue = []
	moist = []
	tmp = []
	x = []
	count = 0

	for i in data['feeds']:
		x.append(str(count))
		hue.append(int(i['field1']))
		moist.append(int(i['field2']))
		tmp.append(int(i['field3']))
		count+=1

	data = {
		'hue' : hue,
		'moist' : moist,
		"tmp" : tmp,
		'x' : x
	}

	print(data)

	data = dumps(data)

	return render(request,'index.html',{'data':data})