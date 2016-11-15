class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        while num:
            if num % 2 == 0:
                num = num // 2
                continue
            if num % 3 == 0:
                num = num // 3
                continue
            if num % 5 == 0:
                num = num // 5
                continue
            if num == 1:
                return True
            else:
                return False
        return False
