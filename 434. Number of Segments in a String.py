class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        flag = 0
        for i in s:
            if i != ' ':
                flag = 1
            if i == ' ' and flag == 1:
                flag = 0
                result += 1
        if flag == 1:
            result += 1
        return result