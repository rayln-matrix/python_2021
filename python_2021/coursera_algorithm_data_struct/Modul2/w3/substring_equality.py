# python3

import sys

class Solver:
    #m1 = 10**9 + 7
    #m2 = 10**9 + 9
    #x = 100157
    
    def __init__(self, s):
        self.s = s
        self.hash1 = [0]*len(s)
        self.hash2 = [0]*len(s)

    def pre_hash(self, s):
        # string = s[a1---an]
        # hash1 = [0]*len(s), hash2 = [0]*len(s) --> to store pre-hash value for every substrings
        s_len = len(self.s)
        #hash1 = [0]*s_len
        #hash2 = [0]*s_len
        x = 100157
        m1 = 10**9 + 7
        m2 = 10**9 + 9
        for i in range(1,s_len):
            self.hash1[i] = (x*self.hash1[i-1] + ord(self.s[i])) % m1
            self.hash2[i] = (x*self.hash2[i-1] + ord(self.s[i])) % m2
        #return
        
    def ask(self, a, b, l):
        #return s[a:a+l] == s[b:b+l]
        self.pre_hash(self.s)
        x = 100157
        hash_a_m1 = self.hash1[a+l] - (x**l)*self.hash1[a]
        hash_a_m2 = self.hash2[a+l] - (x**l)*self.hash2[a]
        
        hash_b_m1 = self.hash1[b+l] - (x**l)*self.hash1[b]
        hash_b_m2 = self.hash2[b+l] - (x**l)*self.hash2[b]
        
        return hash_a_m1 == hash_b_m1 and hash_a_m2 == hash_b_m2
        #    return 

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")




#test1 = [0]*len('string')
#print(test1)
#print(7%5)