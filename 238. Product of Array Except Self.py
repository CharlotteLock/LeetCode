class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_index = []
        ret_lst = []
        sum = 1
        
        for n,i in enumerate(nums):
            if i == 0:
                zero_index.append(n)
            else:
                sum *= i
        for m,j in enumerate(nums):
            if (m in zero_index and len(zero_index) > 1) or (m not in zero_index and len(zero_index) > 0):
                ret_lst.append(0)
            else:
                if j == 0:
                    ret_lst.append(sum)
                else:
                    ret_lst.append(sum // j)
        return ret_lst
        