# -*- coding: utf-8 -*-
"""
Created on Mon May 17 08:52:08 2021

@author: WB
"""


def max_pairwise_product(numbers):
    #max_1 = 0
    maxi_1 = 0
    
    #max_2 = 0
    #maxi_2 = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[maxi_1]:
            #max_1 = numbers[i]
            maxi_1 = i
    if maxi_1 == 0:
        maxi_2 = 1
    else:
        maxi_2 = 0        
    for j in range(len(numbers)):
        if (numbers[j] > numbers[maxi_2]) and (maxi_1 != j):
            #max_2 = numbers[j]
            maxi_2 = j
    #ans = max_1*max_2
    return  numbers[maxi_1]*numbers[maxi_2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
    #print(input_numbers)