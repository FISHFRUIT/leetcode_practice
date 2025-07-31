class Solution:
    def isHappy(self, n: int) -> bool:
        skip = set()
        while n != 1:
            if n in skip:
                return False
            skip.add(n)
            sum = 0
            for number in str(n):
                sum += int(number)**2
            n = sum
        return True