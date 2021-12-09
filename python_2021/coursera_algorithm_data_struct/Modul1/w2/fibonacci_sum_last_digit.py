# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

'''
def pisano_period(m):
    ## find pisano period : int
    ## find pisano period series: list
    pre, cu = 0,1
    pisano_lst = [0]
    if m < 2:
        return [1,0]
    for i in range(m*m):
        pre, cu = cu, (pre + cu)%m
        #print("m is:",i)
        #print("pre is:", pre)
        #print("cu is:",cu)
        if (pre==0) and (cu==1):
            return [i+1,pisano_lst]
        else:
            pisano_lst.append(pre)'''


def fibonacci_sum(n):
    pisano_10 = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
    pisano_10_len = len(pisano_10)
    pisano_10_sum = sum(pisano_10)
    #print(pisano_10_len)
    #print(pisano_10_sum)
    if n >= pisano_10_len:
        numb_of_10 = n//pisano_10_len
        remainder = n%pisano_10_len
        return (sum(pisano_10[:remainder+1]) + numb_of_10*pisano_10_sum)%10
    else:
        remainder = n%pisano_10_len
        return (sum(pisano_10[:remainder+1]))%10
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
    
    ## Get pisano period for 10:
    #print(pisano_period(10)[0]) ---> 60
    #print(pisano_period(10)[1]) --->  [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1] 

    # Checking pisano sum:
    #fibonacci_sum(0)--> correct
    
    ## Naive stress test:
    '''for i in range(100000):
        if fibonacci_sum_naive(i)==fibonacci_sum(i):
            print("Correct")
        else:
            print("Wrong")
            print("N is:", i )
            print("Naive Solution: ",fibonacci_sum_naive(i))
            print("Pisano_10 Solition: ",fibonacci_sum(i))
            break'''
            
            
            