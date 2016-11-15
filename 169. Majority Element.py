class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = dict()
        for i in nums:
            if i not in stack.keys():
                stack[i] = 1
            else:
                stack[i] += 1
        max = 0
        result = None
        for j in stack.keys():
            if stack[j] > max:
                max = stack[j]
                result = j
        return result
