from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return [int(d) for d in str(num)]

    def plusOne2(self, digits: List[int]) -> List[int]:
        num = 0
        for digit in digits:
            num = num * 10 + digit
        
        num += 1
        return [int(x) for x in str(num)]