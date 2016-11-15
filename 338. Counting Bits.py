class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, num+1):
            n = 0
            while i:
                if i % 2 == 1:
                    n += 1
                i = i // 2
            result.append(n)
        return result
