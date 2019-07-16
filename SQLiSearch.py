#!/usr/bin/python
# -*- coding: utf-8 -*

from googlesearch import search
import requests
import optparse

def searchSQLi(query, number, pause):
	f = open("sqlPages.txt", 'w+')
	logs = open("logs.txt", 'a+')
	n = 0
	for i in search(query, stop=number, pause=pause):
		try:
			#Get the response for the url
			r1 = requests.get(str(i))
			r2 = requests.get(str(i) + "'")
			#Compare the urls
			if(r1.status_code == r2.status_code):
				if(str(r1.text) != str(r2.text)):
					n += 1
					print("Possible SQLi on: " + str(i))
					f.write(i)
		except e:
			logs.write(e)
			continue
	f.close()
	print("There are " + str(n) + " possible SQLi")

def main():
	parser = optparse.OptionParser("%prog -q query [-n number -p pause -t tld -l lang] ")
	parser.add_option("-q", dest='query', type='string',\
			help='specify the query to search sqli')
	parser.add_option("-n", dest='number', type='int',\
			help='specify the maximun number of pages to search')
	parser.add_option("-p", dest='pause', type='float',\
			help='specify the seconds between query google, too low maybe result on get block by google')

	(options, args) = parser.parse_args()
	if(options.query == None):
		print(parser.print_help())
		exit(0)
	else:
		query = options.query
	if(options.number == None):
		number = 10
	else:
		number = options.number
	if(options.pause == None):
		pause = 2.0
	else:
		pause = options.pause

	print("Searching your sqli, be patient...")
	searchSQLi(str(query), number, pause)
	print("Search done, check the results in sqlPages.txt")

if __name__ == '__main__':
	main()
