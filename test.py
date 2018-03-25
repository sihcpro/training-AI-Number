from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
# print("DATA")
# print(digits.images[0])
# print(digits.target[1])
X_train, X_test, y_train, y_test = train_test_split(digits.images, digits.target,test_size=0.2, random_state=0)
print("y_train",len(X_train))
print("y_test", len(X_test))

######### Xem bo test
# for i in range(4):
# 	print( "--------------------------" )
# 	print( X_train[i] )
# 	print( y_train[i] )
# 	print( "--------------------------" )



# print ("*************************")

######### Xem cong dung reshap
# print(X_train[0])
# a= X_train[0]
# a.shape
# b= a.reshape((1, 8*8));
# print(b)

######### Su dung SVM
# clf = svm.SVC()
# # iris = datasets.load_iris()

# #	dung het bo test
# # X= digits.images
# # y= digits.target
# # nsamples, nx, ny = X.shape
# # d2_train_dataset = X.reshape((nsamples,nx*ny))
# # clf.fit(d2_train_dataset, y)

# nsamples, nx, ny = X_train.shape
# d2_train_dataset = X_train.reshape((nsamples,nx*ny))
# clf.fit(d2_train_dataset, y_train)


# nsamples, nx, ny = X_test.shape
# d2_train_dataset = X_test.reshape((nsamples,nx*ny))
# kq= clf.score(d2_train_dataset, y_test)
# print( kq )

sv = svm.LinearSVC()
X_train = X_train.reshape(len(X_train), -1)
X_test  = X_test.reshape(len(X_test), -1)

sv.fit( X_train, y_train)
kq= sv.score( X_test, y_test)
print(kq)


