
"""Library containing the two classes"""



from bs4 import BeautifulSoup
import requests
import re
import time


class Title():

	def __init__(self, link):

		self.link = link
		self.source = requests.get ( link ).text
		self.soup = BeautifulSoup ( self.source,"lxml" )

	@property
	def title(self):
		
		matches = self.soup.find_all('meta', property='og:title')
		if matches != []:
			return matches[0].get('content')[:-7]
		else:
			return "__NameError__"

	@property
	def movieID(self):
		pass

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
		""" There is a problem with that. It doesn't work for Scarface and some other movies"""


		matches = self.soup.find_all('meta', itemprop='contentRating')
		#matches = self.soup.find_all('span', itemprop='contentRating')

		if matches != []:
			return matches[0].get('content')
		else:
			#pattern = re.compile(r'contentRating">(.+)<')
			#pattern = re.compile(r'g">(.+)</span')
			#pattern = re.compile(r'content="(.+)">')
			#matches = pattern.findall(self.source)
			return "__RatedError__" + self.title# + str(matches) + str(len(matches))


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
			return matches[0].text.strip()
		else:
			return "__StoryLineError__"



	@property
	def originalTitle(self):

		matches = self.soup.find_all('div', class_ = 'originalTitle')

		if matches != []:
			if matches[0].text[:-17] != self.title:
				return matches[0].text[:-17]
			return None
		else:
			return None


	@property
	def budget(self):

		pattern = re.compile(r'Budget:</h4>((.|\n)+)<span\sclass="attribute"')

		matches = pattern.findall(self.source)

		



		print (matches)
		print ("\n")
		#return matches 


	@property
	def directors(self):
		pass

	@property
	def writers(self):
		pass

	@property
	def actors(self):
		pass

	@property
	def oscars(self):
		pass

	@property
	def metascore(self):
		pass

	@property
	def productionCo(self):
		pass






class Actor():
	"""docstring for ClassName"""

	def __init__(self, link):

		self.link = link
		self.source = requests.get ( link ).text
		self.soup = BeautifulSoup ( self.source,"lxml" )

		self.biosource = requesets.get(link+'bio/')
		self.biosoup = BeautifulSoup (self.biosource, 'lxml')

	@property
	def name(self):
		pass

	@property
	def birthDate(self):
		pass

	@property
	def birthPlace(self):
		pass

	@property
	def jobs(self):
		pass

	@property
	def hight(sefl):
		pass

	@property
	def death(self):
		pass

	@property
	def oscars(self):
		pass





































