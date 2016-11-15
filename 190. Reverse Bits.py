class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit = ''
        while n:
            if n % 2 == 0:
                bit += '0'
            else:
                bit += '1'
            n = n // 2
        result = 0
        length = len(bit)
        print(bit)
        for i, e in enumerate(bit):
            if e == '1':
                result += 2 ** (32 - i - 1)
        return result
