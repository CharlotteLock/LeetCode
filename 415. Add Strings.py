class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        num1 = num1[::-1]
        num2 = num2[::-1]
        mix = len(num1)
        max = num2
        if len(num2) < mix:
            mix = len(num2)
            max = num1
        sum = 0
        for i in range(mix):
            sum += (num_dict[num1[i]] + num_dict[num2[i]]) * 10 ** i
        print(sum)
        for j, e in enumerate(max[mix: ]):
            sum += num_dict[max[j+mix]] * 10 ** (mix+j)
        return str(sum)
