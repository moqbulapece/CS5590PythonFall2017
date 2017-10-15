from sklearn import svm, datasets,metrics
from sklearn.cross_validation import train_test_split
digitsdataset=datasets.load_digits()
x=digitsdataset.data
y=digitsdataset.target
#split the data to 20% testing data, 80% training data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#Instantiate the estimator by applying linear kernel model
model1 = svm.SVC(kernel='linear', C=1, gamma=1)
#Fit the model on the training data
model1.fit(x_train,y_train)
y_pred=model1.predict(x_test)
#checking the accuracy of the model with digit datasets by linear kernel
print 'By using the digits dataset and SVC linear the accuracy is ',metrics.accuracy_score(y_test,y_pred)
#Instantiate the estimator by applying rbf kernel model
model2 =svm.SVC(kernel='rbf',C=1, gamma=1)
#Fit the model on the training data
model2.fit(x_train,y_train)
y_pred=model2.predict(x_test)
#checking the accuracy of the model with digits datasets by rbf kernel
print 'By using the digits dataset and SVC kernel the accuracy is ',metrics.accuracy_score(y_test,y_pred)
