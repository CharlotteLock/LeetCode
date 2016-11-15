class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # No.1
        #if k == 0 or len(nums) == 0:
            #pass
        #else:
            #for i in range(k):
                #tmp = nums.pop()
                #nums.insert(0, tmp)
        
        # No.2
        #length = len(nums)
        #k = k % length
        #tmp = nums[length - k:length]
        #tmp.extend(nums[:length - k])
        #nums = tmp.copy()
        
