class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = 0
        for i in s:
            if n >= len(t):
                return False
            for m, j in enumerate(t[n:]):
                if j == i:
                    n = n + m + 1
                    break
            else:
                return False
        return True
