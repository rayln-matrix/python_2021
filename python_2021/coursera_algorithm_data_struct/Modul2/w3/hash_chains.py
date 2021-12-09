# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {i:[] for i in range(self.bucket_count)} 
        #[]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # elems[query.ind] = chain
            # for string in reversed(chain): write_chain
            chain = self.elems[query.ind]
            self.write_chain(cur for cur in reversed(chain))
            #self.write_chain(cur for cur in reversed(self.elems) if self._hash_func(cur) == query.ind)
        else:
            #try:
            #    ind = self.elems.index(query.s)
            #except ValueError:
            #    ind = -1
            #hash_v = self._hash_func(query.s)
            if query.type == 'find':
                hash_v = self._hash_func(query.s)
                chain = self.elems[hash_v]
                self.write_search_result(query.s in chain)
                #self.write_search_result(ind != -1)
            elif query.type == 'add':
                hash_v = self._hash_func(query.s)
                chain = self.elems[hash_v]
                if not query.s in chain:
                    chain.append(query.s)
                #    continue
                #else:
                #    chain.append(query.s)
                #if ind == -1:
                #    self.elems.append(query.s)
            else:
                # query.type = 'del'
                hash_v = self._hash_func(query.s)
                chain = self.elems[hash_v]
                if query.s in chain:
                    chain.remove(query.s)
                
                #if ind != -1:
                #    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()


#test_d = {i:[] for i in range(5)}
#print(test_d)
#test = [a for a in 'abcdefgh']
#print(test)
#test.remove('a')
#print(test)