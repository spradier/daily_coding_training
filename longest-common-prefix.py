class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        i = 0
        strs = sorted(strs, key=len)
        max_size = len(strs[0])
        while i < max_size:
            curr_letter = strs[0][i]
            for s in strs:
                if s[i] != curr_letter:
                    return prefix
            prefix += curr_letter
            i += 1
        return prefix