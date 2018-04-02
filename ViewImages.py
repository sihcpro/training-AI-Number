import csv
from PIL import Image
import numpy as np
import cv2 
# import cv2.cv

maxleng		= 5
imgWidth 	= 28
imgHeight	= 28

a= []
b= []



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


readFileTrain()
# dst = Mat::zeros( imgHeight, imgWidth, CV_8UC3);
# vis = np.zeros(( imgHeight, imgWidth), np.float32)
# ví2 = cv2.CreateMat( imgHeight, imgWidth, cv2.CV_32FC3)
for i in range(maxleng):
	j = list(map(int, b[i]))
	img = makeImage(j)
	countImgs+= 1

	img2 = np.array( img )
	img2 = cv2.resize( img2, None, fx=7, fy= 7)

	# cv2.namedWindow('Window')
	cv2.imshow("Before", img2)

	ret,thresh = cv2.threshold(img2,127,255,0)
	im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
	cnt = contours[0]
	M = cv2.moments(cnt)
	# hull = cv2.convexHull(cnt)
	rect = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	# cv2.drawContours(img2,[box],0,(255,0,0),2)

	# cv2.imshow("After", img2)

	(x,y),radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	radius = int(radius)
	cv2.circle(img2,center,radius,(255,0,0),2)

	# cv2.imshow("After2", img2)

	ellipse = cv2.fitEllipse(cnt)
	# cv2.ellipse(img2,ellipse,(255,0,0),2)

	cv2.imshow("After3", img2)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

	# print( M )










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



