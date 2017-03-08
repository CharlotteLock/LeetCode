class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        for i in range(n):
            if i == 0:
                result = '1'
                continue
            new_result = ''
            for n, j in enumerate(result):
                if n == 0:
                    count = 1
                    continue
                if j == result[n-1]:
                    count += 1
                else:
                    new_result += str(count) + str(result[n-1])
                    count = 1
            result = new_result + str(count) + str(result[-1])
        return result