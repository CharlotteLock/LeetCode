class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length_s = len(s)
        length = 0
        if len(s) == 0:
            return 0
        while length_s: # find first not spaces from n->1
            if s[length_s - 1] != ' ':
                break
            length_s -= 1
        while length_s: # find first spaces from first no spaces->1
            if s[length_s - 1] == ' ':
                return length
            length += 1
            length_s -= 1
        return length
