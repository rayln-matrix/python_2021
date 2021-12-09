# Uses python3
def edit_distance(s, t):
    #write your code here
    '''
    s[0..i] + s[i+1]
    t[0..j] + t[j+1]
    '''
    dist = dict()
    len_s = len(s)
    len_t = len(t)
    dist[(0,0)] = 0
    #if s[0] == t[0]:
    #    dist[(1,1)]=0
    #else:
    #    dist[(1,1)]=1
    for i in range(1,len_s+1):
        dist[(i,0)] = i
    for i in range(1,len_t+1):
        dist[(0,i)] = i
    
    for i in range(1,len_s+1):
        for j in range(1, len_t+1):
            #insertion
            insrt = dist[(i-1,j)] + 1
            #deletion
            dele = dist[(i,j-1)] + 1
            #replace
            rpl = dist[(i-1,j-1)] + 1
            #match
            match = dist[(i-1,j-1)]
            #if i==j:
            if s[i-1] == t[j-1]:
                dist[(i,j)] = min(insrt,dele,match)
            else:
                dist[(i,j)] = min(insrt,dele,rpl)
            #else:
            #    dist[(i,j)] = min(insrt,dele)
                
    #for key in dist.keys():
    #    print('Key: ', key)
    #    print(dist[key])          
    return dist[(i,j)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))


'''
print(edit_distance('ab', 'ab'))
print(edit_distance('short', 'ports'))
print(edit_distance('editing', 'distance'))
'''