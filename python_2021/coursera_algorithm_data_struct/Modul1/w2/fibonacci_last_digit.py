# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    pr = 0
    cu = 1
    for _ in range(n-1):
        pr, cu = cu%10, (pr%10 + cu%10)%10
    return cu



if __name__ == '__main__':
    ## These are for grading system to check
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
