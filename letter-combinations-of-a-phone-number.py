class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        pad = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        result = []
        
        def dfs(i,curr):
            if i == len(digits):
                result.append(''.join(curr[:]))
                return
            for ch in pad[digits[i]]:
                curr.append(ch)
                dfs(i + 1,curr)
                curr.pop()
        dfs(0,[])
        return result