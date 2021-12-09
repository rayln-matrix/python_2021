#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)

    lcs = dict()
    #lcs[(0,0,0)] = 0
    for i in range(len_a+1):
        for j in range(len_b+1):
            for k in range(len_c+1):
                if (i == 0 or j == 0 or k == 0):
                    lcs[(i,j,k)] = 0
                elif a[i-1]==b[j-1]==c[k-1]:
                    lcs[(i,j,k)] = lcs[(i-1,j-1,k-1)] + 1
                else:
                    lcs[(i,j,k)] = max(lcs[(i-1,j,k)],lcs[i,j-1,k],lcs[i,j,k-1])

        
    return lcs[(len_a,len_b,len_c)]

    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
'''


print(lcs3([1,2,3],[2,1,3],[1,3,5]))
print(lcs3([8,3,2,1,7],[8,2,1,3,8,10,7],[6,8,3,1,4,7]))
#print(lcs3())
#print(lcs3())

'''