import numpy as np #importing numpy
var1 = np.linspace(10, 50, 5)  #creating auto  5 numbers from 10 to 50
print(var1) #displaying the result

#slicing a number
var2 = np.array([(1, 2, 3), (4, 5, 6)]) # creatomt two dimensional array
print(var2[0, 1]) #displaying the result

#printing multiple slicing numbers
var3 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(var3[0:,0]) #displaying the result of all first numbers
print(var3[0:,1]) #displaying the result of all middle numbers
print(var3[0:,2]) #displaying the result of all last numbers

#Min Max & Sum
var4 = np.array([(1, 2, 3), (4, 5, 6)])
print(var4.min()) #displaying the result of min
print(var4.max()) #displaying the result of max
print(var4.sum()) #displaying the result of sum    
