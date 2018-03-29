import csv

with open('answer.csv', newline = '') as csvfile:
	spamreader = csv.reader( csvfile, delimiter = ' ', quotechar = '|')
	file = open("answer2.csv","w")
	d= 0
	for row in spamreader:
		d+= 1
		if( d > 5 ):
			break
		if d < 2:
			file.writelines(row[0]+"\n")
		else:
			row= row[0].split(',')
			print(row, end= "")
			file.writelines(str(int(row[0])+1)+","+row[1]+"\n")
		# print( row )
	file.close()