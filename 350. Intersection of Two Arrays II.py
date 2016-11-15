class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in nums1:
            if len(nums2) == 0:
                return stack
            elif i in nums2:
                stack.append(i)
                nums2.remove(i)
        return stack
