# Uses python3
def calc_fib(n):
    #if (n <= 1):
    #    return n
    #return calc_fib(n - 1) + calc_fib(n - 2)
    fb_numb = dict()
    fb_numb[0] = 0
    fb_numb[1] = 1
    for i in range(2,n+1):
        fb_numb[i]=fb_numb[i-1] + fb_numb[i-2]
        #print(i)
    return fb_numb[n]    
    
n = int(input())
print(calc_fib(n))
