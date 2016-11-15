class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        lst = []
        for i in range(1, n+1):
            if i % 15 == 0:
                lst.append('FizzBuzz')
            elif i % 3 == 0:
                lst.append('Fizz')
            elif i % 5 == 0:
                lst.append('Buzz')
            else:
                lst.append(str(i))
        return lst
