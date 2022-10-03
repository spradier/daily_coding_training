class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # concat arrays and sort them
        concat = nums1 + nums2
        n = len(concat)
        sorted_concat = sorted(concat)
        if n % 2 == 0:
            return((sorted_concat[n//2 - 1] + sorted_concat[n//2]) / 2)
        else: 
            return sorted_concat[n//2]