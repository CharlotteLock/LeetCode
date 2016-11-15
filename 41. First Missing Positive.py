class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in range(len(nums)):
            if nums.count(i+1):
                continue
            return i+1
        return len(nums) + 1
