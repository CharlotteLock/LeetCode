# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        index = 0
        while True:
            for n, i in enumerate(intervals):
                if i.end < newInterval.start:
                    continue
                if i.start > newInterval.end:
                    #index = n
                    intervals.insert(n, newInterval)
                    return intervals
                if i.start < newInterval.start:
                    #i.start --
                    newInterval.start = i.start
                if i.end > newInterval.end:
                    # -- i.end
                    newInterval.end = i.end
                intervals.remove(i)
                break
            else:
                intervals.append(newInterval)
                return intervals