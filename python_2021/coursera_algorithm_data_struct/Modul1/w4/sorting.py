# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    large = l
    equ = l
    '''for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    sub_m = a[:j] # sub_m[i] <= x
    k = j-1
    for i in range(j):
        if (a[i]==x) and (a[k]!=x):
            a[i] = a[k]
            a[k] = x
            k = k-1
    k = 0
    for i in range(j):
        if a[i] != x:
            k = i
    if k == j-1:
        return [j,j]'''
    for i in range(l+1, r+1):
        if a[i] < x:
            a[i],a[large] = a[large], a[i]
            a[i],a[equ+1] = a[equ+1], a[i]
            large+=1
            equ+=1
        elif a[i] ==x:
            a[i],a[equ+1] = a[equ+1],a[i]
            equ+=1
            
    
    
    return [equ,large]
    #pass

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    m = partition3(a,l,r)
    m1 = m[1]
    m2 = m[0]
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
        
    
    '''        
    #k = random.randint(3,6)
    #print(k)  ---> 3 <= random number <= 6
        
    test = [7,3,5,6,2,9,4,10,1]
    test2 = [3,5,3,3,3,3,2,10,1,2,8]
    test3 = [2,3,9,2,2]
    #partition3(test,0,10)
    #print(partition3(test,0,8))
    #print(test)
    #print(partition2(test,0,8))
    #print(test) #---> function operate on list, not a copy
    for a  in [test,test2,test3]:
        randomized_quick_sort(a, 0, len(a) - 1)
        print(a)
    '''