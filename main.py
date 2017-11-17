from bs4 import BeautifulSoup
import requests
import re

f = open("WATCHLIST.csv","r")
test = open("text.txt","r").read()
fw = open("trouble.txt","w")

class title():

	soup = ""
	link = ""

	def __init__(self, link):
		self.link = link

	@property
	def name(self):
		source = requests.get ( self.link ).text
		soup = BeautifulSoup ( source, 'lxml' )

		pattern = re.compile(r'<strong>([a-zA-Z\s\']+)</strong>')
		matches = pattern.findall(source)
		if matches!=[]:
			return (matches[0])
		else:
			return ("error")


def main():

	i = 0

	for link in f:
		"""
		i+=1
		source = requests.get(link[:-1]).text
		soup = BeautifulSoup(source,'lxml')
		#print (soup.prettify)
		year = soup.find_all('span', id  = 'titleYear')[0].text[1:-1]
		#print (soup.find_all('div', class_ = 'txt-block'))
		
		if year != "None":
			print (year+" ",i)
		else:
			fw.write(link[:-1] + " " + str(year) + "\n")

		try:
			print( soup.find('div', class_ = 'originalTitle').text [:-17])
		except :
			print ('bla bla')
		"""
		link = link[:-1]
		new = title(link)
		#print (actor.__dict__)
		print (new.name)

if __name__ == "__main__":
	main()






