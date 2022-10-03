class Solution:
    def intToRoman(self, num: int) -> str:
        m, cm, d, cd, c, xc, l, xl, x, ix, v, iv = 0,0,0,0,0,0,0,0,0,0,0,0
        m, num = num // 1000, num % 1000
        if num // 900 >= 1:
            cm, num = num // 900, num % 900
        if num // 500 >= 1:
            d, num = num // 500, num % 500
        if num % 400 < 100:
            cd, num = num // 400, num % 400
        c, num = num // 100, num % 100
        if num // 90 >= 1:
            xc, num = num // 90, num % 90
        if num // 50 >= 1:
            l, num = num // 50, num % 50
        if num % 40 < 10:
            xl, num = num // 40, num % 40
        x, num = num // 10, num % 10
        if num == 9:
            ix, num = 1, 0
        if num // 5 >= 1:
            v, num = num // 5, num % 5
        if num == 4:
            iv, num = 1, 0
        
        result = m*'M' + cm*'CM' + d*'D' + cd*'CD' + c*'C' + xc*'XC' + l*'L' + xl*'XL' + x*'X' + ix*'IX' + v*'V' + iv*'IV' + num*'I'
        return result