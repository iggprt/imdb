from bs4 import BeautifulSoup
import re




class title():

	soup = ""
	link = ""

	def __init__(self, file):
		file = open(file, "r").read()
		self.html = file
		
	@property
	def name(self):
	
		soup = BeautifulSoup ( self.html,'html.parser' )

		pattern = re.compile(r'<strong>([a-zA-Z:\d\s\']+)</strong>')
		matches = pattern.findall(self.html)
		
		if matches!=[]:
			return (matches[0])
		else:
			return ("__error__")
			
	@property
	def name2 (self):
	
		soup = BeautifulSoup ( self.html, 'html.parser' )
		matches = soup.find_all('h1', itemprop = 'name')
		
		return (matches[0].text)[:-8]
		
	@property
	def year(self):
	
		soup = BeautifulSoup ( self.html, 'html.parser' )
		matches = soup.find_all('span', id = 'titleYear')
		
		return int((matches[0].text)[1:-1])
		
	@property
	def rating(self):
		
		soup = BeautifulSoup ( self.html, 'html.parser' )
		matches = soup.find_all('span', itemprop="ratingValue")
		
		
		if matches!=[]:
			matches[0] = matches[0].text.replace(".","")
			matches[0] = float(matches[0])/10
			return (matches[0])
		else:
			return ("__error__")
			
			
flist = ["./htmls/html_310_to_Yuma.txt",
		"./htmls/html_lives_of_others.txt",
		"./htmls/html_poz_cop.txt",
		"./htmls/html_res_dogs.txt",
		"./htmls/html_the_pianist.txt"]

for file in flist:
	movie = title(file)
	print movie.name
	#print movie.name2
	#print movie.year
	#print type(movie.year)
	print movie.rating 
