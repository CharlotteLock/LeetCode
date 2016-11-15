class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        n = 0
        while True:
            for i, e in enumerate(nums[index: len(nums) - n] ):
                if e == 0:
                    nums.pop(i+index)
                    nums.append(0)
                    index += i
                    n += 1
                    break
            else:
                break
