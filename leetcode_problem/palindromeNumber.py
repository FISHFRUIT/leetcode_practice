class Solution:
    def isPalindrome(self, x: int) -> bool:
        before = x
        result = 0
        if x < 0:
            return False
        while x >= 1:
            result = result * 10
            print(f"Day la result: {result}")
            last = x % 10
            print(f"Day la last: {last}")
            x = int(x/10)
            print(f"Day la x: {x}")
            result = result + last
            print(f"Cuoi cung: {result}")
        return int(result) == before
    
    def isPalindrome2(self, x: int) -> bool:
        x = str(x)
        for i in range(0,int(len(x)/2)):
            if x[i] != x[len(x)-i-1]:
                return False
        return True
    
    def isPalindrome3(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
