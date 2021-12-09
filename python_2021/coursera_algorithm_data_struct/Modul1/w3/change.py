# Uses python3
import sys

def get_change(m):
    #write your code here
    #1,5,10
    k1 = m//10
    r1 = m%10
    k2 = r1//5
    r2 = r1%5 
        
    return k1+k2+r2

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    
    
    #for i in range(30):
    #    print(get_change(i))
