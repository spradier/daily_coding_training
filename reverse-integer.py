class Solution:
    def reverse(self, x: int) -> int:

        begin = True 

        if x < -2**31 or x > 2**31-1 or x == 0:
            return 0
        
        s = str(x)
        sign = ''

        if s[0] == '-':
            sign = '-'
            s = s[1:]
        if s[-1] == '0':
            s = s[:-1]

        new_s = ''

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0' and begin == True:
                pass
            elif s[i] != '0' and begin == True:
                begin = False
                new_s = new_s + s[i]
            else:
                new_s = new_s + s[i]
        
        return sign + new_s