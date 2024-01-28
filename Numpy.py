import numpy as np

a = np.array([1, 2, 3])
print(a)

print(a[0])
a[0] = 10
print(a)

b = a * np.array([1, 0, 5])
print(b)
 
liste = [1, 2, 3]   
a = np.array([1, 2, 3])

liste = liste * 2
print(liste) # [1, 2, 3, 1, 2, 3]
a = a * 2
print(a) # [2 4 6]

# dot product
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
a1 = np.array(liste1)
a2 = np.array(liste2)
# 1*4 + 2*5 + 3*6 = 32
dot = 0
for i in range(len(liste1)):
    dot += liste1[i] * liste2[i]
print(dot) # 32

dot = np.dot(a1, a2)
print(dot) # 32

sum1 = a1 * a2
dot = np.sum(sum1)
print(dot) # 32
dot = a1 @ a2
print(dot) # 32

# nd arrays
a3 = np.array([[1, 2, 3], [4, 5, 6]])
print(a3.shape) #(3, 3)
print(a3.T) # [[1 4][2 5][3 6]]

# indexing/slicing/boolen
a4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a4)
b = a4[0, 1:3]
print(b) # [2 3]
b = a4[:, 1]
print(b) # [2 6]

a5 = np.array([[1, 2], [3, 4], [5, 6]])
print(a5)
print(a5[a5 > 2])

b = np.where(a5>2, a5, -1)
print(b)

a6 = np.array([10, 19, 21, 40, 53, 67])
print(a6)
b = [1, 3, 5]
print(a6[b])

even = np.argwhere(a6%2==0) # [[0] [3]]
even = np.argwhere(a6%2==0).flatten() # [0 3]
print(a6[even])

a7 = np.arange(1,7)
print(a7) # [1 2 3 4 5 6]

b = a7.reshape((2,3))
print(b) # [[1 2 3] [4 5 6]]

a8 = np.array([[1, 2], [3, 4]])
print(a8)
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a8,b))
print(c) # [[1 2] [3 4] [5 6] [7 8]]

# broadcasting
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
#a9 = np.array([3, 5, 1], [3, 5, 1], [3, 5, 1], [3, 5, 1])
a9 = np.array([3, 5, 1])
y = x + a9
print(y)

a10 = np.array([[3, 5, 1, 7, 5, 2], [8, 4, 2, 7, 5, 9]])
print(a10)
print(a10.sum(axis=None)) # 58
print(a10.sum(axis=0)) # [11  9  3 14 10 11]
print(a10.sum(axis=1)) # [23 35]

# datatypes
x = np.array([1, 2, 3])
print(x)
print(x.dtype)

#copying
a11 = np.array([1, 2, 3])
b = a11
b[0] = 9
print(b) # [9 2 3]
print(a11) # [9 2 3]

b = a11.copy()
b[0] = 9
print(b) # [9 2 3]
print(a11) # [1 2 3]

# generating arrays
a12 = np.zeros((2, 3))
print(a12) # [[0. 0. 0.] [0. 0. 0.]]

a13 = np.ones((2, 3), dtype="int32")
print(a13) # [[1 1 1] [1 1 1]]

a14 = np.full((2, 3), 9)
print(a14) # [[9 9 9] [9 9 9]]

a15 = np.eye(4, dtype="int32")
print(a15) # [[1 0 0 0] [0 1 0 0] [0 0 1 0] [0 0 0 1]]

a16 = np.arange(5)
print(a16) # [0 1 2 3 4]

a17 = np.linspace(3, 21, 4) # (başlangıç, bitiş, eleman sayısı)
print(a17) # [ 3  9 15 21]