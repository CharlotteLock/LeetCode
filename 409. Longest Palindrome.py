class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = dict()
        for i in s:
            if i not in stack.keys():
                stack[i] = 1
            else:
                stack[i] += 1
        longest = 0
        tag = 1
        for j in stack.keys():
            if stack[j] % 2 == 0:
                longest += stack[j]
            elif stack[j] > 2:
                longest += stack[j] - 1
                if tag:
                    longest += 1
                    tag = 0
            elif tag:
                longest += 1
                tag = 0
        return longest
