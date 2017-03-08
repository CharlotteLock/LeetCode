class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_lst = []
        for l in findNums:
            i = nums.index(l)
            for r in nums[i:]:
                if r > l:
                    ret_lst.append(r)
                    break
            else:
                ret_lst.append(-1)
            # if i == len(nums) - 1:
            #     ret_lst.append(-1)
        return ret_lst