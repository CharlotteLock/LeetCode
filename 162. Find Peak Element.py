class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n, i in enumerate(nums):
            if n == 0:
                if len(nums) == 1:
                    return n
                if i > nums[n+1]:
                    return n
                continue
            if n == len(nums) - 1:
                if i > nums[n-1]:
                    return n
                continue
            if i > nums[n-1] and i > nums[n+1]:
                return n