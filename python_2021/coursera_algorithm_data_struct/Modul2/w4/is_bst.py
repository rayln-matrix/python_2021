#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    '''
    if len(tree) == 0:
        return True
    
    def isbst(idx):
        if tree[idx][1]==-1 and tree[idx][2]==-1:
            return True
        if tree[idx][1] != -1:
            left_idx = tree[idx][1]
            if not isbst(left_idx):
                return False
            elif tree[idx][0] <= tree[left_idx][0]:
                return False
        if tree[idx][2] != -1:
            right_idx = tree[idx][2]
            if not isbst(right_idx):
                return False
            elif tree[idx][0] >= tree[right_idx][0]:
                return False
        return True
    
    return isbst(0)
        
    #else:
    #    if tree[idx][1]==-1 and tree[idx][2]==-1:
    #        return True
    #    if tree[idx][1] != -1 and IsBinarySearch:
            
        
    '''
    order_lst = []
    def inorder(idx):
        #this_key = tree[idx][0]
        #left_idx = tree[idx][1]
        #right_idx = tree[idx][2]
        #if left_idx == -1 and right_idx == -1:
        #    return [this_key]
        #elif left_idx != -1 and right_idx == -1:
        #    left_part = inorder(left_idx)
        #    return left_part + [this_key]
        #elif left_idx == -1 and right_idx != -1:
        #    right_part = inorder(right_idx)
        #    return [this_key] + right_part
        #else:
        #    left_part =  inorder(left_idx)
        #    right_part = inorder(right_idx)
        #    return left_part + [this_key] + right_part
        #left_part = []
        #right_part = []
        #left_idx = tree[idx][1]
        #right_idx = tree[idx][2]
        #if left_idx != -1:
        #    left_part = inorder(left_idx)
        #this_key = tree[idx][0]
        #if right_idx != -1:
        #    right_part = inorder(right_idx)
        #return left_part + [this_key] +right_part
        if tree[idx][1] != -1:
            inorder(tree[idx][1])
        order_lst.append(tree[idx][0])
        if tree[idx][2] != -1:
            inorder(tree[idx][2])
        return
        
        
    if len(tree)==0:
        return True
    else:            
        inorder(0)
        #print(order_lst)
        for i in range(len(order_lst)-1):
            #print(i)
            #print(order_lst[i])
            if order_lst[i] >= order_lst[i+1]:
                return False
        return True
    


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()


#print(IsBinarySearchTree([[4,1,-1],[2,2,3],[1,-1, -1],[5, -1, -1]]))

#if not (not True):
#    print(False)
#print(-True)