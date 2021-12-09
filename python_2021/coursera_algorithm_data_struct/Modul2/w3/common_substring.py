# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def pre_hash(s,table1,table2):
    m1 = 10**9 + 7
    m2 = 10**9 + 9
    x = 31
    for i in range(1,len(s)):
        table1[i] = (x*table1[i-1] + ord(s[i])) % m1
        table2[i] = (x*table2[i-1] + ord(s[i])) % m2
        
def get_hash(table,i,l):
    # get hash of the substring
    x = 31
    return table[i+l] - (x**l)*table[i]    



def solve(s, t):
    
    # Length and prime
    s_len = len(s)
    t_len = len(t)
    small = min(s_len, t_len)
    x = 31
    if s_len >= t_len:
        short = t
        # hash table for short
        hash_short_1 = [0]*t_len
        hash_short_2 = [0]*t_len
        pre_hash(t,hash_short_1, hash_short_2)
        # hash table for long
        long = s
        hash_long_1 = [0]*s_len
        hash_long_2 = [0]*s_len
        pre_hash(s,hash_long_1, hash_long_2)
    else:
        short = s
        # hash table for short
        hash_short_1 = [0]*s_len
        hash_short_2 = [0]*s_len
        pre_hash(s,hash_short_1, hash_short_2)
        # hash table for long
        long = t
        hash_long_1 = [0]*t_len
        hash_long_2 = [0]*t_len
        pre_hash(t,hash_long_1, hash_long_2)
    
    
    # hash table for s
    #hashs_1 = [0]*s_len
    #hashs_2 = [0]*s_len
    #pre_hash(s,hashs_1, hashs_2)
    
    # hash table for t
    #hasht_1 = [0]*t_len
    #hasht_2 = [0]*t_len
    #pre_hash(s,hasht_1, hasht_2)
    
    # Check substring from min(len(s),len(t)) = min_len
    # for min_len to 0: find if there are substring 
    # i -- len(s)-l
    for l in range(small,0,-1):
        i = 0
        while i<= len(short)-l:
            #s1 = short substring hash 1
            #l1 = long substring hash 1
            s1 = get_hash(hash_short_1,i,l)
            s2 = get_hash(hash_short_2,i,l)
            for j in range(len(long-l)):
                l1 = get_hash(hash_long_1,j,l)
                l2 = get_hash(hash_long_2,j,l)
                if s1==l1 and s2==l2:
                    ans = Answer(i,j,l)
                    return ans
            i+=1
    ans = Answer(0,0,0)
    return ans
            
        
        
    '''ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
                ans = Answer(i, j, l)
                    
    '''          
    #return ans

for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
