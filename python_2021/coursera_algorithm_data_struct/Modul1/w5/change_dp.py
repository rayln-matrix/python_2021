# Uses python3
import sys

def get_change(m):
    #write your code here
    '''
    1.creat a list to store change.
    2. caculate change from i to m and store in list 
    m = min()
    3. denominataions: 1,3,4
    ''',
    if m<5:
        change = [0,1,2,1,1]
        return change[m]
    if m>=5:
        change = [0]*(m+1)
        change[0] = 0
        change[1] = 1
        change[2] = 2
        change[3] = 1
        change[4] = 1
        #print(change)
        for i in range(5,m+1):
            one_min = change[i-1] + 1
            three_min = change[i-3] + 1
            four_min = change[i-4] + 1
            #print(i)
            #print(one_min)
            #print(three_min)
            #print(four_min)
            #print(change)
            change[i] = min(one_min, three_min, four_min)
        #print(change)
        return change[m]

if __name__ == '__main__':
    
    m = int(sys.stdin.read())
    print(get_change(m))
    
    
    '''
    
    
    #test = [0]*10
    #test[1]=1
    #print(test)
    #get_change(6)
    for i in range(1,20):
        print("Number is:", i)
        print(get_change(i))
    '''