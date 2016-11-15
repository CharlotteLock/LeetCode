class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, e in enumerate(s):
            if i < len(s) and e not in s[i+1:] and e not in s[:i]:
                return i
        return -1
