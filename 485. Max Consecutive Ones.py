class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        tmp = 0
        for i in nums:
            if i == 0:
                if tmp > ret:
                    ret = tmp
                tmp = 0
            else:
                tmp += 1
        return max(ret, tmp)