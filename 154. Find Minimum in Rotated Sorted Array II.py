class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n, i in enumerate(nums):
            if n == 0:
                min = i
            else:
                if i < min:
                    min = i
        return min