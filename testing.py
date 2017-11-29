import csv

file = open ("actors.csv",'rb')

data = csv.reader(file)

f = open ("actors2.csv", "wb")

lines = csv.writer(f)

for row in data:
	if row != []:
		lines.writerow (row)
f.close()