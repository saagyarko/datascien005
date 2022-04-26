#creating arrays from a list
import numpy as np
mia=np.array([1,4,2,3,5])
print(np.array([3.14,4,6,3], dtype='int'))
print(mia)
mia1=np.zeros(10, dtype=int)
print(mia1)
#nested arrays of multidimensional
nested= np.array([range(i, i+3) for i in [2,4,6,]])
print(nested)

#creating arrays from scratch
li=np.zeros(12, dtype='int')
print(li)

l2=np.ones((3,5),dtype='int')
print(l2)
l3=np.full((3,5), 3.14)
print(l3)

#array with linear sequence
l4=np.arange(2,20,2 )
print(l4)

#Create an array of five values evenly spaced
# between 0 and 1
l5=np.linspace(0, 1,5)
print(l5)

#Create a 3x3 array of uniformly distributed
# random values between 0 and 1
l6=np.random.random((3,3))
print(l6)

 # Create a 3x3 array of normally distributed random values
 # with mean 0 and standard deviation 1
l7=np.random.normal(0,1,(3,3))
print(l7)

# Create a 3x3 array of random integers in the interval [0, 10)
l8= np.random.randint(0,10,(3,3))
print(l8)

# Create a 3x3 identity matrix
l9=np.eye(3)
print(l9)

#Numpy attribute
# seed for reproducibility
#creating multidimensions(1d,2d,3d)
np.random.seed(0)
x1=np.random.randint(10, size=6)
x2=np.random.randint(10, size=(3,4))
x3=np.random.randint(10, size=(3,4,5))

print(x3.ndim)
print(x3.shape)
print(x3.size)

#datatype
print("dtype: ", x3.dtype)
print(x3.itemsize)
print(x3.nbytes)

print(x1)
print(x2)
print(x2[0,0])

#One-dimensional subarrays
l10=np.arange(10)
print(l10)
print(l10[::2])
print(l10[1::2])

#Multidimensional subarrays
print(x2[:3, :2])

#Creating copies of arrays
x2sub=x2[:2, :2].copy()
print(x2sub)

#Reshaping of Arrays
grid=np.arange(1,10).reshape((3,3))
print(grid)

x=np.array([1,3,4])
# row vector via reshape
print(x.reshape(1,3))
# row vector via newaxis
print(x[np.newaxis, :])
# column vector via reshape
print(x.reshape((3, 1)))

#Concatenation of arrays
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))

x11=np.array([1,3,5])
y11=np.array([5,3,1])
conc=np.concatenate([x11,y11])
print(conc)
