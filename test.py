from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
print("DATA")
print(digits.images[0])
print(digits.target[1])
X_train, X_test, y_train, y_test = train_test_split(digits.images, digits.target,test_size=0.4, random_state=0)
print("y_train",len(y_train))
print("y_test", len(y_test))