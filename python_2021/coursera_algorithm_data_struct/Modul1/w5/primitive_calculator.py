# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    operations = [0]*(n+1)
    if n<=1:
        return [n]
    if n==2:
        return [1,2]
    if n==3:
        return [1,3]
    
    if n>=4:
        operations[0] = 0
        operations[1] = 0
        operations[2] = 1
        operations[3] = 1
        for numb in range(4,n+1):
            add = operations[numb-1] + 1
            mult2 = float('inf')
            mult3 = float('inf')
            if numb%2==0:
                mult2 = operations[numb//2] + 1
            if numb%3==0:
                mult3 = operations[numb//3] + 1
            operations[numb] = min(add,mult2,mult3)
        
        while n >= 1:
            sequence.append(n)
            op2 = float('inf')
            op3 = float('inf')
            ad1 = operations[n-1]
            if n%2 == 0:
                op2 = operations[n//2]
            if n%3 == 0:
                op3 = operations[n//3]
            best = min(ad1,op2,op3)
            if best==ad1:
                n = n-1
            elif best==op2:
                n = n//2
            elif best==op3:
                n = n//3
        return reversed(sequence)
        #while n >= 1:
        #sequence.append(n)
        #if n % 3 == 0:
        #    n = n // 3
        #elif n % 2 == 0:
        #    n = n // 2
        #else:
        #    n = n - 1
        #return reversed(sequence)
        
        


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


'''


test = [0]*10
for i in range(10):
    test[i]=i
print(test)

for i in range(1,10):
    sequence = list(optimal_sequence(i))
    print("Number is:",i)
    print(len(sequence) - 1)
    print(sequence)
    
'''