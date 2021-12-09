# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    '''
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps
    '''
    # Build min -heap
    # get child,siftdown, siftup
    
    swaps = []
    def get_lch(i):
        return 2*i + 1
    def get_rch(i):
        return 2*i + 2
    def siftup(i,sw):
        min_idx = i
        rch = get_rch(i)
        lch = get_lch(i)
        #print(len(data))
        #print(rch)
        #print(lch)
        if lch <= len(data)-1:
            if data[lch] < data[min_idx]:
                min_idx = lch
        if rch <= len(data)-1:
            if data[rch] < data[min_idx]:
                min_idx = rch
        if min_idx != i:
            data[i],data[min_idx] = data[min_idx], data[i]
            sw.append((i,min_idx))
            siftup(min_idx,sw)
    for i in range(len(data)//2,-1,-1):
        #print(i)
        siftup(i,swaps)
    #print(data)
    #print(swaps)
    #
    #if len(swaps)==0:
    #    return []
    #else:
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
'''

#test = [3,4,5,6,2,1,0]
#for i in range(len(test)):
#    for j in range(i+1,len(test)):
#        if test[i] > test[j]:
#            test[j], test[i] =test[i], test[j]
#            print(test)
            
#print(5//2)
#print(7//2)
#print(3//2)

print(build_heap([5,4,3,2,1]))
print(build_heap([1,2,3,4,5]))
print(build_heap([5,1,3,4,2]))
'''