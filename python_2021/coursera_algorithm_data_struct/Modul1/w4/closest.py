#Uses python3
import sys
import math

def minimum_distance(x, y):
    #write your code here
    # cut points into two half: find the smallest distance in two half: d1,d2
    # find d = min(d1, d2)
    # descard points out of range d from line
    # find the smallest dr within the range, find d = min(d,dr)
    # return d
    if len(x)<=1:
        return math.inf
    if len(x)==2:
        p1=[x[0],y[0]]
        p2=[x[1],y[1]]
        #if math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)==0:
        #    return math.inf
        #else:
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    # Find d in two halves
    n = len(x)
    x_y = [[x[i],y[i]] for i in range(n)]
    x_y.sort(key=lambda x:x[0])
    x = [x[0] for x in x_y]
    y = [x[1] for x in x_y]
    
    #print(x)
    #print(y)
    mid = n//2
    ds = min(minimum_distance(x[0:mid],y[0:mid]),minimum_distance(x[mid:],y[mid:]))    
    x_line = (x[mid] + x[mid-1])/2

    
    # Find the points within range
    idx_lst = []
    for i in range(n):
        if abs(x[i]-x_line) <= ds:
            idx_lst.append(i)
    x_y = [[x[idx],y[idx]] for idx in idx_lst]
    x_y.sort(key=lambda x:x[1])
    
    #print(idx_lst)
    d_min = ds
    if len(x_y)<=8:
        for i in range(len(x_y)-1):
            for j in range(i+1,len(x_y)):
                #p1 = x_y[i]
                #p2 = x_y[j]
                #dpp = math.dist(p1,p2)
                #if math.sqrt((x_y[i][0]-x_y[j][0])**2 + (x_y[i][1]-x_y[j][1])**2) !=0:
                d_min = min(d_min, math.sqrt((x_y[i][0]-x_y[j][0])**2 + (x_y[i][1]-x_y[j][1])**2))
        #print(d_min)
        return d_min
    if len(x_y)>8:
        i = 0
        while (i<(len(x_y)-1)):
            j = i+1
            while (j<=i+7) and (j<len(x_y)):
                #if math.sqrt((x_y[i][0]-x_y[j][0])**2 + (x_y[i][1]-x_y[j][1])**2) !=0:
                d_min = min(d_min, math.sqrt((x_y[i][0]-x_y[j][0])**2 + (x_y[i][1]-x_y[j][1])**2))
                # min(d_min, math.dist(x_y[i],x_y[j]))
                j +=1
            i += 1
        #print(d_min)
        return d_min

if __name__ == '__main__':
    
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    
    '''
   

    
    x= [1,2,3,4]
    y= [4,3,2,1]
    data = [[x[i],y[i]] for i in range(len(x))]
    print(data)
    data.sort(key=lambda x: x[1])
    print(data)
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            print(i,j)
    test = [x[0] for x in data]
    print(test)
    
    
    
    test_x=[[0,3],[7,1,4,7],[4,-2,-3,-1,2,-4,1,-1,3,-4,-2]]
    test_y=[[0,4],[7,100,8,7],[4,-2,-4,3,3,0,1,-1,-1,2,4]]
    for i in range(len(test_x)):
        print(test_x[i])
        print(test_y[i])
        print(minimum_distance(test_x[i], test_y[i]))
        
    '''
