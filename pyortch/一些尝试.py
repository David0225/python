# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:18:19 2018

@author: wuzw
"""
import torch as t
from torch.autograd import Variable as v

a = v(t.FloatTensor([2, 3]), requires_grad=True)
b = a + 3
c = b * b * 3
out = c.mean()
out.backward()
print('*'*10)
print('=====simple gradient======')
print('input')
print(a.data)
print('compute result is')
print(out.data[0])
print('input gradients are')
print(a.grad.data)


m = v(t.FloatTensor([[2, 3]]), requires_grad=True)
n = v(t.zeros(1, 2))
n[0, 0] = m[0, 0] ** 2
n[0, 1] = m[0, 1] ** 3

n.backward(m.data)
n.backward(t.FloatTensor([[1,1]]))
m.grad


m = v(t.FloatTensor([[2, 3]]), requires_grad=True)
j = t.zeros(2 ,2)
k = v(t.zeros(1, 2))
#m.grad.data.zero_()
k[0, 0] = m[0, 0] ** 2 + 3 * m[0 ,1]
k[0, 1] = m[0, 1] ** 2 + 2 * m[0, 0]

k.backward(t.FloatTensor([[1,1]]))

m.grad
