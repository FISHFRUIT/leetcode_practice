import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        a = 0
        for n in range(1,int(num/2)+1):
            if num % n == 0:
                a += n
        if a == num:
            return True
        return False

    def checkPerfectNumber2(self, num: int) -> bool:
        # Luôn bắt đầu với 1 vì nếu num / 1 = num cộng vào sum > num thì sẽ luôn sai ==> dùng luôn trường hợp 1 để không phải tính
        if num == 1:
            return False
        sum = 1 

        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                sum += i + num/i
        
        return sum == num
    
    def checkPerfectNumber3(self, num: int) -> bool:
        return num in {6, 28, 496, 8128, 33550336}