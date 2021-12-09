# python3

def hash_func(s):
    m = 263
    prime = 1000000007
    ans = 0
    for c in reversed(s):
        ans = (ans * m + ord(c)) % prime
    return ans


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    #return [i for i in range(len(text) - len(pattern) + 1) if text[i:i + len(pattern)] == pattern]
    len_p = len(pattern)
    len_t = len(text)
    result = []
    hash_p = hash_func(pattern)
    for i in range(len_t - len_p + 1):
        sub_str = text[i:i+len_p]
        hash_sub = hash_func(sub_str)
        if hash_sub == hash_p:
            check = 0
            for j in range(len(pattern)):
                if sub_str[j] == pattern[j]:
                    check+=1
            if check == len(pattern):
                result.append(i)
    # 
    #
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

