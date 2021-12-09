# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def p3(A):
    if len(A)< 3 :
        return 0
    if sum(A)%3 != 0 :
        return 0
    if sum(A)%3 ==0 and len(A)%3==0:
        return 1
    

    if sum(A)%3 ==0 :
        len_a = len(A)
        sum_3 = sum(A)//3
        idx = [i for i in range(len(A))]
        first = []
        #print(idx)
        for i in range(len_a):
            for j in range(0,len_a):
                for k in range(0,len_a):
                    if i != j and j != k and i != k:
                        if A[i]==sum_3:
                            first = [i]
                            break
                        if A[j]==sum_3:
                            first = [j]
                            break
                        if A[k]==sum_3:
                            first = [k]
                            break
                        if A[i]+A[j]+A[k]==sum_3:
                            first=[i,j,k]
                            break
        #print(first)
        remain = [i for i in idx if i not in first]
        #print(remain)
        '''
        if len(remain)<2:
            return 0
        if len(remain)==2:
            left = 0
            for i in remain:
                left += A[i]
            if left == 2*sum_3:
                return 1
            else:
                return 0
        '''    
        
        for i in remain:
            for j in remain:
                for k in remain:
                    if i != j and j != k and i != k:
                        if A[i]==sum_3:
                            #print("i")
                            remain.remove(i)
                            break
                        if A[j]==sum_3:
                            #print("j")
                            remain.remove(j)
                            break
                        if A[k]==sum_3:
                            #print("k")
                            remain.remove(k)
                            break
                        if A[i]+A[j]+A[k]==sum_3:
                            #print("ijk")
                            remain.remove(i)
                            remain.remove(j)
                            remain.remove(k)
                            break
        #print(remain)
        left = 0
        for r in remain:
            left += A[r]
        if left==sum_3:
            return 1
        else:
            return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(p3(A))





#test = [1,2,3,4,5]
#test.remove(1)
#print(test)
#print(p3([3,3,3,3]))
#print(p3([40]))
#print(p3([17,59,34,57,17,23,67,1,18,2,59]))
#print(p3([1,2,3,4,5,5,7,7,8,10,12,19,25]))

#print(p3([1,1,1]))
#print(sum([1,2,3,4,5]))

