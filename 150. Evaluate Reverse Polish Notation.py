class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ope = ['+', '-', '*', '/']
        index = 0
        while tokens:
            for n, i in enumerate(tokens[index:]):
                if i in ope:
                    n += index
                    tokens.pop(n)
                    if i == '+':
                        tmp = int(tokens.pop(n-1)) + int(tokens.pop(n-2))
                    if i == '-':
                        tmp = int(tokens.pop(n-2)) - int(tokens.pop(n-2))
                    if i == '*':
                        tmp = int(tokens.pop(n-1)) * int(tokens.pop(n-2))
                    if i == '/':
                        tmp = float(tokens.pop(n-2)) / int(tokens.pop(n-2))
                    tokens.insert(n-2, tmp)
                    index = n - 2
                    #print(tokens)
                    break
            else:
                break
        return int(tokens.pop())