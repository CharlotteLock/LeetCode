class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lst = []
        for n in range(1,numRows+1): 
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
        return lst
