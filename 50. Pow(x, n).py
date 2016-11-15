class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0 or x == 1:
            return x
        if x == -1:
            if (n % 10) % 2 == 0:
                return x * -1
            return x
        result = 1
        if n < 0:
            n *= -1
            x = 1 / x
        while n:
            result *= x
            if result < 0.000004 and result > -0.000004:
                return 0
            n -= 1
        return result
