class Solution:
    def mySqrt(self, x: int) -> int:
        check = 0
        i = 1
        while check < x:
           check = i * i
           i = i + 1
        return i - 1 if check == x else i - 2 