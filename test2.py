# from sklearn import datasets
from sklearn import svm
import csv
from multiprocessing import Process

sv = svm.SVC(kernel = 'poly')

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
print("Bat dau xu li du lieu : ", end="")

# # print(a[0:5])
# # d= 0
# # for row in b:
# 	# if d > 5:
# 	# 	break
# 	# d+= 1
# 	# row= row[0].split(',')
# 	# a.insert( len(a),row[0] )
# 	# row= row[1:]
# 	# print( row )


c= []
# print( len(b) )
d= 0
for i in b:
	d+= 1
	# if d > 5:
	# 	break
	# print(d)
	# print(a[d])
	if d % 1000 == 0:
		print(".", end="")
	b2= []
	b3= []
	for j in range(28):
		e= i[28*j:28*(j+1)]
		b2.append( [int(k) for k in e] )
		# print(e)
		b3.append( sum(b2[-1]) )
	summ= 0
	for j in range(28):
		for k in b2:
			# print( len(k) )
			summ+= k[j]
		b3.append( summ )
	c.append( b3)
	# print(b3)

print()
print("Xu li xong")
# /////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////
print("Bat dau hoc")
p = Process( target=sv.fit, args=(c,a,) )
# sv.fit( c, a)
p.start()
p.join()
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
print("Bat dau xu li du lieu : ", end="")

c= []
a= []
d= 0
for i in b:
	d+= 1
	if d % 1000 == 0:
		print(".", end="")
	# if d > 5:
	# 	break
	b2= []
	b3= []
	for j in range(28):
		e= i[28*j:28*(j+1)]
		b2.append( [int(k) for k in e] )
		# print(e)
		b3.append( sum(b2[-1]) )
	summ= 0
	for j in range(28):
		for k in b2:
			# print( len(k) )
			summ+= k[j]
		b3.append( summ )
	# print(b3)
	c.append( b3)

# print(c)
print()
print("Xu li xong")
# /////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////////////////
print("Bat dau so ket qua")
a = sv.predict( c )
print("So ket qua xong")
# //////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////
print("Bat dau ghi ra file")

file = open("answer.csv","w") 
# a= [1,2,3,4,5]
file.write("ImageId,Label\n")
for i in range( len(a) ):
	file.writelines(str(i+1)+","+str( a[i] )+"\n" )
file.close() 

print("Ghi ra file xong")
# /////////////////////////////////////////////////////////////////////////


print("All done!")