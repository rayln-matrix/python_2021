# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    
    current_refuel = 0
    number_of_refuel = 0
    n = len(stops)
    #stops.insert(-1,distance)
    stops.insert(0,0)
    stops.insert(n+1,distance)
    #print(stops)
    
    
    while current_refuel <= n:
        last_refuel = current_refuel
        #print("Last refuel:", last_refuel)
        while (current_refuel<=n)and((stops[current_refuel + 1] -stops[last_refuel])<=tank):
            current_refuel += 1
            #print("Current refuel:", current_refuel)
        #print(number_of_refuel)
        if current_refuel==last_refuel:
            return -1
        if current_refuel <= n:
            number_of_refuel += 1
    return number_of_refuel
    
    
    '''if distance<tank:
        return 0
    if stops[0]>tank or (distance-stops[-1]>tank):
        return -1
    while current_refuel <= (number_of_stops-1):
        last_refuel = current_refuel
        if last_refuel ==  (number_of_stops-1):
            if distance-stops[last_refuel]>tank:
                return -1
            else:
                return number_of_refuel
        while (current_refuel<number_of_stops-1)and(stops[current_refuel + 1] -stops[last_refuel])<=tank:
            current_refuel += 1
        if current_refuel <= (len(stops)-1):
            number_of_refuel += 1
    return number_of_refuel'''


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

    # Stress test:
    #t = [1,2,3,4]
    #t.insert(-1,5)
    #t.insert(0,0)
    #print(compute_min_refills(950,400,[200,375,550,750]))
    #print(compute_min_refills(10,3,[1,2,5,9]))
    #print(compute_min_refills(200,250,[100,150]))