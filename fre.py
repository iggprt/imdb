import re
from bs4 import BeautifulSoup
#import lxml
#import html5lib


file = open("html.txt","r")
file_the_pianist = open("html_the_pianist.txt","r")
file_res_dogs = open("html_res_dogs.txt","r")
html_res_dogs = file_res_dogs.read()
html_the_pianist = file_the_pianist.read()
html=file.read()

#html_the_pianist = html_the_pianist.replace("\n","")


test_txt = open ("test.txt","r")
string = test_txt.read()


def actor_get_name(local_html):

	""" Returns the actors's name. Needs IMDb_html. """
	
	pattern = re.compile(r'itemprop="name">[a-zA-Z\s\']+<')
	matches = pattern.findall(local_html)

	return matches[0][16:-1]

	
def actor_get_bday(local_html):

	""" Returns the actors's birthday as a dictionary. Needs IMDb_html. """
	
	pattern = re.compile(r'datetime="([\d]+)-([\d]+)-([\d]+)"')
	match = pattern.findall(local_html)
	
	result = {  'year' :	int (match[0][0]),
				'month':	int (match[0][1]),
				'day'  :	int (match[0][2])}
	
	
	return result

def actor_get_jobs(local_html):

	""" Returns the actors's jobs as a list. Needs IMDb_html. """
	
	pattern = re.compile(r'">[\n]([a-zA-Z]+)<')
	pattern2 = re.compile(r'<span class="itemprop" itemprop="jobTitle">[\n]Writer</span>')
	#pattern = re.compile(r'J')
	matches = pattern.findall(local_html)
	
	return matches
	
	
	
def title_get_name(local_html):
	#pattern = re.compile(r'class>\n([]+)\n<')
	pattern = re.compile(r'<strong>([a-zA-Z\s\']+)</strong>')
	matches = pattern.findall(local_html)
	
	return (matches[0])
	
	
def title_get_year(local_html):
	
	pattern = re.compile(r'/year/([\d]{4})/')
	matches = pattern.findall(local_html)
	
	return matches[0]
	
def title_get_rating(local_html):

	pattern = re.compile(r'Value">([\d.]+)<')
	matches = pattern.findall(local_html)
	matches[0] = matches[0].replace(".","")
	matches[0] = int(matches[0])
	
	if matches[0]<=10:
		return matches[0]
	else:
		return matches[0]/10.
	
	
def title_get_rCount(local_html):

	pattern = re.compile(r'Count">([\d,]+)<')
	matches = pattern.findall(local_html)
	matches[0] = matches[0].replace(",","")
	matches[0] = int(matches[0])
	
	return matches[0]
	
def title_get_genre(local_html):

	pattern = re.compile(r'genre">([a-zA-Z\s]+)</span')
	matches = pattern.findall(local_html)
	
	return matches
	
	
def title_get_duration(local_html):

	pattern = re.compile(r'duration" datetime="PT([\d]+)M">')
	matches = pattern.findall(local_html)
	
	return int(matches[0])
	
	
def title_get_actors(local_html):
	
	#print local_html.find("castlist")
	#print local_html.find("Storyline",local_html.find("castlist"))
	local_html = local_html[local_html.find("castlist"):local_html.find("Storyline",local_html.find("castlist"))]
	
	pattern = re.compile(r'itemprop="name">(.+)</span>')
	pattern2 = re.compile(r'name/nm')
	matches = pattern.findall(local_html)
	
	#print len(matches)
	
	return matches 


def title_get_director(local_html):

	beg = local_html.find("credit_summary_item")
	end = local_html.find("credit_summary_item", beg) +1  
	#end = local_html.find("metacriticScore",beg)
	local_html = local_html[beg:end]
	
	print beg, end
def merge_actors_list(a,b):
	pass
 
def main():
	#print (actor_get_name(html))
	#print (actor_get_bday(html))
	#print (actor_get_jobs(html))
	#print title_get_name(html_the_pianist)
	#print title_get_year(html_the_pianist)
	#print title_get_rating(html_the_pianist)
	#print title_get_rCount(html_the_pianist)
	#print title_get_genre(html_the_pianist)
	#print title_get_duration(html_the_pianist)
	#title_get_actors(html_the_pianist)
	#print title_get_actors(html_res_dogs)
	#title_get_director(html_res_dogs)
	
	
	soup = BeautifulSoup(html_res_dogs,"html.parser")
	
	containers = soup.find_all('tr', class_='odd')
	containers2 = soup.find_all('tr', class_='even')
	
	for i in range(len(containers)):
		containers[i] = containers[i].find('span').text
		
	#print containers[1]
	for i in range(len(containers2)):
		containers2[i] = containers2[i].find('span').text
		
		
	#print containers
	#print containers2
	j = 0
	
	for j in range( len(containers2) ):
		containers.insert(j*2,containers2[j])
		print j,containers[j]
	k=0	
	for name in containers:
		print k , name 
		k+=1
	#print containers[0]
	#print len(containers2)
	#name =  containers[2].find('span').text
	#print name
	#merge_actors_list(containers, containers2)
	
	
if __name__=="__main__":
	main() 
	
	
#print("__done__") 	

file.close()

