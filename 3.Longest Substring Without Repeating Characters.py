def lengthOfLongestSubstring(s):
    maxs = 0
    max_sub = ''
    length = 0
    for i, e in enumerate(s):
        if i == 0:
            maxs = 1
            max_sub += s[i]
        elif s[i] not in max_sub:
            max_sub += s[i]
            maxs += 1
        else:
            if maxs > length:
                length = maxs
            max_sub = max_sub.split(s[i])[-1] + s[i]
            maxs = len(max_sub)
    if maxs > length:
        length = maxs
    return length
#lengthOfLongestSubstring('abcabcbb')
