class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        while True:
            sum = 0
            for i in range(0,len(str_num)):
                sum += int(str_num[i])
                # print(sum)
            # num = sum
            str_num = str(sum)
            # print(num)
            if len(str_num) == 1:
                return int(str_num)