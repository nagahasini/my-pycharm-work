import numpy as np
a=np.array([1,2,3])
print(a)

b=np.ones((3,4))
c=np.full((4,4),2)

m=np.matmul(b,c)
print(m)



ex=np.array([[1,2,3],[4,5,6]])
print(ex)
print(np.sum(ex,axis=0))