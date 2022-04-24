import requests

data = requests.get("https://api.thingspeak.com/channels/1699059/feeds.json?api_key=8J0UBF269PG0OSKH&results=4")
data = data.json()

hue = []
moist = []
tmp = []
x = []
count = 1

for i in data['feeds']:
	x.append(count)
	hue.append(int(i['field1']))
	moist.append(int(i['field2']))
	tmp.append(int(i['field3']))

print(hue)
print(moist)
print(tmp)

# print(data)