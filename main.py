
""" Main module """



from bs4 import BeautifulSoup
import requests
import re
import imdblib
import time
file = open("WATCHLIST.csv","r")



def main():

	i = 0
	for link in file:
		
		i = i + 1
		link = link[:-1]
		movie = imdblib.Title(link)

		str_ = str(movie.title)+ ' ' + str(movie.titleYear) + str(movie.__repr__) + str(
			type(movie.titleYear))
		#str_ = str(movie.name)
		#print (str (i) + '. ' +  str_ + ' ' +str(round(i/1625, 3))+ '%')

		#print (movie.genre, end = " ")
		#print (movie.name, end = " ")
		#print (str(movie.originalTitle)+"       " + movie.budget + movie.title + "<stuff = 'type'sd>")
		print (str(movie.budget) + movie.title)
		#print (movie.contentRating)

def test():

	x = [1,3,5,7,9]
	y = [2,4,6,8,10]


	list = []
	k = 0
	for i,j in zip(x,y):
		list.append(i)
		list.append(j)
	print (list)


def test2():
	movie = imdblib.Title("http://www.imdb.com/title/tt0086250/")
	print (movie.contentRating)

if __name__ == "__main__":
	main()
	#test()
	#test2()