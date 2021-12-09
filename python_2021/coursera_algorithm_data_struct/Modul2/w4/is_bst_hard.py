#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree,idx, min_idx, max_idx):
    # Implement correct algorithm here
    #def inorder(idx):
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
    if len(tree) <=1:#or (tree[idx][1] == -1 and tree[idx][2] == -1) :
        return True
    if idx == -1:
        return True
    if (min_idx != -1 and tree[idx][0] < tree[min_idx][0]) or (max_idx != -1 and tree[idx][0]>=tree[max_idx][0]):
        return False
    return IsBinarySearchTree(tree, tree[idx][1], min_idx, idx) and IsBinarySearchTree(tree, tree[idx][2], idx, max_idx)
    #    return False
    #return True
    
    
    '''
    if idx == -1:
        return True
    # For left part
    #if tree[idx][1] != -1 and not IsBinarySearchTree(tree,tree[idx][1]):
    #    return False
    
    # Current part
    if tree[idx][1] != -1 and tree[idx][0] <= tree[tree[idx][1]][0] : 
        return False
    if tree[idx][2] != -1 and tree[idx][0] > tree[tree[idx][2]][0]: #tree[idx][2] != -1:
        #left = tree[tree[idx][1]][0]
        #right = tree[tree[idx][2]][0]
        return False
    #if tree[idx][2] != -1 and not IsBinarySearchTree(tree,tree[idx][2]):
    #    return False
    return IsBinarySearchTree(tree,tree[idx][1]) and IsBinarySearchTree(tree,tree[idx][2])
    '''
         
        
        
        
    #else:            
    #    order_lst = inorder(0)
    #    print(order_lst)
    #    for i in range(len(order_lst)-1):
    #        if order_lst[i] > order_lst[i+1]:
    #            return False
    #    return True
    #return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree,0,-1,-1):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()

#print(IsBinarySearchTree([[2,1,2],[1,-1,-1],[3,-1,-1]],0,-1,-1)) # T
#print(IsBinarySearchTree([[2,1,2],[2,-1,-1],[3,-1,-1]],0,-1,-1)) # F
#print(IsBinarySearchTree([[1,1,2],[2,-1,-1],[3,-1,-1]],0,-1,-1)) # F