
""" Main module """



from bs4 import BeautifulSoup
import requests
import re
import imdblib

file = open("WATCHLIST.csv","r")



def main():

	i = 0
	for link in file:
		
		i = i + 1
		link = link[:-1]
		movie = imdblib.Title(link)

		#str_ = str(movie.name)+ ' ' + str(movie.year) + str(movie.__repr__) + str(type(movie.year))
		#str_ = str(movie.name)
		#print (str (i) + '. ' +  str_ + ' ' +str(round(i/1625, 3))+ '%')

		#print (movie.genre, end = " ")
		#print (movie.name, end = " ")
		print (str(movie.storyline.strip()) + movie.title )


if __name__ == "__main__":
	main()