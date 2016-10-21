def longestCommonPrefix(strs):
    comPrefix_long = ''
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    for n, i in enumerate(strs[0]):
        for j in strs[1:len(strs)]:
            if n >= len(j):
                    return comPrefix_long
            if i != j[n]:
                return comPrefix_long
        comPrefix_long += i
    return comPrefix_long
longestCommonPrefix(["adfg","abdfg","ad","adf"])
