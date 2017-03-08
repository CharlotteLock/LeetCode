class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for n, i in enumerate(nums):
            if i == target:
                return n
            if i > target:
                if n == 0:
                    return 0
                else:
                    return n
        return len(nums)