# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    mid =  (left + right)//2 
    found = -1
    
    # write your code here
    while (left < right):
        if a[mid] == x:
            found = mid
            return found
        if x < a[mid] :
            right = mid
            mid = (left + right)//2 

        elif x > a[mid]:
            left = mid+1
            mid = (left + right)//2 

    return found
    
    

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
    
    '''
    #print(binary_search([1,5,8,12,13],11))
    for i in [8,1,23,1,11]:   
        bs = binary_search([1,5,8,12,13],i)
        ls = linear_search([1,5,8,12,13],i)
        if bs != ls:
            print("x=",i)
            print("bs=",bs)
            print("ls=",ls)
            
    #for i in [5,1,2,3,4,5]:   
    #    bs = binary_search([1,2,3,4,5],i)
    ##    ls = linear_search([1,2,3,4,5],i)
    #    if bs != ls:
    #        print("x=",i)
    #        print("bs=",bs)
    #        print("ls=",ls)
    
    '''