# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        # request = [Request(Ai,Pi)]
        # process return each packet status: was_dropped, started_at 
        ai = request.arrived_at
        pi = request.time_to_process
        tf = ai + pi # finished time for the packet
        ## If finish_time is empty, put the packet finished time in it
        #print(self.finish_time)
        if len(self.finish_time) == 0:
            self.finish_time.append(tf)
            return Response(False, ai)
        if ai >= self.finish_time[0]:
            last = self.finish_time.pop(0)
            if len(self.finish_time) == 0:
                #self.finish_time.append(last + pi)
                if ai > last:
                    self.finish_time.append(tf)
                    return Response(False,ai)
                else:
                    self.finish_time.append(last + pi)
                    return Response(False,last)
            else:
                if ai < self.finish_time[0]:
                    if len(self.finish_time) < self.size:
                        last = self.finish_time[-1]
                        self.finish_time.append(self.finish_time[-1] + pi)
                        return Response(False,last)
                    else:
                        return Response(True,-1)
            
        else:
        #     last = self.finish_time[0]
        #if ai < self.finish_time[0]:
            if len(self.finish_time) < self.size:
                last = self.finish_time[-1]
                self.finish_time.append(self.finish_time[-1] + pi)
                return Response(False,last)
            else:
                return Response(True,-1)
        '''
        last_t = self.finish_time.pop(0)
        if ai < last_t and len(self.finish_time)+1 < self.size:
            return Response(True,-1)
        else:
            self.finish_time.append(last_t + pi)
            return Response(False,last_t)
        '''
        # if ai >= f[0]: f.pop(0)
        # if ai < f[0]: 
        #    if f < size: f.append(f[-1]+pi) return response(t,f[-1])
        #    else: return response(f,-1)
        
        #if len(self.finish_time) <= self.size:
            #last_t = self.finish_time.pop(0)
            #self.finish_time = self.finish_time[1:]
            #self.finish_time.append(tf)
        #else:
        #    return Response(True,-1)
 
       
        
        
        #return self.finish_time
        #return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)



if __name__ == "__main__":
    main()
    
    

'''
#test1
buffer = Buffer(1)
re = []
print("Test 1")
print(process_requests(re,buffer))

#test2
buffer = Buffer(1)
re = [Request(0,0)]
responses = process_requests(re, buffer)
print("Test 2")
for response in responses:
    print(response.started_at if not response.was_dropped else -1)
    
#test3
buffer = Buffer(1)
re = [Request(0,1),Request(0,1)]
responses = process_requests(re, buffer)
print("Test 3")
for response in responses:
    print(response.started_at if not response.was_dropped else -1)   

#test4
buffer = Buffer(1)
re = [Request(0,1),Request(1,1)]
responses = process_requests(re, buffer)
print("Test 4")
for response in responses:
    print(response.started_at if not response.was_dropped else -1)    
    
#test5
buffer = Buffer(3)
re = [Request(0,1),Request(0,1),Request(1,2),Request(1,3)]
responses = process_requests(re, buffer)
print("Test 5")
for response in responses:
    print(response.started_at if not response.was_dropped else -1)      
    
#test6
buffer = Buffer(3)
re = [Request(0,1),Request(0,1),Request(1,2),Request(1,3),Request(1,2),Request(2,1)]
responses = process_requests(re, buffer)
print("Test 6")
for response in responses:
    print(response.started_at if not response.was_dropped else -1)       
    
    
#test = [0,1,2,3,4]
#test.pop(0)
#print(test)
#print(test[0])
    
#test7
buffer = Buffer(1)
re = [Request(1,0)]
print("Test 7")
responses = process_requests(re,buffer)
for response in responses:
    print(response.started_at if not response.was_dropped else -1) 

#test8
buffer = Buffer(1)
re = [Request(0,1),Request(2,1)]
print("Test 8")
responses = process_requests(re,buffer)
for response in responses:
    print(response.started_at if not response.was_dropped else -1) 
'''