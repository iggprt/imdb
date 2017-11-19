
"""Library containing the two classes"""



from bs4 import BeautifulSoup
import requests
import re
import time


class Title():

	def __init__(self, link):

		self.link = link
		self.source = requests.get ( link ).text
		self.soup = BeautifulSoup ( self.source, 'lxml' )
		#time.sleep(1)

	@property
	def title(self):
		
		matches = self.soup.find_all('meta', property='og:title')
		if matches != []:
			return matches[0].get('content')[:-7]
		else:
			return "__NameError__"


	@property
	def titleYear(self):

		matches = self.soup.find_all('span', id='titleYear')

		if matches != []:
			return int(matches[0].text[1:-1])
		else:
			return "__YearError__"


	@property
	def genre(self):

		matches = self.soup.find_all('span', itemprop='genre')

		if matches != []:
			for i in range(len(matches)):
				matches[i] = matches[i].text
			return matches
		else:
			return "__GenreError__"

	@property
	def contentRating(self):

		matches = self.soup.find_all('meta', itemprop='contentRating')
		#matches = self.soup.find_all('span', itemprop='contentRating')

		if matches != []:
			return matches[0].get('content')
		else:
			return "__RatedError__" + self.name


	@property
	def ratingValue(self):

		matches = self.soup.find_all('span', itemprop='ratingValue')
		match = float(matches[0].text.replace(".",""))/10

		if matches != []:
			return match
		else:
			return "__ratingValueError__ "+self.name

	@property
	def ratingCount(self):

		matches = self.soup.find_all('span', itemprop='ratingCount')
		match = int(matches[0].text.replace(",",""))

		if matches != []:
			return match
		else:
			return "__ReviewsError__ "+self.name


	@property
	def runtime(self):

		matches = self.soup.find_all('time', itemprop='duration')
		match = int(matches[0].get('datetime')[2:-1])

		if matches != []:
			return match
		else:
			return "__runtimeError__ "+self.name


	@property
	def storyline(self):

		matches = self.soup.find_all('div', itemprop='description')

		if matches != []:
			return matches[0].text
		else:
			return "__YearError__"