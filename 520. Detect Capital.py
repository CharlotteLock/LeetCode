class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        low = ''
        uper = ''
        head = ''
        for n, i in enumerate(word):
            if i.islower():
                if n == 0:
                    head = 'l'
                    continue
                low = 'l'
            else:
                if n == 0:
                    head = 'u'
                    continue
                uper = 'u'
        print(low)
        print(uper)
        print(head)
        if head == 'l':
            if uper == 'u':
                return False
            else:
                return True
        elif uper == '' or low == '':
            return True
        else:
            return False