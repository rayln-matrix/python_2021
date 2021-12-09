#python3
import sys

class StackWithMax():
    # Find max with O(1):
    
    
    
    def __init__(self):
        self.__stack = []
        #self.max_idx = 0
        self.max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__stack)==1:
            #self.max_idx = 0
            self.max_stack.append(a)
        else:
            #if a > self.__stack[self.max_idx]:
            #    self.max_idx = len(self.__stack) - 1
            #    self.max_stack.append(a)
            if a >= self.max_stack[-1]:
                self.max_stack.append(a)
        #return self.__stack

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[-1] == self.max_stack[-1]: #and self.max_idx == len(self.__stack)-1:
            self.max_stack.pop()
            self.__stack.pop()
        else:
            self.__stack.pop()
        #return self.__stack

    def Max(self):
        assert(len(self.__stack))
        return self.max_stack[-1]



if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
'''

#Test 1:
print("Test 1")
stack = StackWithMax()
stack.Push(2)
stack.Push(1)
print(stack.Max())
stack.Pop()
print(stack.Max())

#Test 2:
print("Test 2")
stack = StackWithMax()
stack.Push(1)
stack.Push(2)
print(stack.Max())
stack.Pop()
print(stack.Max())

#Test 3:
print("Test 3")
stack = StackWithMax()
stack.Push(2)
stack.Push(3)
stack.Push(9)
stack.Push(7)
stack.Push(2)
print(stack.Max())
print(stack.Max())
print(stack.Max())
stack.Pop()
print(stack.Max())

#Test 4:
print("Test 4")
stack = StackWithMax()
stack.Push(1)
stack.Push(7)
stack.Pop()

#Test 5:
print("Test 5")
stack = StackWithMax()
stack.Push(7)
stack.Push(1)
stack.Push(7)
print(stack.Max())
stack.Pop()
print(stack.Max())

#Test 6:
print("Test 6")
stack = StackWithMax()
stack.Push(0)
print(stack.Max())
stack.Push(1)
print(stack.Max())
stack.Push(2)
print(stack.Max())
stack.Push(3)
print(stack.Max())
stack.Push(4)
print(stack.Max())
stack.Push(5)
print(stack.Max())
stack.Push(6)
print(stack.Max())
stack.Push(7)
print(stack.Max())
stack.Push(8)
print(stack.Max())
stack.Push(9)
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())
stack.Pop()
print(stack.Max())

'''