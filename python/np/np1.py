# -*- encoding:utf-8 -*-
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(np.zeros((2, 3)))
print(np.ones((2, 4)))
print(np.empty((2, 3)))
print(np.arange(10, 30, 5))
print(np.arange(0, 3, 0.3))
# 第三个参数为元素个数，而非步长
print(np.linspace(0, 3, 10))

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(b)
print(a-b)
print(b*2)
print(a < 30)
print(a * b)
print(a.dot(b))

print(a.sum())
print(a.min())
print(a.max())

a = np.arange(12).reshape(3,4)
print(a)
print(a.sum(axis=0))
print(a.sum(axis=1))

a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])
print(a[:6:2])
print(a[::-1])

a = np.floor(10*np.random.random((3, 4)))
print(a)
print(a.shape)
print(a.ravel())
print(a.reshape(6,2))

print(a.T)
print(a.T.shape)

a = np.arange(12)
b = a
print(b is a)
b.shape = 3, 4
print(a.shape)

def f(x):
    print(id(x))

print(id(a))
f(a)
c = a.view()
print(c is a)
print(c.base is a)
c.shape=2, 6
print(a.shape)
print(c)
print(a)
c[0, 3] = 1111
print(a)


d = a.copy()
print(d is a)
print(d.base is a)
print(a)
d[0, 3] = 2222
print(a)

a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
print(a)
print(a[i])
j = np.array([[3, 4], [9, 7]])
print(a[j])

a = np.arange(12).reshape(3, 4)
print(a)

i = np.array([[0, 1], [1, 2]])
j = np.array([[2, 1], [3, 3]])
print(j)
# 配对原则如下理解，i标示一维，j标示2维（0,2）(1,1)/(1,3)(2,3)
print(a[i, j])

