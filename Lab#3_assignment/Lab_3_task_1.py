import numpy as np
import matplotlib . pyplot as plt
##own dataset for predicting y for x
x = np. array ([0,1,2,3,4,5,6,7,8,9])
y =np.array([1,3,2,5,7,8,8,9,10,12])
#apply linear regrssion formula on the dataset to generate the predicting model for y where x as input
xbar = np.mean(x)
ybar=np.mean(y)
xi_min_x=x-xbar
yi_min_y=y-ybar
xi_min_x_sq=xi_min_x * xi_min_x
p=np.sum(xi_min_x_sq)
mult_x_y=xi_min_x * yi_min_y
q=np.sum(mult_x_y)
beta_1= q/p
beta_0=ybar-(beta_1*xbar)
r=beta_0 + (beta_1*x)
#plot the scatter value and generated line after applying linear regression model on the dataset

predict_x = 13 #give a input value for predicting y
predict_y = beta_0+(beta_1*predict_x)
#print the predicted output value
print 'the predicted value for the input 13 is',predict_y
plt . plot (x , r,color='yellow')
plt . scatter(x , y,color='red')
plt .show()


