import numpy as np #importing numpy
#mathematical operations
var1 = np.array([(1, 2, 3), (4, 5, 6)])
var2 = np.array([(7, 8, 9), (10, 11, 12)])
print(var1+var2)
print(var1-var2)
print(var1*var2)
print(var1/var2)

print(var1.ravel())
print(var1.sum())
print(var1.max())
print(var1.min())
print(np.std(var1))
print(var1.sum(axis=1))