# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    if len(starts)==0:
        return 0
    if len(starts)==1:
        for idx in range(len(points)):
            if starts[0] <= points[idx] <= ends[0]:
                cnt[idx] += 1
        return cnt
    
    #write your code here
    left = 0
    right = len(starts)
    mid = (left + right)//2
    
    '''
    Starts -> list of starting points
    Ends -> list of ending points
    segment[i] = Starts[i] - Ends[i]
    for each points:
        starts = left + right
        ends = left + rigt
        find cnt in left (left[j]<=points)
        find cnt in right (right[i]<=points)
        cnt = left cnt + right cnt   
    '''
    for idx in range(len(points)):
        p = points[idx]
        cnt[idx] += fast_count_segments(starts[left:mid],ends[left:mid],points)[idx]
        cnt[idx] += fast_count_segments(starts[mid:right],ends[mid:right],points)[idx]
    return cnt

#def count_seg(point,starts,ends):
#    count = 0
    


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
    
    
    '''
    print("First Test: ")
    cnt1 = naive_count_segments([0,5],[7,10],[1,6,11])
    cnt2 = fast_count_segments([0,5],[7,10],[1,6,11])
    print("Naive: ", cnt1)
    print("Fast: ", cnt2)
    
    print("Second Test: ")
    cnt1 = naive_count_segments([-10],[10],[-100,100,0])
    cnt2 = fast_count_segments([-10],[10],[-100,100,0])
    print("Naive: ", cnt1)
    print("Fast: ", cnt2)
    
    print("Third Test: ")
    cnt1 = naive_count_segments([-10],[10],[-100,100,0])
    cnt2 = fast_count_segments([-10],[10],[-100,100,0])
    print("Naive: ", cnt1)
    print("Fast: ", cnt2)
    
    print("Forth Test: ")
    cnt1 = naive_count_segments([0,-3,7],[5,2,10],[1,6])
    cnt2 = fast_count_segments([0,-3,7],[5,2,10],[1,6])
    print("Naive: ", cnt1)
    print("Fast: ", cnt2)
    '''
    
    
