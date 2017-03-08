class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_lst = []
        y_lst = []
        ret = 0
        if x == 0:
            x_lst.append(x)
        if y == 0:
            y_lst.append(y)
        while x:
            x_lst.append(x % 2)
            x = x // 2
        while y:
            y_lst.append(y % 2)
            y = y // 2
        min_len = min(len(x_lst), len(y_lst))
        for i in range(1, min_len + 1):
            x_tmp = x_lst[min_len - i]
            y_tmp = y_lst[min_len - i]
            if x_tmp != y_tmp:
                ret += 1
        flg = 0
        if len(x_lst) > i:
            tm_lst = x_lst
        elif len(y_lst) > i:
            tm_lst = y_lst
        else:
            flg = 1
        if flg != 1:
            for j in range(i, len(tm_lst)):
                if tm_lst[j] == 1:
                    ret += 1
        return ret