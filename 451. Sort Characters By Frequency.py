class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp_dic = dict()
        ret = ''
        for c in s:
            if c in tmp_dic.keys():
                tmp_dic[c] += 1
            else:
                tmp_dic[c] = 1
        tmp_lst = sorted(tmp_dic.items(), key=lambda x:x[1])
        for i in tmp_lst:
            # print(i[0],i[1])
            ret = i[0] * i[1] + ret
        return ret