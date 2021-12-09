# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:59:13 2021

@author: WB
"""
import sys

class person():
     population = 0
    
     def __init__(self, age=18, h=170, w=60, salary=10000):
         self.age = age 
         self.h = h
         self.w = w
         self.salary = salary
    
     def get_age(self):
         return self.age
        
     def get_h(self):
         return self.h
     
     def get_w(self):
         return self.w

     def get_salary(self):
         return self.salary
     

class clerk(person):
    def __init__(self,age, h, w, salary, work_year):
        super().__init__(age, h, w, salary)
        self.work_year = work_year
        

tim = clerk(19,178,80,10000,2)
#print(tim.get_w())

        
def test_wrapper(func,x):
    def print_wrap(func,x):
        print("The wrapper started!")
        r = func(x)
        print("The wrapper ended.")
        return r
    return print_wrap

## return a function object, it should be called to run
    
def be_wrapped():
    print("This function will be wrapped.")
    return

def be_wrapped2(x):
    print("Wrapped function with variable.")
    return x**2

#test_func = test_wrapper(be_wrapped)
test2_func = test_wrapper(be_wrapped2,2)

#print(test2_func(be_wrapped2,2))
#test_func(be_wrapped)
        
def test_raise(x):
    if x>2:
        raise ValueError("X too big!")
        
#test_raise(3)

test_arr = [[0]*3]*3
#print(test_arr)

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    LastAnswer = 0
    ans = []
    print(arr)
    #for i in range(n):
    #    print(arr[i])
    for q in queries:
        if q[0]==1:
            idx = (q[1]^LastAnswer) % n
            #print(idx)
            temp = arr[idx]
            temp.append(q[2])
            arr[idx] = temp
            #print(arr[idx])
        if q[0]==2:
            idx = (q[1]^LastAnswer) % n
            #print(idx)
            LastAnswer = arr[idx][q[2]%len(arr[idx])]
            ans.append(LastAnswer)
        print(arr)
    return ans  


test = dynamicArray(2,[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])
for t in test:
    print(t)
    
    
test_st = [i for i in range(11)]
print(test_st)
test_st.pop(-1)
print(test_st)
test_text = '1 97'
test_op = test_text.split()
print(test_op)
s = sum(test_st)
print(s)
l1 = [i for i in range(1,4)] #
l2 = [i for i in range(4,7)]
l3 = [i for i in range(7,10)]
s1, s2, s3 = map(sum, [l1,l2,l3])
print(s1, sum(l1))
print(s2, sum(l2))
print(s3,sum(l3))