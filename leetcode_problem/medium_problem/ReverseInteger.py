class Solution:
    def reverse(self, x: int) -> int:
        b = x
        if x < 0:
            x = x -2*x
        nums = str(x)
        nums = list(nums)                  
        for i in range(len(nums)//2):
            a = nums[i]
            nums[i] = nums[len(nums)-1-i]
            nums[len(nums)-1-i] = a
        nums = int("".join(nums))

        if nums < -2**31 or nums > 2**31 - 1:
            return 0             
        if b < 0:
            nums = nums - 2*nums
            return nums
        return nums
    
    def reverse2(self, x: int) -> int:
        result = str(abs(x))
        temp = int(result[::-1])
        if temp*-1 < -2**31 or temp > 2**31 - 1:
            return 0  
        return temp*-1 if x < 0 else temp
    
    def reverse3(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        
        rev *= sign
        
        # 32-bit signed integer range check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev