def letterCombinations(digits):
    num_dic = {'0':' ','1':'*', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    result = []
    tmp = []
    for i in digits:
        if len(result) == 0:
            for k in num_dic[i]:
                result.append(k)
            continue
        for j in num_dic[i]:
            for m in result:
                tmp.append(m+j)
        result = tmp
        tmp = []
    return result
letterCombinations("23")
