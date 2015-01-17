"""
David Schonberger
Hackerrank.com
Dynamic Programming - Max contiguous & noncontiguous subarray
1/13/2015
"""

def max_subarray(l):    
    curr_sum = 0
    curr_idx = -1
    best_sum = 0
    best_start_idx = -1
    best_end_idx = -1

    all_nonpos = sum([x <= 0 for x in l])
    
    if(all_nonpos == len(l)):
        if(0 in l):
            return [0]
        else:
            return [max(l)]
        
    for i in xrange(len(l)):
        val  = curr_sum + l[i]
        if(val > 0):
            if(curr_sum == 0):
                curr_idx = i
            curr_sum = val
        else:
            curr_sum = 0
        if(curr_sum > best_sum):
            best_sum = curr_sum
            best_start_idx = curr_idx
            best_end_idx = i
            
    return l[best_start_idx : best_end_idx + 1]

def max_noncontig_subarray(l):
    all_nonpos = sum([x <= 0 for x in l])
    
    if(all_nonpos == len(l)):
        if(0 in l):
            return [0]
        else:
            return [max(l)]
    else:
        return [x for x in l if x > 0]

T = input()
for i in range(T):
    n = input()
    ar = raw_input()
    ar = ar.split(' ')
    ar = [int(x) for x in ar]
    res = max_subarray(ar)
    res2 = max_noncontig_subarray(ar)
    print sum(res), sum(res2)