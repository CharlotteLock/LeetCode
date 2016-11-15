class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        while True:
            while num:
                sum += num % 10
                num = num // 10
            if sum // 10 == 0:
                return sum
            else:
                num = sum
                sum = 0
