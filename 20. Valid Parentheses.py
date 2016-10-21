def isValid(s):
    brackets = (
        ('(', ')'), 
        ('[', ']'), 
        ('{', '}')
    )
    stack = []
    for c in s:
        if c in (t[0] for t in brackets):
            stack.append(c)
        elif c in (t[1] for t in brackets):
            if len(stack) == 0:
                return False
            left = [t[0] for t in brackets if c == t[1]]
            if stack.pop() != left[0]:                
                return False
    else:
        if len(stack) == 0:
            return True
        else:
            return False
isValid('()[]{}')
