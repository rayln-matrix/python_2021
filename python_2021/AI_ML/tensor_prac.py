# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:09:22 2021

@author: WB
"""


import torch
import tensorflow as tf


# initiate a tensor
tensor_1  = torch.arange(12)
#tensor_2 = tf.range(12)
print(tensor_1)
#print(tensor_2)

# Size
print(tensor_1.size())
#print(tf.size(tensor_2))

print(tensor_1.numel())
#print(tf.shape(tensor_2))

# Zeros and ones:
t_o_1 = torch.ones((2,3,4))
#t_o_2 = tf.ones((2,3,4))

t_z_1 = torch.zeros((2,3,4))
#t_z_2 = tf.zeros((2,3,4))

print("from torch: ")
print(t_o_1, t_z_1)
#print("from tf: ")
#print(t_o_2, t_z_2)

# Broadcasting:
b_1 = torch.arange(4).reshape(4,1)
b_2 = torch.arange(2).reshape(1,2)
print(b_1)
print(b_2)
print(b_1 + b_2)

# Memory location
# Re assign will induce reallocate
before = id(b_1)
b_1 = b_1 + b_2
print(before == id(b_1))

# In-place (without reallocate)
new = torch.zeros_like(b_1)
print(id(new))
new[:] = b_1 + b_2
print(id(new))
# In-place:
b_1 = torch.arange(4)
b_2 = torch.ones(4)
print(b_1.size())
print(b_2.size())
before = id(b_1)
b_1[:] = b_1 + b_2 
print(id(b_1) == before)

### Exercise:

x = torch.randn(4,4,4)
y = torch.randn(4,4,4)
print(x==y)
print(x>y)
print(x<y)

x = torch.arange(3).reshape(3,1)
y = torch.arange(5).reshape(1,5)
print(x + y)


###################

# Linear Algebra
x = torch.tensor(3.0)
y = torch.tensor(4.0)
z = torch.tensor([1,2,3])
print(x + y)
print(x + z)
print(z.shape)
print(len(z))

# Hadamard product
x = torch.arange(12).reshape(2,2,3)
y = torch.ones((2,2,3))
y = 2*y
print("x is: ", x)
print("y is: ", y)
print("Hadamard product of x and y is:", x*y)

# Reduction:
x_ax_0 = x.sum(axis = 0) # reduce axis 0 to scaler
x_ax_1 = x.sum(axis = 1)
x_ax_2 = x.sum(axis = 2)
print('Axis 0:', x[:,0,0])
print('Axis 1:', x[0,:,0])
print('Axis 2:', x[0,0,:])

print("Reduce axis 0:")
print('x_ax_0 :',x_ax_0)
print(x_ax_0.shape)

print("Reduce axis 1:")
print('x_ax_1 :',x_ax_1)
print(x_ax_1.shape)

print("Reduce axis 2:")
print('x_ax_2 :',x_ax_2)
print(x_ax_2.shape)

# Without reduction: keep the dimension:
x_kd_ax_0 = x.sum(axis = 0,keepdims = True)
print(x_kd_ax_0)
print(x_kd_ax_0.shape)
print(x+x_kd_ax_0)
x_cumsum_ax_0 = x.cumsum(axis = 0)
print(x_cumsum_ax_0)
print(x_cumsum_ax_0.shape)
A = torch.arange(20).reshape(5,4)
print(A)
print(A.shape)
print(A.cumsum(axis = 0))  

#Dot product:
x = torch.arange(15, dtype=torch.float32)
y = torch.ones(15, dtype=torch.float32)
print(x)
print(y)
print(torch.dot(x,y)) ## Warning: be careful of the data type
print(torch.sum(x*y))

# Matrix-Vector product
A = torch.arange(20).reshape(5,4)
x = torch.arange(4)
print(A)
print(x)
print(torch.mv(A,x)) # projecting n-vector to m vector

# Matrix-Matrix product
#B = A.clone().T
B = torch.ones(4,3,dtype=torch.long)
print(torch.mm(A,B))

# Norm:
u = torch.tensor([3.0,-4.0])
print(torch.norm(u))  # this is L2 norm
print(torch.abs(u).sum()) # this is L1 norm
# Frobenius norm of a matrix
m = torch.ones(4,9) # 4*9=36, 36**1/2 = 6
print(torch.norm(m))
x = torch.ones(2,3,4)
print(x.shape)
print(len(x))

# Excercise:
A = torch.arange(20).reshape(5,4)
print(A)
## print(A/A.sum(axis=1)) ---> the dimension is reduced so no broadcast--> error
print(A/A.sum(axis=1,keepdims = True))
B = torch.ones(2,3,4)
print(B.shape)
B_ax_0 = B.sum(axis=0)
B_ax_1 = B.sum(axis=1)
B_ax_2 = B.sum(axis=2)
print(B_ax_0.shape)
print(B_ax_1.shape)
print(B_ax_2.shape)

###################
#  Caculus : Auto differentiation---> Warning: Must not re-allocate memory

x = torch.arange(4.0, requires_grad = True)
y = 2*torch.dot(x,x)
print(x)
print(x.grad)
print(y)
y.backward()
print(x.grad)
y = x.sum() # y = dot(x,ones(shape_of_x))
y.backward()
print(x.grad) # grad is accumulated
x.grad.zero_() # clear
y.backward()
print(x.grad)
x.grad.zero_()
y = x*x
#y.backward()  ---> error: grad can be implicitly created only for scalar outputs
#print(x.grad)
#x.grad.zero_()
#y.sum().backward()  ---> this is the same as y.backward(torch.ones(len(x))) ???
#print(x.grad)

# Detach computation
x.grad.zero_()
u = y.detach()
z = u*x
z.sum().backward()
print(x.grad == u)
x.grad.zero_()
y.sum().backward()
print(x.grad == 2*x)

# Computing the Gradient of Python Control Flow
test = torch.ones(5,dtype = torch.float32)
k = torch.sum(test*test)
print(k)
print(test.norm() == k**(1/2)) # Ckecking norm function: L2 norm

def f(a):
    b = 2*a
    while b.norm()<1000:
        b = b*2
    if b.sum()>0:
        c = b
    else:
        c = 100*b
    return c

a = torch.randn(size=(),requires_grad=True)
print(a)
d = f(a)
d.sum().backward()
print(a.grad == d/a)

### Exercises:
a = torch.arange(5.0, requires_grad=True)
h = 2*torch.dot(a,a)
#h.backward()
#g = a.grad
#g.backward()
#h.backward() ---> RuntimeError: Trying to backward through the graph a second time, but the saved intermediate results have already been freed. Specify retain_graph=True when calling backward the first time.
# WHy second derivative is expensive?


###################

# Probability:

from torch.distributions import multinomial as multnml

prob_ideal = torch.ones(6)/6
#print(prob_distru)
test_1 = multnml.Multinomial(1000, prob_ideal).sample() ## a sample with 1000 tries
print(test_1)

count = multnml.Multinomial(10,prob_ideal).sample((500,)) ## 500 samples each with 10 tries
print(count.shape)
#x = torch.ones(4,2)
#print(x.cumsum(axis = 0))
#print(x.cumsum(axis = 1))
print(count.cumsum(axis = 0))
count_sum = count.cumsum(axis=0) ## 累加每次sample每種事件的發生次數--sample1 + sample2 + sample3...
#print(count_sum[-1].sum()) ### this is 500*10 =5000
#print(count_sum.sum(dim = 1, keepdim = True)) 10 for each sample--> add up from 10 to 5000
estimate = count_sum / count_sum.sum(dim=1, keepdim=True) #
print(dir(multnml))

