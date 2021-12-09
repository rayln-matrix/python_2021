#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    len_a = len(a)
    len_b = len(b)
    sub = dict()
    #if a[0]==b[0]:
    #    sub[(0,0)]=1
    #else:
    sub[(0,0)]=0
    for i in range(1,len_a+1):
        sub[(i,0)] = 0
    for i in range(1,len_b+1):
        sub[(0,i)] =0
    
    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            if a[i-1]== b[j-1]:
                sub[(i,j)] = sub[(i-1,j-1)] + 1
            else:
                sub[(i,j)] = max(sub[(i,j-1)],sub[(i-1,j)],sub[(i-1,j-1)])
    '''
    ans = []
    for i in range(len_a):
          test = ans
          for j in range(len_b):
              if a[i] == b[j]:
                  ans.append(a[i])
          
    '''          
    return sub[(i,j)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
'''

print(lcs2([2,7,5],[2,5]))
print(lcs2([7],[1,2,3,4]))
print(lcs2([2,7,8,3],[5,2,8,7]))

'''