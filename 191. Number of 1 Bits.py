class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            if n % 2 == 1:
                result += 1
            n = n // 2
        return result
