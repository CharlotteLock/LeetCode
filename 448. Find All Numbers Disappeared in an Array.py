class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                result.append(i)
        return result