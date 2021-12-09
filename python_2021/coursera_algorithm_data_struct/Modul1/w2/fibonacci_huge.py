# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


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
            pisano_lst.append(pre)
            #pisano_lst.append(cu)
            
            
def get_fibonacci_huge(n,m):
    pisano_m = pisano_period(m)[0]
    pisano_list = pisano_period(m)[1]    
    rmd = n % pisano_m
    return pisano_list[rmd]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
    
    # Naive stress test:
    
    '''for j in [1,1,2,3,5,8,13,21]:#,34,55,89]:
        p_lst = pisano_period(j) 
        print(p_lst[0])
        print(p_lst[1])'''
        
    '''    
    for i in range(1,1000000):
        for j in range(2,10000):
            if get_fibonacci_huge_naive(i, j)==get_fibonacci_huge(i,j):
                print("Correct")
            else:
                print("Wrong!")
                print("Naive Solution:", get_fibonacci_huge_naive(i, j))
                print("Pisano Solution:", get_fibonacci_huge(i,j))
                break'''
