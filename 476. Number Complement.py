class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b_lst = []
        ret = 0
        if num == 0:
            return 1
        while num:
            b_lst.append(num % 2)
            num = num // 2
        for i in range(len(b_lst)):
            if b_lst[i] == 0:
                ret += 2 ** i
        return ret