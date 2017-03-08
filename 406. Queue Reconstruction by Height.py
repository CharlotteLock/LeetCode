class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [] # 最终结果
        flag = 0
        while True:
            if len(people) == 0:
                break
            for n,i in enumerate(people):
                if i[1] == flag:
                    tmp_p = i
                    people.pop(n)
                    if n == len(people):
                        flag += 1
                    break
            else:
                flag += 1
                continue
            if len(ret) == 0:
                ret.append(tmp_p)
            else:
                tmp_k = tmp_p[1]
                for m,j in enumerate(ret):
                    if tmp_k == 0:
                        #print(tmp_p, j)
                        if tmp_p[0] < j[0]:
                            ret.insert(m,tmp_p)
                        if tmp_p[0] >= j[0]:
                            continue
                            #ret.insert(m+1,tmp_p)
                        #print(ret)
                        break
                    else:
                        if j[0] >= tmp_p[0]:
                            tmp_k -= 1
                            # print(tmp_p)
                            # print(j)
                            # print(tmp_k)
                else:
                    ret.append(tmp_p)
        return ret