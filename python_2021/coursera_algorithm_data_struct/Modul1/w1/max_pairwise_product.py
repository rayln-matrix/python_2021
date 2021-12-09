# python3
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pair_product_2(numbers):
    # Find the largest two integers:ai , aj for ai>=aj>ax, for x in range(n)
    # find the product of ai aj:
    
    #max_1_i = -1 --> in python index is not needed(embeded)
    #max_2_j = -1
    ## index is good for dealing with identical values
    ## stress test for range(0-100000) length, integer range:100000000
    ### 
    '''max_1 = 0
    max_2 = 0
    for i in range(len(numbers)):
        if numbers[i]>max_1:
            max_1 = numbers[i]
    for j in range(len(numbers)):
        if (numbers[j]>max_2) and (max_1!=numbers[j]):
            max_2 = numbers[j]
            
    return [max_1*max_2,max_1, max_2]'''
    max_1 = 0
    maxi_1 =0
    
    max_2 = 0
    maxi_2=0
    for i in range(len(numbers)):
        if numbers[i]>max_1:
            max_1 = numbers[i]
            maxi_1 = i
    for j in range(len(numbers)):
        if (numbers[j]>max_2) and (maxi_1 != maxi_2):
            max_2 = numbers[j]
            maxi_2 = j
    #ans = max_1*max_2
    return  [max_1*max_2,max_1, max_2]
    

if __name__ == '__main__':
    #input_n = int(input())
    #input_numbers = [int(x) for x in input().split()]
    #print(max_pairwise_product(input_numbers))
    #print(input_numbers)
    for i in range(2,10000):
        test_data = random.sample(range(1000000),i)
        if max_pairwise_product(test_data) == max_pair_product_2(test_data)[0]:
            print(test_data)
            print("Correct")
        else:
            print("Test Fail at:")
            print(test_data)
            print("Solution 1:", max_pairwise_product(test_data))
            print("Solution 2:", max_pair_product_2(test_data)[0])
            max1 = max(test_data)
            max2 = max([i for i in test_data if i != max1])
            print("First largest integer: ", max1)
            print("Second Largest integer: ", max2)
            print("the product: ", max1*max2)
            
            print("Max 1:", max_pair_product_2(test_data)[1])
            print("Max 2:", max_pair_product_2(test_data)[2])