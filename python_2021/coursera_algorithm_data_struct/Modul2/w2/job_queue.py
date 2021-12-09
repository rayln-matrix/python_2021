# python3

from collections import namedtuple
#import pandas as pd

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

'''
def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    #result = []
    #next_free_time = [0] * n_workers
    #for job in jobs:
    #    next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #    result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #    next_free_time[next_worker] += job

    #return result
    
    # [[0,1],[1,1]...[n,1]] ---> initail working que
    # 
    result = []
    n_jobs = len(jobs)
  
    if n_workers >= n_jobs:
        for i in range(n_jobs):
            result.append(AssignedJob(i, 0))
        return result
    #else:        
    #    for i in range(n_workers):
    #        result.append(AssignedJob(i, 0))
    z = 0
    while jobs[z] == 0 and z<=n_jobs:
        result.append(AssignedJob(0, 0))
        z+=1
    ## Setting initial queu:
    pro = [0]
    if z!=0:
        for i in range(n_workers):
            pro.append([i,jobs[z+i]])
    else:
        for i in range(n_workers):
            result.append(AssignedJob(i, 0))
        for i in range(n_workers):
            pro.append([i,jobs[i]])
    
    #print(pro)
    def parent(i):
        return i//2
    
    def get_lch(i):
        return 2*i #+ 1
   
    def get_rch(i):
        return 2*i + 1#+ 2
    
    #def get_prio(lst):
    #    return lst[0] + lst[1]
    
    def siftdown(i):
        min_idx = i
        rch = get_rch(i)
        lch = get_lch(i)
        if lch <= len(pro)-1 and pro[lch][1]<=pro[min_idx][1]:#get_prio(pro[lch]) <= get_prio(pro[min_idx]):
            #if get_prio(pro[lch]) == get_prio(pro[min_idx]):
            if pro[lch][1] == pro[min_idx][1]:
                #if pro[lch][1]== 0:
                #    min_idx = min_idx
                if pro[lch][0] < pro[min_idx][0]:
                    min_idx = lch
                #else:
                #    min_idx = min_idx
            else:
                min_idx = lch
        if rch <= len(pro)-1 and pro[rch][1]<=pro[min_idx][1]:#get_prio(pro[rch]) <= get_prio(pro[min_idx]):
            #if get_prio(pro[rch]) == get_prio(pro[min_idx]):
            if pro[rch][1] == pro[min_idx][1]:
                #if pro[rch][1] ==0:
                #    min_idx = min_idx
                if pro[rch][0] < pro[min_idx][0]:
                    min_idx = rch
                #else:
                #    min_idx = min_idx    
            else:
                min_idx = rch
        if min_idx != i:
            pro[i],pro[min_idx] = pro[min_idx],pro[i]
            siftdown(min_idx)
            
    def insert(p):
        if len(pro)-1 == n_workers:
            return 0
        pro.append(p)
        siftup(len(pro)-1)
    
    def siftup(i):
        
        while i > 1  and pro[i][1]<=pro[parent(i)][1]:#get_prio(pro[i]) <= get_prio(pro[parent(i)]):get_prio(pro[i]) <= get_prio(pro[parent(i)]):#pro[i][1]<=pro[parent(i)][1]:#get_prio(pro[i]) <= get_prio(pro[parent(i)]):
            #print('test')
            if pro[i][1] == pro[parent(i)][1]:
                #if pro[i][1]==0:
                #    break
                if pro[i][0] < pro[parent(i)][0]:
                    pro[i],pro[parent(i)] =  pro[parent(i)], pro[i]
                    i  = parent(i)
                else:
                    break
            
            else:
                pro[i],pro[parent(i)] =  pro[parent(i)], pro[i]
                i  = parent(i)
            #pro[i],pro[parent(i)] =  pro[parent(i)], pro[i]
            #i  = parent(i)
            
    def get_top():
        #print("get top")
        #print(pro)
        result = pro[1]
        pro[1] = pro.pop()
        #print(pro)
        siftdown(1)
        return result
    #print(get_top())
    #insert([0,4])
    #print(pro)
    #print(n_workers)
    for i in range(n_workers//2,0,-1):
        siftdown(i)
    
    #print(pro)
    if z==0:
        for i in range(n_workers,len(jobs)):#n_workers,len(jobs)):
            #print('Process schedule:')
            #print(pro)
            work = get_top()
            result.append(AssignedJob(work[0], work[1]))        
            #print('Schedule Lenght:')
            #print(len(pro))
            #print('Current free:')
            #print(work[0],work[1])
            #print('Next job:')
            #print([work[0],work[1]+jobs[i]])
            insert([work[0],work[1]+jobs[i]])
            #print("")
            #print("")
            #print(pro)
            #print(jobs[i])
    else:
        for i in range(z,len(jobs)):#n_workers,len(jobs)):
            #print('Process schedule:')
            #print(pro)
            work = get_top()
            result.append(AssignedJob(work[0], work[1]))        
            #print('Schedule Lenght:')
            #print(len(pro))
            #print('Current free:')
            #print(work[0],work[1])
            #print('Next job:')
            #print([work[0],work[1]+jobs[i]])
            insert([work[0],work[1]+jobs[i]])
            #print("")
            #print("")
            #print(pro)
            #print(jobs[i])        
        
    #print(pro)
    return result    
'''


def assign_jobs(n_workers,jobs):
    # que: top--current free with the lowest index
    # siftup: move up the lowest free time workers(for parent lch rch), 
    #         if all free time is equal then move up lowest index
    # siftdwon:move down the highest free time workers(for parent lch rch),
    #         if all free time is equal then move down lowest index
    # gettop: get the top, and restructure the que
    # get parent/ rch /lch
    # insert: append at the last and siftup
    result = []
    proc = [0] # 0: dummy element, to find parent/rch/lch index easier
    
    def get_parent(i):
        return i//2
    
    def get_lch(i):
        return 2*i
    
    def get_rch(i):
        return 2*i + 1
    
    def siftdown(i):
        min_idx = i
        lch = get_lch(i)
        rch = get_rch(i)
        # Find min in parent and lch / rch
        if lch<=len(proc)-1 and proc[lch][1] <= proc[min_idx][1]:
            if proc[lch][1] < proc[min_idx][1]:
                min_idx = lch
            if proc[lch][1] == proc[min_idx][1] and proc[lch][0]<proc[min_idx][0]:
                min_idx = lch

        if rch<=len(proc)-1 and proc[rch][1] <= proc[min_idx][1]:
            if proc[rch][1] < proc[min_idx][1]:
                min_idx = rch
            if proc[rch][1] == proc[min_idx][1] and proc[rch][0]<proc[min_idx][0]:
                min_idx = rch

        if min_idx != i:
            proc[i], proc[min_idx] = proc[min_idx], proc[i]
            siftdown(min_idx)
    
    def siftup(i):
        while i > 1 and proc[i][1] <= proc[get_parent(i)][1]:
            if proc[i][1] == proc[get_parent(i)][1] and proc[i][0] < proc[get_parent(i)][0]:
                proc[i],proc[get_parent(i)] = proc[get_parent(i)], proc[i]
                i = get_parent(i)
            elif proc[i][1] < proc[get_parent(i)][1]:
                proc[i],proc[get_parent(i)] = proc[get_parent(i)], proc[i]
                i = get_parent(i)
            else:
                break
    
    def insert(p):
        if len(proc)-1 >= n_workers:
            return
        proc.append(p)
        last_idx = len(proc)-1
        #print("Last idx:",last_idx)
        siftup(last_idx)
        
    def get_top():
        if len(proc)<=1:
            return
        # restructure can be a problem
        if len(proc)==2:
            top = proc.pop()
            return top
        else:
            last = proc.pop()
            top = proc.pop(1)
            proc.insert(1,last)
            siftdown(1)
            return top
    
    for i in range(n_workers):
        proc.append([i,0])
        
    for i in range(len(jobs)):
        #print("Befor get top:",proc)
        worker = get_top()
        result.append(AssignedJob(worker[0], worker[1]))
        insert([worker[0],worker[1]+jobs[i]])
        #print("After insert:",proc)
    
    return result
    

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)
     
    #a_dict = dict()    
    #for i in range(len(assigned_jobs)):
    #    a_dict[i] = assigned_jobs[i]
    #a_pd = pd.DataFrame(a_dict).T
    #a_pd.to_csv('test_1.txt',header=False, sep=' ', index=False )
    #print(a_pd)
    #return a_pd



if __name__ == "__main__":
    main()
#print(7//2)


    #a = main()
    #a_file = pd.read_csv('02_a.txt',sep=' ',header=None)#'C:\Users\WB\Desktop\algorithm_coursera\Modul_2\week2_priority_queues_and_disjoint_sets\02.a') 
    #print(a_file)
    #print(a)
    #print(2//2)
    #print(1//2)
    
    #w_line = 0
    #for i in range(len(a)):
        ##print(a.iloc[i])
        ##print(a_file.iloc[i])
        #if (a.iloc[i][0] != a_file.iloc[i][0]) or (a.iloc[i][1] != a_file.iloc[i][1]):
            #print()
            #print()
            #print("Wrong at: ",i)
            #print("Correct:")
            #print(a.iloc[i])
            #print("Wrong")
            #print(a_file.iloc[i])
            #w_line +=1
    #print("Wrong number: ", w_line)


'''
print("Test 1")
assigned_jobs = assign_jobs(2,[1,2,3,4,5])
for job in assigned_jobs:
    print(job.worker, job.started_at)
print()
print('#########################')
    
print("Test 2")    
assigned_jobs = assign_jobs(4,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
for job in assigned_jobs:
    print(job.worker, job.started_at)
'''