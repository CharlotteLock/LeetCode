class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        while True:
            for n, i in enumerate(nums[begin:]):
                if i == val:
                    nums.pop(n+begin)
                    begin += n
                    break
            else:
                return len(nums)