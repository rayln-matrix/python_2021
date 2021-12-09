# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares(n):
    # f1**2 + f2**2 + f3**2 + ... fn**2 = fn*fn+1
    pisano_10 = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
    ps_len = 60 # len(pisano_10)
    rn = n % ps_len
    rn_1 = (n+1) % ps_len
    return (pisano_10[rn]*pisano_10[rn_1])%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
    
    '''for i in range(100000):
        if  fibonacci_sum_squares_naive(i) ==  fibonacci_sum_squares(i):
            print("Correct")
        else:
            print("Wrong")
            print("Naive Solution: ",  fibonacci_sum_squares_naive(i))
            print("Test Solution: ",  fibonacci_sum_squares(i))
            break'''
