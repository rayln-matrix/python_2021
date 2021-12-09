# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    # segments[0]->n --> number of segments
    '''
    i=0
    j=0
    while i <= n:
        j=i 
        if i == n:
            return number_of_points + 1
        if a(i+1) <= bj:
            i+=1
        number_of_points =+ 1  
        i+=1
    '''
    
    ### Failed: input is not sorted, and output position should be considered
    '''
    i = 0  # index of next overlapping segment
    j = 0  # index of current segment
    n = segments[0]
    seg = segments[1:]
    points = []
    #number_of_points =0
    #print(n)
    #print(seg)
    #print(len(seg))
    while i<=(n-1):
        j=i
        #print(j)
        if j == (n-1):
            #number_of_points += 1
            points.append(seg[j][1])
            #points.insert(0,number_of_points)
            return points
        while  (i<(n-1)) and (seg[i+1][0] <= seg[j][1]):
            #print(seg[i+1][0])
            #print(seg[j][1])
            i+=1
        #print(i)
        #print(seg[i+1][0] <= seg[j][1])
        #print(i<(n-1))
        points.append(seg[j][1])
        #number_of_points +=1
        i+=1
        #print(i)
    #points.insert(0, number_of_points)'''
        
    # Must start from the lowest:
    # sort the input:
    i = 0  # index of next overlapping segment
    j = 0  # index of current segment
    n = segments[0]
    #print(n)
    seg = segments[1:]
    seg.sort()
    points = []
    overlap = 0
    
    while i<=(n-1):
        j=i
        overlap = seg[j][1]
        if j == (n-1): 
            overlap = seg[j][1]
            points.append(overlap)
            return points
        while  (i<(n-1)) and (seg[i+1][0] <= overlap) and (seg[i+1][0] <= seg[j][1]):
            if seg[i+1][1] <= seg[j][1]:
                overlap = seg[i+1][1] 
            i+=1

        #points.append(seg[j][1])
        points.append(overlap)
        i+=1


        
    return points

    '''for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points'''

if __name__ == '__main__':
    
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
    # * operator can be used to unpack an iterable into the arguments in the function call
    ''' 
    test = [3,[1,3],[2,5],[3,6]]
    points = optimal_points(test)
    print(len(points))
    print(*points)
    
    test = [4,[4,7],[1,3],[2,5],[5,6]]
    #test.sort()
    #print(test)
    points = optimal_points(test)
    print(len(points))
    print(*points)'''
    