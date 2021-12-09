# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    
    #print(right-1)
    #print(a[right-1])
    '''
    for i in range(right):
        most=a[i]
        mid = (left + right)//2
        sub1 = a[:mid+1]
        sub2 = a[mid+1:]
        if most is majority in sub1 and most is majority in sub2:
            return most
    return -1
    0  1  2  3  4  5
    02 02 02 32 24 25 -->
    
    if right = 2k ---> odd
       else --> even 
    
    mid = (left + right-1)//2
    
    for item in a:
        if item==get_majority_element(a[:mid+1], left, mid+1) or item==get_majority_element(a[mid+1:], left,right-mid-1):
            return item
    return -1
    
    #############################
    
    for i in range(right):
        most = a[i]
        j = 0
        count = 0
        #print(a[i])
        if right%2 == 0: # even, last = right -1
            while j<=(right-2): # the last round will be j=right-2
                 if (a[j]==most) and (a[j+1]==most):
                    j+=2
                    count += 2
                    continue
                 if (a[j]==most) or (a[j+1]==most):
                    j+=2
                    count += 1
                    continue
                 #else:
                 j+=2
        if right%2 != 0: # odd, last = right-3
            if a[right-1]== most:
                count += 1
            while j<=(right-3):
                 if (a[j]==most) and (a[j+1]==most):
                    j+=2
                    count += 2
                    continue
                 if (a[j]==most) or (a[j+1]==most):
                    j+=2
                    count += 1
                    continue
                 #else:
                 j+=2
        if count > (right/2):
            return most
        
    return -1
    '''
    
    '''
    numb_set = set(a)
    count_dict =dict()
    for numb in numb_set:
        count = 0
        for i in a:
            if numb==i:
                count+=1
        count_dict[numb]=count
    if max(count_dict.values()) > (right/2):
        return 1
    else:
        return -1
    '''
    

if __name__ == '__main__':
    
    
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
    
    
    '''
    
    
    s = '8 2 1 1 4 4 5 6 1' 
    #print(s.split())
    n, *a = list(map(int,s.split()))
    print(n)
    print(a)
    
    
    print(get_majority_element([2,3,9,2,2],0,5))
    print(get_majority_element([1,2,3,4],0,4))
    print(get_majority_element([1,1,1,1,2,3,4],0,7))              
    print(get_majority_element([2,1,2,2,3,3,4,2],0,8))     
    
    
    #d = {1:3,2:4,3:5}
    #print(max(d.values()))
    '''