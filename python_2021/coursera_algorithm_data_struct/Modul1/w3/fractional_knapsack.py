# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    w_v_lst = []
    w_v_dict = dict()
    for i in range(len(weights)):
        w_v_lst.append(values[i]/weights[i])
        w_v_dict[values[i]/weights[i]]=weights[i]
    w_v_lst.sort(reverse=True)
    for i in range(len(w_v_lst)):
        if capacity == 0:
            return value
        wv = w_v_lst[i]
        w = w_v_dict[wv]
        a = min(w,capacity)
        value = value + a*wv
        capacity = capacity - a
        w_v_dict[wv] = w -a
        

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
