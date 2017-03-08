class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret_dic = dict()
        for n in nums:
            if n in ret_dic.keys():
                ret_dic[n] += 1
            else:
                ret_dic[n] = 1
        #print(ret_dic)
        ret_dic = sorted(ret_dic.items(), key=lambda x: x[1], reverse=True)
        #print(ret_dic)
        ret = [i[0] for i in ret_dic]
        return ret[:k]