#!/usr/bin/python

import requests, os, codecs
from bs4 import BeautifulSoup

#################################
#Core spider, making progress
#################################

def trade_spider(max_pages):
	page = 1
	restaurants = []
	while page <= max_pages:
		url = "https://www.yelp.com"
		source_code = requests.get("http://www.yelp.com/search?find_desc=Restaurants&find_loc=Champaign%2C+IL&ns=1")
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "lxml")
		for link in soup.findAll('a', {'class': 'biz-name'}):
			href = url + link.get('href')
			title = link.string
			print(title)
			print(href)
			print("")
			f.write(title.encode('utf8')+"\n")
			reviews = get_single_item_data(href)
			for review in reviews:
				print(str(review))
			f.write('\n')
		page += 1


def get_single_item_data(item_url):
	reviews = []
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "lxml")
	for item in soup.findAll('p', {'itemprop': 'description'}):
		review = item.string
		reviews.append(review)
	return reviews

f = open("reviews.txt", "w")
trade_spider(1)
f.close()
