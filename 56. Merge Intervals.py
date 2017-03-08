# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        while True:
            for n, i in enumerate(intervals):
                for m, j in enumerate(intervals):
                    if m == n:
                        continue
                    if i.start > j.end or i.end < j.start:
                        continue
                    intervals.remove(i)
                    intervals.remove(j)
                    if i.start < j.start:
                        left = i.start
                    else:
                        left = j.start
                    if i.end < j.end:
                        right = j.end
                    else:
                        right = i.end
                    intervals.append(Interval(left, right))
                    break
                else:
                    continue
                break
            else:
                break
            continue
        return intervals