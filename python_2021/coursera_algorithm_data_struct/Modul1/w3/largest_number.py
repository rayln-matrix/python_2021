#Uses python3

import sys

def largest_number(a):
    #write your code here"
    '''
    1<=a[i]<=1000
    max:
    a[j]a[i]
    
    answer <- empty string
    max <- -1
    while input is not empty:
        for string in input:
            find max string pattern:
                find the largest single digit
                find the largest three digits string in input 
                find the largest two digits string in input
                compare largest single, two three digit to find the largest pattern
        answer + = max string pattern
        remove max string pattern    
    '''
    res = ""
    
    '''while len(a) != 0:
        for numb in a:
            digit1 = 0
            digit2 = 0
            digit3 = 0
            pattern = ""
            if len(numb)==1:
                if int(numb)>digit1:
                    digit1 = int(numb)
            if len(numb)==2:
                if int(numb)>digit2:
                    digit2 = int(numb)
            if len(numb)==3:
                if int(numb)>digit3:    
                    digit3 = int(numb)
        # single digit is the largest pattern            
        if (digit1>(digit2//10)) and (digit1>(digit3//100)):
            pattern = str(digit1)
        #  two digit is the largest pattern
        if ((digit2//10)>=digit1) and ((digit2%10)>=digit1) and ((digit2%10)> (digit3%100)):
            pattern = str(digit2)
        # three digit is the largest pattern:
        if ((digit3//100)>=digit1) and ((digit3%10)>=digit1) and ((digit2%10)> (digit3%100)):
    '''
    
    
    while len(a)!=0:
        max_numb = 0
        idx = 0
        for i in range(len(a)):
            if grtorequ(a[i],str(max_numb)):
            #if int(a[i])>=max_numb:
                max_numb = int(a[i])
                idx = i
        res += str(max_numb)
        a.pop(idx)
    
    return res

def grtorequ(a,b):
    "true if a is larger pattern, otherwhise false"
    str1 = a + b
    str2 = b + a
    #print(str1)
    #print(str2)
    if int(str1) > int(str2):
        return True
    return False




if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
    #print(largest_number(['4','5','6','8','9','1','2','2','7']))
    #print(largest_number(['4','5','6','6','6','7']))
    #print(largest_number(['54','546','548','60']))
    #print(largest_number(['1','34','3','98','9','76','45','4']))    
    #grtorequ('-1','1')
    #print(grtorequ('0','1'))

