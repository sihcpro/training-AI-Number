import csv
from PIL import Image
import numpy as np
import cv2 
import time
import math

maxleng		= 20
imgWidth 	= 28
imgHeight	= 28

a= []
b= []
out= []

def readFileTrain():
	print("Reading file")
	with open('train.csv', newline = '') as csvfile:
		spamreader = csv.reader( csvfile, delimiter = ' ', quotechar = '|')
		d= 0
		for row in spamreader:
			d+= 1
			if d < 2:
				continue
			if d > maxleng+1:
				break
			row= row[0].split(',')
			a.append( row[0]  )
			b.append( row[1:] )
	print("Read file done")


new_img = Image.new("P", (imgWidth, imgHeight))
def makeImage(l):
	new_img.putdata(l)
	return new_img

countImgs= 0
def saveImage(img):
	img.save('Image out/out'+str(countImgs)+'0.tif')

def saveImageAfterEdit(img):
	img.save('Image out/out'+str(countImgs)+'1.tif')

affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR
def deskew(img):
	m = cv2.moments( img )
	# if abs(m['mu02']) < 1e-2:
	# 	return img.copy()
	skew = m['mu11']/m['mu02']
	skew = 0.75

	# for i in m:
	# 	print(i+" = "+str(m[i]))
	# print( skew )

	M = np.float32([[1, skew, -0.5*imgHeight*skew], [0, 1, 0]])
	img = cv2.warpAffine(img,M,(imgWidth, imgHeight),flags=affine_flags)
	makeImage( img.tolist() ).show()
	return img


# ///////////////////////////////////////////////////////////////////////

def distanceTwoPoint(x, y):
	xx= x[0]-y[0]
	yy= x[1]-y[1]
	return math.sqrt( xx*xx+yy*yy )

def check(img):
	d1= distanceTwoPoint( img[0], img[1])
	d2= distanceTwoPoint( img[1], img[2])
	if d1 < d2:
		out.append( img )
		out.append( ["----------------------"] )
		return img
	else:
		out.append( img )
		omg= np.concatenate( ( [img[-1]], img[:3] ), axis=0)
		out.append( omg )
		out.append( ["----------------------"] )
		return omg














readFileTrain()
# dst = Mat::zeros( imgHeight, imgWidth, CV_8UC3);
# vis = np.zeros(( imgHeight, imgWidth), np.float32)
# vi2 = cv2.CreateMat( imgHeight, imgWidth, cv2.CV_32FC3)

for i in range(maxleng):
	j = list(map(int, b[i]))
	img = makeImage(j)
	countImgs+= 1

	img2 = np.array( img ).copy()
	img2 = cv2.resize( img2, None, fx=7, fy= 7)

	# cv2.namedWindow('Window')
	# cv2.imshow("Before", img2)
	# time.sleep(0.25)



	# kernel = np.ones((5,5),np.uint8)
	# img2 = cv2.erode(img2,kernel,iterations = 1)
	# cv2.imshow("After", img2)
	# time.sleep(0.25)

	# img2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)


	img3 = img4 = img2

	#find contours
	# im2, contours, hierarchy = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	ret,thresh = cv2.threshold(img2,127,255,0)
	im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
	cnt = contours[-1]
	# a.append(cnt)
	M = cv2.moments(cnt)
	# hull = cv2.convexHull(cnt)
	rect = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	# box = box
	cv2.drawContours(img2,[box],0,(255,255,0),2)

	cv2.imshow("After1", img2)
	time.sleep(0.25)

	(x,y),radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	radius = int(radius)
	# cv2.circle(img2,center,radius,(255,0,0),2)

	# cv2.imshow("After2", img2)
	# time.sleep(0.25)


	# ellipse = cv2.fitEllipse(cnt)
	# cv2.ellipse(img2,ellipse,(255,0,0),2)

	# cv2.imshow("After3", img2)

	rows,cols = img2.shape[:2]
	[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
	lefty = int((-x*vy/vx) + y)
	righty = int(((cols-x)*vy/vx)+y)
	# cv2.line(img2,(cols-1,righty),(0,lefty),(255,0,0),2)

	# cv2.imshow("After4", img2)
	# time.sleep(0.25)
	
	a1= box
	a1= check(a1) 
	xx= distanceTwoPoint(a1[0], a1[1])
	yy= distanceTwoPoint(a1[1], a1[2])
	zz= (int)(196/yy*xx)/2
	a2= [[98+zz,195], [98-zz,195], [98-zz,0], [98+zz,0]]



	# Perspective
	pts1= np.array( a1, np.float32)
	pts2= np.array( a2, np.float32)
	M   = cv2.getPerspectiveTransform(pts1,pts2)
	dst = cv2.warpPerspective(img3,M,(28*7,28*7))
	cv2.imshow("Final 1", dst )
	time.sleep(0.25)

	# warpAffine
	pts1= np.array( a1[:3], np.float32)
	pts2= np.array( a2[:3], np.float32)
	M   = cv2.getAffineTransform(pts1,pts2)
	dst = cv2.warpAffine(img4,M,(28*7,28*7))
	cv2.imshow("Final 2", dst)
	time.sleep(0.25)




	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# print( M )

for o in out:
	print(o)
# print( len(a[-1]) )








	#	convour test
	# im2, contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# for contour in contours:
	# 	cv2.drawContours(img2, contour, -1, (255,0,0), 3)

	# # s= input()
	# # cv2.destroyAllWindows()
	# cv2.imshow("Convour image", img2 )






	# countImgs += 1
	# img.save('Image out/number'+str(a[i])+'out'+str(countImgs)+'0.tif')
	# img = deskew( np.array(img) )
	# img = makeImage( img.tolist() )
	# saveImageAfterEdit( img )



