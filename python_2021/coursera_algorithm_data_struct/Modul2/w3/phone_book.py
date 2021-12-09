# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    #contacts = [] --> use dict to avoid index problem
    contacts = dict()
    #contacts = [0]*len(queries)
    '''
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result
    '''
    def get_hash(a,b,x):
        # return (a*x +b) mod p 
        return (a*x + b) % 10007#1299827
    a = 3 # random choice
    b = 7 # random choice
    
    for cur_query in queries:
        
        # if 'add' 
        # caculate the hash value, search for hash table -> in / not
        # in -> search chain: in / not -> in: replace, not: append
        # not -> add to table[hash_value]
        if cur_query.type == 'add':
            #hash_v = get_hash(a,b,cur_query.number)
            #if not hash_v in contacts.keys():#contacts[hash_v]==None:
            #if contacts[hash_v]==0:
                #contacts[hash_v]=[[cur_query.number,cur_query.name]]
            #contacts[hash_v] = cur_query.name
            contacts[cur_query.number] = cur_query.name
            '''
            else:
                for pairs in contacts[hash_v]:
                    if pairs[0] == cur_query.number:
                        pairs[1] = cur_query.name
                        break
                else:
                    contacts[hash_v].append([cur_query.number,cur_query.name])
            '''
        # if query = 'del'
        elif cur_query.type == 'del':
            if cur_query.number in contacts.keys():
                del contacts[cur_query.number]
            
            #hash_v = get_hash(a,b,cur_query.number)
            #if hash_v in contacts.keys():
                #chain = contacts[hash_v]
                #del contacts[hash_v]
                #for pair in chain:
                #    if pair[0]==cur_query.number:
                #        chain.remove(pair)
                #        break
        # if query  = search
        else:
            response = 'not found'
            #hash_v = get_hash(a,b,cur_query.number)
            #chain = conctacts[hash_v]
            if cur_query.number in contacts.keys():
                result.append(contacts[cur_query.number])
            #if hash_v in contacts.keys():
                #result.append(contacts[hash_v])                
                #chain = contacts[hash_v]
                #if len(chain) != 0:
                #    for pair in chain:
                #        if pair[0]==cur_query.number:
                #            result.append(pair[1])
                #            break
                #else:
                #    result.append(response)
            else:
                result.append(response)      
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

#test = [[1,2],[3,4],[5,6],[6,'a'],[7,'b']]
#test.remove([1,2])
##print(test)
#test2 = dict()
#for i in range(10):
#    test2[i]=i
#print(2 in test2.keys())

#test = {i:i for i in range(10)}
#print(test)
#del test[1]
#print(test)