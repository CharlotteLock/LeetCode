class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_three = []
        for i in nums:
            if i in first_three:
                continue
            if len(first_three) == 0:
                first_three.append(i)
            elif len(first_three) == 1:
                if i > first_three[0]:
                    first_three.insert(0, i)
                else:
                    first_three.append(i)
            elif len(first_three) == 2:
                if i > first_three[0]:
                    first_three.insert(0, i)
                elif i > first_three[1]:
                    first_three.insert(1, i)
                else:
                    first_three.append(i)
            elif len(first_three) == 3:
                if i > first_three[0]:
                    first_three.insert(0, i)
                elif i > first_three[1]:
                    first_three.insert(1, i)
                elif i > first_three[2]:
                    first_three.insert(2, i)
                else:
                    continue
                first_three.pop()
        if len(first_three) == 3:
            return first_three[2]
        else:
            return first_three[0]
            