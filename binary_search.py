
import random
import time
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l,target,low=None,high=None):
    
    if low == None:
        low = 0
    if high == None:
        high = len(l)-1
    if high < low:
        return -1
    
    mid_point = (low+high) // 2
    
    if l[mid_point] == target:
        return mid_point
    elif l[mid_point] > target:
        
        return binary_search(l, target,low,mid_point-1)
    else:
        return binary_search(l, target,mid_point+1,high)
if __name__ == "__main__":
    #l = [1,3,5,10,21]
    #target = 10 
    #print(naive_search(l,target))
    #print(binary_search(l,target))
    lenght = 10000
    sorted_list = set()
    
    while len(sorted_list) < lenght:
        sorted_list.add(random.randint(-3*lenght,3*lenght))
    
    sorted_list = sorted(list(sorted_list))
    
    start = time.time()
    
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()
    
    print("Naive search time: ",(end-start)/lenght,"seconds")
    start = time.time()
    
    
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print( "Binary search time: ",(end-start)/lenght,"seconds")