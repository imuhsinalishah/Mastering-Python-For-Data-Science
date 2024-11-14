import numpy as np #importing numpy
var1 = np.array([1, 2, 3]) #creating first arrays
print(var1.itemsize) #size of the array
print(var1.dtype) #type of the array
print(var1.ndim) #dimension of the array

var2 = np.array([(4, 5, 6), (7, 8, 9)]) #two dimensional array
print(var2.ndim) #dimension of the array
print(var2.size) #size of the array
print(var2.shape) #shape of the array 2rows and 3columns
var3 = var2.reshape(3, 2) #reshaping the array
print(var3)
