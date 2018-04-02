# from sklearn import datasets
from sklearn import svm
import csv

sv = svm.SVC(kernel = 'linear')
# sv = svm.LinearSVC();


picSize  = 28
zipLever = 1
newSize  = int( picSize / zipLever )
jumpLeng = picSize*zipLever
def zipPicture( list ):
	if zipLever <= 1:
		return list

	a= []
	i2= 0
	for i in range( newSize ):				# column index
		j2= i2
		for j in range( newSize ):			# row index
			s= 0
			k2= j2
			for k in range( newSize ):
				s+= sum( list[ (k2) : (k2+zipLever) ])
				k2+= picSize
			j2+= zipLever
			a.append( s )
		i2+= jumpLeng
	# print( a )
	return a


#	I have 2 type of zip:
#	1: I add in Horizontal and Vertical to zip a 28x28 => 2x28	( max point: 61% )
#	2: I zip the picture 4 time, 28x28 => 7x7					( max point: 81% )


def ZipData(data):
	result= []
	d= 0
	ld= len(data)
	l= int( ld/10 )
	# 1
	"""
	for i in b:
		d+= 1
		if d % 10000 == 0:
			print(".")
		# if d > 5:
		# 	break
		if d % 10000 == 0:
			print(".")
		ii= [int(j) for j in i if int(j) > 0]
		ii= sum(ii)/len(ii)
		i = [ 1 if int(j) > ii else 0 for j in i ]
		# print(i)

		b2= []
		b3= []
		for j in range(28):
			b2.append( i[28*j:28*(j+1)] )
			# print(e)
			b3.append( sum(b2[-1]) )
		summ= 0
		for j in range(28):
			for k in b2:
				# print( len(k) )
				summ+= k[j]
			b3.append( summ )
		# print(b3)
		result.append( b3)
	"""

	#2
	for i in data:
		d+= 1
		# if d > 50:
		# 	break
		if d % l == 0: print(str(10*d/l)+"%")

		i= [int(j) for j in i]

		ii= [ j for j in i if j > 0]
		ii= sum(ii)/len(ii)
		i = [ 1 if j > ii else 0 for j in i ]
		# print(i)

		b3= zipPicture(i)
		# print(b3)
		result.append( b3)

	return result






# /////////////////////////////////////////////////////////////////////////
print("Bat dau doc file train")

a= []
b= []
with open('train.csv', newline = '') as csvfile:
	spamreader = csv.reader( csvfile, delimiter = ' ', quotechar = '|')
	d= 0
	for row in spamreader:
		d+= 1
		if d < 2:
			continue
		row= row[0].split(',')
		a.append( row[0]  )
		b.append( row[1:] )
		# print( b[-1] )
		# print( row )
		# print( len( row ) )

print("Doc xong")
# /////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////
print("Bat dau xu li du lieu : ")

c= ZipData(b)
# print(c)

print("Xu li xong")
# /////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////
print("Bat dau hoc")
# p = Process( target=sv.fit, args=(c,a,) )
sv.fit( c, a)
# p.start()
# p.join()
print("Hoc xong")
# /////////////////////////////////////////////////////////////////////////











# /////////////////////////////////////////////////////////////////////////
print("Bat dau doc file test")

b= []
with open('test.csv', newline = '') as csvfile:
	spamreader = csv.reader( csvfile, delimiter = ' ', quotechar = '|')
	d= 0
	for row in spamreader:
		d+= 1
		if d < 2:
			continue
		# if d > 5:
		# 	break
		b.append( row[0].split(',') )

print("Doc xong")
# /////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////
print("Bat dau xu li du lieu : ")

c= ZipData(b)
# print(c)

print("Xu li xong")
# /////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////
print("Bat dau so ket qua")
a = sv.predict( c )
print("So ket qua xong")
# //////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////
filename= "answer3.csv"
print("Bat dau ghi ra file "+ filename)

file = open(filename,"w") 
# a= [1,2,3,4,5]
file.write("ImageId,Label\n")
for i in range( len(a) ):
	file.writelines(str(i+1)+","+str( a[i] )+"\n" )
file.close() 

print("Ghi ra file xong")
# /////////////////////////////////////////////////////////////////////////


print("All done!")