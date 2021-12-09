# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    '''
    start from i = 1 to n:
        if n-i > max(summands):
            n=n-i
            summands.append(i)
    nb = len(summands)
    summands.insert(0,nb)        
    return summands
    k1<k2<k3....<km
    k1+k2+k3....=n
    1 + (n-1) =n
    k1 + (n-1-k1) = n-1
    1<k1<(n-1-k1)
    
    '''
    if n==1:
        return [1]
    if n==2:
        return [2]
    l = 1
    k = n-1
    temp = 0
    numb = 1
    if k <= l:
        summands.append(1)
        summands.append(n)
        return summands
    while l<k:
        numb += 1
        summands.append(l)
        #summands.append(k)
        l += 1
        temp = k
        k = k-l
    #numb += 1
    summands.append(temp)
    #summands.insert(0, numb)     
    
    return summands
   

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    
    
    #for i in range(1,16):
    ##    sol = optimal_summands(i)
    ##    print(i)
    #    print(len(sol))
    #    print(sol)
    