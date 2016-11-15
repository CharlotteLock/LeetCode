class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst = []
        for n in range(1,rowIndex+2): 
            if n == 1:
                lst.append([1])
            elif n == 2:
                lst.append([1, 1])
            else:
                sub_lst = [1]
                for k in range(1, n-1): 
                    sub_lst.append(lst[n-2][k-1] + lst[n-2][k])
                sub_lst.append(1)
                lst.append(sub_lst)
        return lst[-1]
