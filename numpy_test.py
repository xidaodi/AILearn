import numpy as np


# method1
arr1=np.zeros(5)
arr2=np.zeros([5,3],dtype=int)
print(arr1)
print(arr2)

# method2
arr3=np.array([[1,2,3],[4,5,6],[7,4,5]])
print(arr3)
print(arr3.shape)

# method3
arra4=np.arange(0,10,0.5)
print(arra4)

# method4
arra5=np.linspace(0,10,20)
print(arra5)

# can be any of type
arra6=np.array(['hello',1,2,3,4],dtype=object)
print(arra6)