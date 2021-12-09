# Uses python3
import sys
import random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
    
    #Naive stress test
    '''while(True):
        numbers = random.sample(range(1000000),2)
        #print(numbers)
        if gcd_naive(numbers[0], numbers[1]) == gcd(numbers[0],numbers[1]):
            print("Correct")
        else:
            print("Wrong")
            print("Naive solution:",gcd_naive(numbers[0], numbers[1]))
            print("Recursive solution: ", gcd(numbers[0],numbers[1]))'''
