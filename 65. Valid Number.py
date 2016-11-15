class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Determine the space
        strs = s.strip() # remove spaces
        if len(strs) == 0:
            return False
        for c in strs:
            if c == ' ':
                return False
        
        # Determine e|E
        str_left = None
        str_right = None
        if len(strs.split('e')) == 2:
            str_list = strs.split('e')# split e
        else:
            str_list = strs.split('E')# split E
        if len(str_list) == 2: # hava e|E
            str_right = str_list[-1]
            str_left = str_list[0]
            if len(str_right) and len(str_left): # incomplete
                pass
            else:
                return False
        elif len(str_list) == 1: # without e|E
            str_left = str_list[0]
        else:
            return False
            
        # Record tag
        dec_tag = 0
        dec_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        point_tag = 0
        #for right
        rnum_tag = 0
        rminus_tag = 0
        rplus_tag = 0
        if str_right is not None:
            if len(str_right) != 0:
                for n, c in enumerate(str_right):
                    if c == '.':
                        return False
                    if c == '-':
                        if n != 0:
                            return False
                        else:
                            if rminus_tag == 0 and rplus_tag == 0:
                                rminus_tag = 1
                                continue
                            return False
                    if c == '+':
                        if n != 0:
                            return False
                        else:
                            if rplus_tag == 0 and rminus_tag == 0:
                                rplus_tag = 1
                                continue
                            return False
                    if c not in dec_list:
                        return False
                    rnum_tag += 1
                if rnum_tag == 0:
                    return False
            else:
                return False
        #for left
        lnum_tag = 0
        lminus_tag = 0
        lplus_tag = 0
        for m, c in enumerate(str_left):
            if c == '.':
                if point_tag == 0: # two point
                    point_tag = 1
                    continue
                return False
            if c == '-':
                if m != 0:
                    return False
                else:
                    if lminus_tag == 0 and lplus_tag == 0: # two minus
                        lminus_tag = 1
                        continue
                    return False
            if c == '+':
                if m != 0:
                    return False
                else:
                    if lplus_tag == 0 and lminus_tag == 0:
                        lplus_tag = 1
                        continue
                    return False
            if c not in dec_list: # not 0-9
                return False
            lnum_tag += 1
        if lnum_tag == 0:
            return False
        return True
