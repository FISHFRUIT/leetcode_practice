from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                a.append("FizzBuzz")
            if i % 3 == 0 and i % 5 != 0:
                a.append("Fizz")
            if i % 5 == 0 and i % 3 != 0:
                a.append("Buzz")
            if i % 5 != 0 and i % 3 != 0:
                a.append(str(i))
        return a