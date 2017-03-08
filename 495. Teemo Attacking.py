class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        time_now = None
        ret = 0
        for t in timeSeries:
            if time_now is None or time_now <= t:
                time_now = t + duration
                ret += duration
            else:
                ret = ret + duration - (time_now - t)
                time_now = t + duration
        return ret