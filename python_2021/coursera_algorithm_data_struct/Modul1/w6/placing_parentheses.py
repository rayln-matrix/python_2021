# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    digit_lst = [i for i in range(len(dataset)) if i%2 ==0]
    op_lst = [j for j in range(len(dataset)) if j%2 != 0]
    #print(digit_lst)
    #print(op_lst)
    digit = [int(dataset[i]) for i in digit_lst]
    op = [dataset[i] for i in op_lst]
    #print(digit)
    #print(op)
    max_lst = [[0 for i in range(len(digit))] for j in range(len(digit))]
    min_lst = [[0 for i in range(len(digit))] for j in range(len(digit))]
    
    for i in range(len(digit)):
        max_lst[i][i] = digit[i]
        min_lst[i][i] = digit[i]
    
    #print(max_lst[0])
    #print(min_lst)
    #print(max_lst[0])
    for s in range(1,len(digit)):
        for i in range(1,len(digit)-s+1):
            j = i+s
            min_v = float('inf')
            max_v = -float('inf')
            for k in range(i-1,j-1):
                #print(max_lst[i-1][k])
                #print(min_lst[i-1][k])
                a = evalt(max_lst[i-1][k],max_lst[k+1][j-1],op[k])
                b = evalt(max_lst[i-1][k],min_lst[k+1][j-1],op[k])
                c = evalt(min_lst[i-1][k],max_lst[k+1][j-1],op[k])
                d = evalt(min_lst[i-1][k],min_lst[k+1][j-1],op[k])
                min_v = min(min_v,a,b,c,d)
                max_v = max(max_v,a,b,c,d)
            max_lst[i-1][j-1] = max_v
            min_lst[i-1][j-1] = min_v
            #max_lst[i-1][j-1] = maxvalue(digit[i-1:j],op_lst[i-1:j],max_lst,min_lst)[1]
            #min_lst[i-1][j-1] = maxvalue(digit[i-1:j],op_lst[i-1:j],max_lst,min_lst)[0]
    
    #print(max_lst)
    #print(min_lst)
    return max_lst[0][len(digit)-1]



if __name__ == "__main__":
    print(get_maximum_value(input()))


#print(get_maximum_value('5-8+7*4-8+9'))


'''
n = 6
for s in range(1,n-1):
    for i in range(1,n-s):
        j= s+i
        print("s :",s)
        print("i :",i)
        print("j :",j)
        print((i,j))
'''