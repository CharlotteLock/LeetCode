class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stack = []
        newn = n
        while newn:
            stack.append(newn)
            n = newn
            newn = 0
            while n:
                newn += (n % 10) ** 2
                n = n // 10
            if newn == 1:
                return True
            if newn in stack:
                return False
        return False
