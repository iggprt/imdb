import sqlite3
import random

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS actors (actor_id integer primary key autoincrement,name text, age integer)")
	c.execute("CREATE TABLE IF NOT EXISTS films (film_id integer primary key autoincrement,name text, year integer)")
	c.execute("CREATE TABLE IF NOT EXISTS bind (character_id integer primary key autoincrement, actor_id integer, film_id integer, character text)")
	c.execute("CREATE TABLE IF NOT EXISTS genre (genre_id integer primary key autoincrement,name text)")
	c.execute("CREATE TABLE IF NOT EXISTS genre_bind (genre_bind_id integer primary key autoincrement, genre_id, film_id)")
	
def actor_entry(act):
	c.execute("INSERT INTO actors(name,age) VALUES(:name, :age)", {
	'name': act+str(random.randint(1,10)), 
	'age': random.randint(1,100)})
	conn.commit()

def film_entry(act):
	c.execute("INSERT INTO films(name,year) VALUES(:name, :year)", {
	'name': act+str(random.randint(1,10)), 
	'year': random.randint(1970,2018)})
	conn.commit()
	
def character_entry(film_id, actor_id):
	c.execute("INSERT INTO bind(actor_id,film_id,character) VALUES(:actor, :film, :character)", {
	'actor': actor_id, 
	'film': film_id,
	'character': "character " + str(random.randint(1,100))})
	conn.commit()
def genre_entry(name):
	c.execute("INSERT INTO genre(name) VALUES(:name)", {
	'name': name})
	conn.commit()
	
def genre_bind_entry(genre_id, film_id):
	c.execute("INSERT INTO genre_bind(genre_id, film_id) VALUES(:genre, :film)", {
	'genre':  genre_id,
	'film': film_id})
	conn.commit()


create_table()	
#c.execute("select * from actors")


c.execute("select actor_id, name from actors")
actors = c.fetchall()

c.execute ("select name, film_id from films")
films = c.fetchall()
for item in actors: 
	print item
	
print "\n"
for film in films:
	print film[0]
	act = raw_input("genres: ")
	act = act.split(" ")
	act = map(int,act)
	for num in act:
		genre_bind_entry( num, film[1] )
		
conn.close()

