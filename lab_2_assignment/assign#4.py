import numpy as npy #import numpy module as the name npy
rand_number= npy.random.random(15)#create the random variable
print("Random vector of size 15:")
print(rand_number)
rand_number[rand_number.argmax()] = 100 #replace the maximum value by 100
print("Maximum value is replaced by the value of 100:")
print(rand_number)