# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:48:44 2021

@author: WB
"""


## These problems are from "Classic Computer Problems in Python" by David Kopec.
## However, these are not the code in the book. 
## I write these for practice my understanding of concepts and ideas

### CH 1 
### Problems 1: The Fibonacci sequence
# Input: integer n, Output: nth fibonacci number

# Recurrive solution:
def fibo_recur(n):
    # N should be no less than 0
    if n<0:
        return "Key Error"
    # Base case
    if n<=1:
        return n
    #Recursive call
    return fibo_recur(n-1) + fibo_recur(n)

# Dynamic programming & Memoization to the rescue:
# this is my solution:
def fibo_dc(n):
    if n==0:
        return 0
    #if n==1:
    #    return 1
    fibo=[0]*(n+1)
    fibo[0],fibo[1] = 0, 1
    if n>=2:
        for i in range(2,n+1):
            fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]

'''
# solution1 in book:
from typing import Dict
# set mem to be a dict type with int as keys and values and put 0, 1 in mem
mem: Dict[int,int] ={0:1,1:1} 
def fibo_mem1(n:int)->int:
    if n not in mem:
        mem[n] = fibo_mem1(n-1) + fibo_mem1(n-2)
    return mem[n]
'''
# solution2 in book: ###----> this is used for exercise 1
from functools import lru_cache
@lru_cache(maxsize=None)
def fibo_mem2(n: int) -> int: 
    if n < 2: # base case
        return n
    return fibo_mem2(n - 2) + fibo_mem2(n - 1) # recursive case
    
# Generator: create the fibonacci sequence
# These are my codes:
def fibo_series_1(n):
    # return a list and print the list to generate the sequence
    fibo=[0]*n
    fibo[0],fibo[1] = 1, 1
    if n>=2:
        for i in range(2,n):
            fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo

def fibo_series_2(n):
    # return a generator --> save space
    yield 0 # n=0
    if n>0:
        yield 1 # start from n=1
    n2 = 0
    n1 = 1
    for _ in range(2,n):
        cur = n1 + n2
        n1,n2 = cur ,n1
        yield cur

'''
# Solution from book:
from typing import Generator
def fib6(n: int) -> Generator[int, None, None]:
     yield 0 # special case
     if n > 0: yield 1 # special case
     last: int = 0 # initially set to fib(0)
     next: int = 1 # initially set to fib(1)
     for _ in range(1, n):
         last, next = next, last + next
         yield next # main generation step    
''' 

        
### Problem 2: Compression (Trivial)
         
# Test: converting  string of A C G T to bit string (These are my codes):
def str_to_bstr(string):
    bit_string = 1
    for c in string:
        bit_string <<= 2
        if c == 'A':
            bit_string |= 0b00
        if c == 'C':
            bit_string |= 0b01
        if c == 'G':
            bit_string |= 0b10
        if c == 'T':
            bit_string |= 0b11
    return bit_string        
# Test convert bit string to ACGT string(gene string), these are my codes:
def bstr_to_str(bstring):
    result = ''
    # bin(int) add 0b to bit string so the length should -2, can use int.bit_length() instead
    for i in range(0,len(bin(bstring))-3,2):
        bits = bstring>>i & 0b11
        if bits == 0b00:
            result += 'A'
        if bits == 0b01:
            result += 'C'
        if bits == 0b10:
            result += 'G'
        if bits == 0b11:
            result += 'T'
    return result[::-1]
# My simple test
str1 = str_to_bstr('ACGTACCGGT')
str2 = bstr_to_str(str1)   
assert str2=='ACGTACCGGT', 'Converting Error'  
# Testing compress size:
from sys import getsizeof
test_string = "ACCCTAGGGAATCTCAAGGTTCCCGGATTAGGCGAA"*100
print(len(test_string))
print('The size before being compressed is {} bytes'.format(getsizeof(test_string)))
print('The size after being compressed is {} bytes'.format(getsizeof(str_to_bstr(test_string))))
print('The compression rate is {:.2f}% '.format((getsizeof(str_to_bstr(test_string))/getsizeof(test_string))*100))
assert bstr_to_str(str_to_bstr(test_string))==test_string, 'Converting Error'

### One-time pad encryptrion
from secrets import token_bytes
## method :
# Encrypt
# 1.convert original string to utf-8 bytes
# 2. Use utf-8 byte length as input to token_bytes() to generate key with proper length
# 3. Convert utf-8 bytes to int bit strings
# 4. Use (random key) XOR (original bit strings) to get the encrypted 
# Decrypt
# 1. Use (encrypted) XOR (random key) to get original bit string
# 2. Find the proper bytes length: (len(original bit string) + 7) //8 --> need one more bytes for the remainder
# 3. Convert bit string to utf-8 bytes
# 4. Convert utf-8 bytes to string
# generate random key
def random_key(key_length):
    tb = token_bytes(key_length)    
    return int.from_bytes(tb,'big')
#print(len(bin(random_key(7))))
#print("this is a test".encode())

# generate dummy data and pad with original data to encrypt
def encrypt(string):
    #dummy'length should be equal to string
    original_b = string.encode()
    dummy = random_key(len(original_b))
    original_key = int.from_bytes(original_b,'big')
    encrypted = dummy ^ original_key
    return dummy, encrypted

# decrypt: using a^b=c, c^b=a, c^b=a 
#--> dummy ^ original = encry --> encry ^ dummy = original 
def decrypt(dummy, encrypted):
    original_key = dummy ^ encrypted
    original_b = original_key.to_bytes((encrypted.bit_length()+7)//8,'big')
    return original_b.decode()

test_string = "this is a test"
test_encrypted = encrypt(test_string)
test_decrypted = decrypt(test_encrypted[0], test_encrypted[1])
assert test_decrypted == test_string, "Ecrypt-Decrypt Error"


### Caculating PI:
# Use Leibniz formula = 4*(1 + (-1**k)/(1 + 2**k) for k =1 to inf )
#import sys
def leibniz_pi(size):
    upper = 4.0
    lower = 1.0
    sign = 1.0
    pi = 0.0
    for i in range(size):
        pi += sign*(upper/lower)
        lower += 2.0
        sign *= -1.0       
    return pi
#print(sys.maxsize)
#for size in range(1000000):
#    print(leibniz_pi(size)) --> converge to pi when it adds to infi
    
    
### Tower of  Hanoi:
# Using stack
class stack():
    def __init__(self):
        self._container = []
    def pop(self):
        #last = self._container[-1]
        #self._container = self._container[:-1]
        return self._container.pop()
    def push(self,T):
        self._container.append(T)
    def __repr__(self):
        return repr(self._container)
        
# three towers:
tower_a = stack()
tower_b = stack()
tower_c = stack()
number_of_discs = 10
for i in range(1, number_of_discs+1):
    tower_a.push(i)
print("Before Moving")
print(tower_a)
print(tower_b)
print(tower_c)
print()

def hanoi_tower(ta,tb,tc,n):
    # ta: begin, tb: middle, tc: end, n: disc numbers
    if n==1:
        tc.push(ta.pop())
    else:
        hanoi_tower(ta,tc,tb,n-1)
        hanoi_tower(ta,tb,tc,1)
        hanoi_tower(tb,ta,tc,n-1)
hanoi_tower(tower_a,tower_b,tower_c,number_of_discs)
print("After Moving")
print(tower_a)
print(tower_b)
print(tower_c)

##### Excercise:
###1
# Test my Fibonacci code:
# use book solution (fibo_mem2):
for i in range(200):
    assert fibo_dc(i) == fibo_mem2(i), "Fibonacci Error: your answer is {d1}, correct is {d2}".format(d1=fibo_dc(i),d2=fibo_mem2(i))

###2: Create integer wrapper so that integer can be use as bit string        
class int_bit_string(int):
    def __init__(self,integer):
        self.bit_string = integer << 2
    def __repre__(self):
        return repr(self.bit_string)
    def __getitem__(self,index): ## Not sure what this is for in this class
        return self.bit_string[index]
int_test = int_bit_string(3)
print(int_test)
print(3<<2)
###3