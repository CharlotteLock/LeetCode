class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for n, i in enumerate(nums):
            if i > target:
                break
            if i == target:
                if len(result) > 1:
                    result.pop()
                result.append(n)
        if len(result) == 1:
            result.append(result[0])
        if len(result) == 0:
            result = [-1, -1]
        return result