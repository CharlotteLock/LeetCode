class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j= 0
        while True:
            for i, e in enumerate(nums[j :]):
                if (i + j + 1) < len(nums):
                    if nums[i+j+1] == e:
                        nums.pop(j+i)
                        j = j + i
                        break
            else:
                break
        return len(nums)
