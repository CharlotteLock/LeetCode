class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        tmp_lst = []
        num = 1
        for n, i in enumerate(A):
            if n == 0:
                continue
            tmp_lst.append(i-A[n-1]) # structure different lst
        print(tmp_lst)
        for m, j in enumerate(tmp_lst):
            if m == 0:
                continue
            if j == tmp_lst[m-1]:
                num += 1
            else:
                if num > 1:
                    ret += (num-1 + 1)*(num-1)//2
                    num = 1
        if num > 1:
            ret += (num-1 + 1)*(num-1)//2
        return ret