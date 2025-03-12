import numpy as np
# a=np.array([1,2,3])
# print(a)
#
# b=np.ones((3,4))
# c=np.full((4,4),2)
#
# m=np.matmul(b,c)
# print(m)
#
#
#
# ex=np.array([[1,2,3],[4,5,6]])
# print(ex)
# print(np.sum(ex,axis=0))

# ex=np.arange(25).reshape(5,5)
# print(ex)
#
# m=np.arange(12).reshape(2,3,2)
# print(m)

# hstack and vstack for normal stacking

#misllaneous
a=np.genfromtxt('t.txt')
a=a.astype('int32')
print(a)

print(a[a>6])

#iteration in arrayy
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
for row in arr:
    print(row)

for i in arr.flat:
    print(i)

# splittingggg
