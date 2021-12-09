# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.result = []
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
   
    #def get_parent(self, key):
        # a node only has a parent: it is in left or right. 
        # if not in both left and right then it is root
        #if key in self.left:
        #    return self.left.index(key)
        #elif key in self.right:
        #    return self.right.index(key)
        #else:
        #    return 0
        
    #def get_sibl(self,key):
        # find parent index-> find sibl, no sibl return -1 
        # if root then return 0
        #if key in self.left:
        #    parent = self.get_parent(key)
        #    return self.right[parent]
        #elif key in self.right:
        #    parent = self.get_parent(key)
        #    return self.left[parent]
        #else:
        #    return 0        
    
    #def get_smallest(self):
        # get the left most = smallest
        #idx = 0
        #while self.left[idx] != -1:
        #    idx = self.left[idx]
        #return idx
    
    def l_m_r(self,idx):
        # if no left and no right-> return [key[idx]]
        '''
        if self.left[idx] == -1 and self.right[idx] == -1 :
            return [self.key[idx]]
        else:
        # with left but no right / no left but with right    
            if self.left[idx] != -1 and self.right[idx] ==-1:
                left_key = self.l_m_r(self.left[idx])
                this_key = [self.key[idx]]
                return left_key + this_key
            elif self.left[idx] == -1 and self.right[idx] !=-1:
                right_key = self.l_m_r(self.right[idx])
                this_key = [self.key[idx]]
                return this_key + right_key
            else:
                left_key = self.l_m_r(self.left[idx])
                right_key = self.l_m_r(self.right[idx])
                this_key = [self.key[idx]]
                return left_key + this_key + right_key
        ''' 
        left_part = []
        right_part = []
        
        if self.left[idx] != -1:
            left_part = self.l_m_r(self.left[idx])
        this_key = [self.key[idx]]
        if self.right[idx] != -1:
            right_part = self.l_m_r(self.right[idx])
        return left_part + this_key + right_part
            
    
    def m_l_r(self,idx):
        # if no left and no right -> return [key[idx]]
        '''
        if self.left[idx] == -1 and self.right[idx] == -1 :
            return [self.key[idx]]
        else:
            if self.left[idx] != -1  and self.right[idx]== -1:
                left_key = self.m_l_r(self.left[idx])
                this_key = [self.key[idx]]
                return this_key + left_key
            elif self.left[idx] == -1  and self.right[idx] !=-1:
                right_key = self.m_l_r(self.right[idx])
                this_key = [self.key[idx]]
                return this_key + right_key
            else:
                left_key = self.m_l_r(self.left[idx])
                right_key = self.m_l_r(self.right[idx])
                this_key = [self.key[idx]]
                return this_key + left_key  + right_key
        '''
        left_part = []
        right_part = []
        if self.left[idx] != -1:
            left_part = self.m_l_r(self.left[idx])
        this_key = [self.key[idx]]
        if self.right[idx] != -1:
            right_part = self.m_l_r(self.right[idx])
        return this_key + left_part + right_part
        

    
    def l_r_m(self,idx):
        '''
        if self.left[idx] == -1 and self.right[idx] == -1 :
            return [self.key[idx]]
        else:
            if self.left[idx] != -1  and self.right[idx]== -1:
                left_key = self.l_r_m(self.left[idx])
                this_key = [self.key[idx]]
                return left_key + this_key
            elif self.left[idx] == -1  and self.right[idx] !=-1:
                right_key = self.l_r_m(self.right[idx])
                this_key = [self.key[idx]]
                return right_key + this_key
            else:
                left_key = self.l_r_m(self.left[idx])
                right_key = self.l_r_m(self.right[idx])
                this_key = [self.key[idx]]
                return left_key  + right_key + this_key
        '''
        left_part = []
        right_part = []
        if self.left[idx] != -1:
            left_part = self.l_r_m(self.left[idx])
        this_key = [self.key[idx]]
        if self.right[idx] != -1:
            right_part = self.l_r_m(self.right[idx])
        return left_part + right_part + this_key
        
            

    def inOrder(self,idx):
        #self.result = self.l_m_r(0)
        #self.result = []
        #result = []
        #idx = 0
    # Finish the implementation
        #if self.left[idx] != -1:
        #    result = self.inOrder(self.left[idx])
        #result.append(self.key[idx])
        #if self.right[idx] != -1:
        #    result = result + self.inOrder(self.right[idx])
        #return result
        #self.result = []
        if self.left[idx] != -1:
            self.inOrder(self.left[idx])
        self.result.append(self.key[idx])
        if self.right[idx] != -1:
            self.inOrder(self.right[idx])
        return self.result
         
        
            
    # You may need to add a new recursive method to do that
    #    if self.left[0]==-1 and self.right[0]==-1:
    #        self.result.append(self.key[0])
        #return self.result

    def preOrder(self,idx):
        #self.result = self.m_l_r(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that                
        #eturn self.result
        #self.result = []
        self.result.append(self.key[idx])
        if self.left[idx] != -1:
            #result = result + self.preOrder(self.left[idx])
            self.preOrder(self.left[idx])
        if self.right[idx] != -1:
            #result = result + self.preOrder(self.right[idx])
            self.preOrder(self.right[idx])
        return self.result
        

    def postOrder(self,idx):
        #self.result = self.l_r_m(0)
    # Finish the implementation
    # You may need to add a new recursive method to do that                
        #return self.result
        #self.result = []
        if self.left[idx] != -1:
            #result = result + self.postOrder(self.left[idx])
            self.postOrder(self.left[idx])
        if self.right[idx] != -1:
            #result = result + self.postOrder(self.right[idx])
            self.postOrder(self.right[idx])
        self.result.append(self.key[idx])    
        return self.result
        
    def reset_result(self):
        self.result = []
        return 


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder(0)))
    tree.reset_result()
    print(" ".join(str(x) for x in tree.preOrder(0)))
    tree.reset_result()
    print(" ".join(str(x) for x in tree.postOrder(0)))

threading.Thread(target=main).start()

#t = [1,2,3,4]
#try: print(t.index(5))
#except ValueError: 
#    print("Not in the list")
    
#print([1,2]+ [3,4] +[[]])  
