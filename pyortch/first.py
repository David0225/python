# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 10:04:02 2018

@author: wuzw
"""
from __future__ import print_function
import torch
from torch.autograd import Variable

x = torch.Tensor(5, 3)
print(x[:,1][1])

print(type(x))

x = torch.randn(4, 4)
y = x.view(16,1)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())


a = torch.ones(5)

b=a.numpy()
a.add(1)

import numpy as np
a=np.ones(5)
b=torch.from_numpy(a)
c=torch.from_numpy(a)
np.add(a,1,out=a)

torch.cuda.is_available()
b=b.cuda()
c=c.cuda()
b+c


x = torch.randn(3)
x = Variable(x, requires_grad=True)
x.grad

x = Variable(torch.ones(2, 2), requires_grad=True)

y = x + 2
print(y)
y.grad_fn
x.grad
z = y * y * 3
out=z.mean()
out.backward()
x.grad




x = torch.randn(3)
x = Variable(x, requires_grad=True)

y = x * 2
while y.data.norm() < 1000:
    y = y * 2

print(y)

gradients = torch.FloatTensor([0.1, 1.0, 0.0001])
#gradients = torch.FloatTensor([1.0, 1.0, 1.0])
y.backward(gradients)

print(x.grad)
