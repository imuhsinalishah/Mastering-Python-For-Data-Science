import numpy as np #importing numpy
var1 = np.array([1, 2, 3]) #creating first arrays
var2 = np.array([4, 5, 6]) #creating second arrays
var3 = np.add(var1, var2) #addition of var1 and var2
print(var1+var2) #displaying the result
print(var3) #displaying the result

# to print 2 arrays in one line
print(np.array([7,8,9]), np.array([10, 11, 12])) # or another method
var = np.array([7,8,9]),([10, 11, 12])
print(var)

# to add 2 arrays
var5 = np.array([(1, 2, 3), (4, 5, 6)])
var6 = np.array([(7, 8, 9), (10, 11, 12)])
print(var5+var6)