# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    # W is the max, W - wi is the max
    #ans = dict()
    len_w = len(w)
    ans_lst = [[0 for i in range(W+1)] for j in range(len_w+1)]
    #print(len(ans_lst))
    #print(ans_lst)
    
    for i in range(W+1):
        #ans[(0,i)]=0
        ans_lst[0][i]=0
    for j in range(len(w)+1):
        #ans[(j,0)] = 0
        ans_lst[j][0]=0
    
    for i in range(1,len(w)+1):
        for total in range(1,W+1):
            #ans[(total,i)] = ans[(total,i-1)]
            ans_lst[i][total] = ans_lst[i-1][total]
            if w[i-1] <= total:
                #val = ans[(total-w[i-1],i-1)] + w[i-1]
                val = ans_lst[i-1][total-w[i-1]] + w[i-1]
                #if ans[(total,i)] <= val:
                #    ans[(total,i)] = val
                if ans_lst[i][total] <= val:
                    ans_lst[i][total] = val
    #print(ans_lst)
    return ans_lst[len_w][W]
    
    '''
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
    '''
    
    
  
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
'''

test = [[0 for i in range(3)] for j in range(4)]
test[0][1]=1
test[1][1]=2
test[2][1]=3
#print(test)
#print(test[1])
'''

print(optimal_weight(10,[1,4,8]))
print(optimal_weight(20,[1,4,7,8,9,10]))
print(optimal_weight(10,[3,5,3,3,5]))