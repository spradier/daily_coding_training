class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 0, 1
        for i in range(0,n):
            out = n1 + n2
            n1 = n2 
            n2 = out
        return out