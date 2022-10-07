class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if needle == haystack:
            return 0

        for i in range(len(haystack)-l+1):
            if needle[0] == haystack[i] and needle == haystack[i:i+l]:
                return i 
        return -1
