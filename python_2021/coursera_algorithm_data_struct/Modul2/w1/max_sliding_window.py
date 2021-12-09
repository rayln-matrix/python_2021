# python3


def max_sliding_window_naive(sequence, m):
    #maximums = []
    #for i in range(len(sequence) - m + 1):
    #    maximums.append(max(sequence[i:i + m]))
    #return maximums
    que = []
    #max_lst = [-1]
    #que.append(sequence[0])
    ans = []
    #ans.append(que[-1])
    n = len(sequence)
    #print(que)
    
    for i in range(m):
        while len(que)>0 and sequence[i]>=sequence[que[-1]]:
            que.pop(-1)
        que.append(i)
    ans.append(sequence[que[0]])
    for i in range(m,n):
        while len(que)>0 and sequence[i]>=sequence[que[-1]]:
            que.pop(-1)
        que.append(i)
        while i-que[0] >= m:
            que.pop(0)
        ans.append(sequence[que[0]])
    
    return ans
    '''
    ## Second
    for i in range(m):
        que.append(sequence[i])
    ans.append(max(que))
    for i in range(m,n):
        que.pop(0)
        que.append(sequence[i])
        ans.append(max(que))
    return ans

        #if sequence[i]>=max_lst[-1]
    ## First
    for i in range(0,n-m+1):
        count = 0
        que.append(sequence[i])
        #print(i)
        #print(que)
        while count <= m-1:
            #print(count)
            #print(sequence[i + count])
            if sequence[i + count] > que[0]:
                que.append(sequence[i + count])
                que.pop(0)
            count += 1
        #print(que)
        ans.append(que[0])
        que.pop(0)
    return ans
    '''


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))



#print(max_sliding_window_naive([2,7,3,1,5,2,6,2],4))