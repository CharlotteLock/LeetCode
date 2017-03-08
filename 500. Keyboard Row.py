class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'
        ret_lst = []
        #words_l=words.lower()
        for w in words:
            w_l = w.lower()
            for n,c in enumerate(w_l):
                if n == 0:
                    if c in first_row:
                        target = first_row
                    elif c in second_row:
                        target = second_row
                    else:
                        target = third_row
                    print(target)
                elif c not in target:
                    print(c)
                    print(target)
                    break
            else:
                ret_lst.append(w)
        return ret_lst