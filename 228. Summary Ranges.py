class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        left = None
        right = None
        for i in nums:
            if left is None:
                left = i
                continue
            if right is None:
                if i == left + 1:
                    right = i
                else:
                    result.append('{}'.format(left))
                    left = i
                continue
            if i == right + 1:
                right = i
                continue
            else:
                result.append('{}->{}'.format(left, right))
                left = i
                right = None
        if left is not None:
            if right is None:
                result.append('{}'.format(left))
            else:
                result.append('{}->{}'.format(left, right))
        return result