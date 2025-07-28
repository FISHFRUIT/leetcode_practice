import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        while True:
            if n % 2 == 1:
                return False
            if n == 3:
                return False
            if n == 2:
                return True
            n=n/2

    # way 2: use log
    def isPowerOfTwo2(self, n: int) -> bool:
            if n <= 0:
                return False
            x = math.log2(n)
            if x.is_integer():
                return True
            return False

    # way 3: supper optimize
    def isPowerOfTwo3(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n / 2
        return n == 1