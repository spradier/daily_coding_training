class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        k = 0

        neg = 0
        if dividend < 0:
            neg += 1
        if divisor < 0:
            neg += 1

        dividend, divisor = abs(dividend), abs(divisor)

        if divisor == 1 and neg == 1:
            return -dividend
        elif divisor == 1 and neg != 1:
            return dividend




        while dividend >= divisor:
            dividend -= divisor 
            k += 1

        if neg == 1:
            k = -k
        return k