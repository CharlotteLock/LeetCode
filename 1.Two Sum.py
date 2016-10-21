#import time 
start = time.time() 
#def twoSum(nums, target):
    lst = []
    for i, e in enumerate(nums):
        if target - e in nums:
            j = nums.index(target - e)
            if i == j:
                continue
            lst.append(i)
            lst.append(j)
            return lst
twoSum([3,2,4],6)
#end = time.time() - start 
#print(end) #

#import time
#start = time.time()
def twoSum(nums, target):
    lst = []
    for i, e in enumerate(nums):
        for j, f in enumerate(nums):
            if i == j:
                continue
            if e + f == target:
                lst.append(i)
                lst.append(j)
                return lst
twoSum([2,7,11,15],13)
#end = time.time() - start
#print(end)
