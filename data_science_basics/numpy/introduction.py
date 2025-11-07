import numpy as np
lst = [1,2,3]
arr = np.array([
                [1,2,3],
                [3,4,6],
                [4,5,7]
                ])
print('Print the array \n',arr)
print('Print the shape of array\n',arr.shape)
print('================================')
# Scalar Arithmatic
arr = np.array([1,2,3])
print(f'Multipy {arr} by 3\n',arr * 3)
print('================================')
print(f'Add {arr} by 1\n',arr +1)
print('================================')
print(f'Differentiate {arr} by 2\n',arr -2)
print('================================')
# Vectroized math function
print(f'square root of each value of array\n{np.sqrt(arr)}')
print('================================')
arr = np.array([1.2,3.4,2.7])
print(f'Round each value of array\n{np.round(arr)}')
print('================================')
print(f'Floor each value of array\n{np.floor(arr)}')
print('================================')
print(f'Ciel each value of array\n{np.ceil(arr)}')
print('================================')
# Element-wise arithmatic
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(f'Add {arr1} + {arr2} \n {arr1+arr2}')
print('================================')
print(f'Diffrentiate {arr1} - {arr2} \n {arr1-arr2}')
print('================================')
print(f'Multiply {arr1} * {arr2} \n {arr1*arr2}')
print('================================')
print(f'Divide {arr1} / {arr2} \n {arr1/arr2}')
print('================================')
# Comparison Operators
scores = np.array([100,50,39,78,87,10])
print('What values are 60 or above',scores>=60)
print('================================')
# Broadcasting allows Numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.
# the dimensions have the same size or one of the dimensions has a size of one.
# Create bellow arries 
# [1 2 3 4]
#  [2]
#  |3|
#  |4|
#  [5]
arr1 = np.array([[1,2,3,4]])
arr2 = np.array([[2],[3],[4],[5]])
print('Shape of first array',arr1.shape)
print('Shape of second array',arr2.shape)
print('Broadcastinf first array into second array\n',arr1*arr2)
print('================================')
# Aggregative functions = summarize data and typically return a single value

print('================================')



