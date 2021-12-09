# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


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

def fibonacci_partial_sum(m,n):
    pisano_10 = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
    pisano_10_len = len(pisano_10)
    fm_10 = pisano_10[(m%pisano_10_len)]
    
    return (fibonacci_sum(n) - fibonacci_sum(m) + fm_10)%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
    
    '''
    pisano_10 = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
    for i in range(100):
        for j in range(2,1000):
            if i <= j:
                if fibonacci_partial_sum(i,j)==fibonacci_partial_sum_naive(i,j):
                    print("Correct")
                else:
                    print("Wrong")
                    print("From - to:",i,j)
                    print("Naive solution:",fibonacci_partial_sum_naive(i,j))
                    print("Test solution:",fibonacci_partial_sum(i,j))
                    print(pisano_10[(j%len(pisano_10))-1])
                    print(pisano_10[(j%len(pisano_10))])
                    break'''