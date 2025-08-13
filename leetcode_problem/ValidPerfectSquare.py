from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = sqrt(num)
        if n != int(n):
            return False
        return True