class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        j = 0
        k = 0
        one = None
        two = None
        for i in range((len(nums1) + len(nums2)) // 2 + 1):
            for j in range(j, len(nums1)):
                one = nums1[j]
                break
            for k in range(k, len(nums2)):
                two = nums2[k]
                break
            if i > 0:
                presult = result
            if one is None:
                result = two
                k += 1
            elif two is None:
                result = one
                j += 1
            elif one < two:
                result = one
                j += 1
            else:
                result = two
                k += 1
            one = None
            two = None
            if i == 0:
                presult = result
        print(result, presult)
        if (len(nums1) + len(nums2)) % 2 == 0:
            print('..')
            result = (result + presult) / 2.0
        return result
