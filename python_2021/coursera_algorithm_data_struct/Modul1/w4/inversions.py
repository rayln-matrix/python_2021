# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right-1) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave+1)#-left+1)
    number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
    number_of_inversions += merge_count(a,b,left,right, ave)
    
    return number_of_inversions
    '''for ai in a[left:ave]:
        for aj in a[ave:right]:
            if ai>aj:
                number_of_inversions = ave - ai+1
    return number_of_inversions
    
    
    func (a,b,left,right):
        numb = 0
        if right - left <=1:
            return number_of_inversion
    1. based case
    if rigt-left == 2:
        if a[right] < a[left]:
            number_of_inversion += 1
    2. merge:
        number_of_inversion += left
        number_of_inversion += right
        count number_of_inversion between left and right:
            for a in left:
                for b in right:
                    if a>b:
                        number_of_inerstion += 1
    '''
    
    #write your code here

def merge_count(a,b,left,right, mid):
    
    l = left
    r = mid +1
    k = left
    count = 0
    
    while (l<=mid) and (r<right):
        if a[l] <= a[r]:
            b[k]=a[l]
            l+=1
            k+=1
        else:
            count += (mid-l+1)
            b[k] = a[r]
            r+=1
            k+=1
    while l<=mid:
        b[k]=a[l]
        k+=1
        l+=1
    while r<right:
        b[k]=a[r]
        k+=1
        r+=1
    for i in range(left,right):
        a[i]=b[i]
    
    return count


def naive_get(a):
    numb = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i] > a[j]) and (i<j):
                numb += 1
    return numb
      
            
            
            
if __name__ == '__main__':
    
    
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
    
    '''
    
    #print(1//2)
    
    
    
    for a in [[2,3,9,2,9],[1,4,5,2,3,8,6],[2,3,1,4,7,5],[9,8,7,3,2,1]]:
        b = len(a)*[0]
        print(get_number_of_inversions(a, b, 0, len(a)))
        #print(naive_get(a))
    
    '''
    