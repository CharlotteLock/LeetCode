class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        toal = 0
        num = 0
        while toal <= n:
            num += 1
            toal += num
        return num-1
