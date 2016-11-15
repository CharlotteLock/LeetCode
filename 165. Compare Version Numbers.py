class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vl1 = version1.split('.')
        vl2 = version2.split('.')
        mix = len(vl1)
        if len(vl2) < mix:
            mix = len(vl2)
        for i in range(mix):
            if int(vl1[i]) > int(vl2[i]):
                return 1
            if int(vl1[i]) < int(vl2[i]):
                return -1
        if len(vl1) > len(vl2) and int(vl1[-1]) != 0:
            return 1
        elif len(vl1) < len(vl2) and int(vl2[-1]) != 0:
            return -1
        else:
            return 0
