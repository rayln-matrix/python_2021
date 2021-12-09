# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:12:19 2021

@author: WB
"""


### Linear neural networks: linear regression , softmax regression
## Keys: Minibatch stochastic gradient descent, Hyperparameter tuning

import math
import time
import numpy as np
import torch
import random


### Experiment on vectorization
class Timer:
    def __init__(self):
        self.time = []
        self.start()
        
    def start(self):
        self.tik = time.time()
        
    def stop(self):
        # return the last timing (end - start)
        self.time.append(time.time()-self.tik)
        return self.time[-1]
    
    def avg(self):
        return sum(self.time)/len(self.time)
    
    def sum_(self):
        return sum(self.time)
    
    def cumsum(self):
        return np.array(self.time).cumsum().tolist()
    
    
n = 100000
a = torch.ones(n)
b = torch.ones(n)
#time for using for-loop:
c = torch.zeros(n)
timer = Timer()
for i in range(n):
    c[i] = a[i] + b[i]
    timer.stop()
print("The time for every steps:")    
print(timer.time)
print("Total time:")
print(f"{timer.sum_():.5f} sec")
print("Average time:")
print(f"{timer.avg():.5f} sec")

#time for using vectorization
timer2 = Timer()
d = a + b
timer2.stop()
print("The time for every steps:")    
print(timer2.time)
print("Total time:")
print(f"{timer2.sum_():.5f} sec")
print("Average time:")
print(f"{timer2.avg():.5f} sec")

#### Ch3.1 practice on paper (2021/12/01---not finished yet)


## testing Simple linear regression:
def synthetic_data(w, b, num_examples):  #this function is from book
    """Generate y = Xw + b + noise."""
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))

w_init = torch.tensor([2,-3.4]) # random w 
b_init = 4.2 # random b
features, labels = synthetic_data(w_init,b_init,10000)
#print('features:', features,'\nlabel:', labels)

def get_minibatch(batch_size, features, labels):
    number_of_examples = len(features)
    indice = list(range(number_of_examples))
    random.shuffle(indice)
    #for i in range(0, number_of_examples, batch_size):
    #    batch_indice = torch.tenor([random.randint(0,number_of_examples) for _ in range(batch_size)])
    # above code may not exhaust the data set and can sample same data multiple times
    
    ## Below is implementation from book
    for i in range(0, number_of_examples, batch_size):
        batch_indice = torch.tensor(indice[i:min(i+batch_size, number_of_examples)])  
        yield features[batch_size], labels[batch_size]
        
def lin_regre(x,w,b):
    # Function from book
    return torch.matmul(x,w) + b

def loss_function(y_target, y):
    # Function from book
    return (y_target - y.reshape(y_target.shape))**2/2

def opt_sgd(params, lr, batch_size):
    # Function from book
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()


w = torch.normal(0,0.001, size=(2,1), requires_grad = True)
b = torch.zeros(1,requires_grad = True)
print(w)
print(b)

### Training 

lr = 0.03
num_epochs = 100
net = lin_regre
loss = loss_function
batch_size = 10

for epoch in range(num_epochs):
    for X, y in get_minibatch(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # Minibatch loss in `X` and `y`
        # Compute gradient on `l` with respect to [`w`, `b`]
        l.sum().backward()
        opt_sgd([w, b], lr, batch_size)  # Update parameters using their gradient
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')
        
        
### 3.2 exercise not finished (2021/12/01)        