class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: # negative integer
            return False
        if x // 10 == 0: # only one digit
            return True
        x = str(x) # transform to string
        while len(x): # 
            if x[0] != x[-1]: # left != right
                return False
            if len(x) < 3: # according above, one two si true
                return True
            x = x[1:-1]
        return False
