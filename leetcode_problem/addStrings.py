class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        is_carrying = False
        if len(num1) >= len(num2):
            num_max = num1
            num_min = num2
        else:
            num_max = num2
            num_min = num1


        result = ""
        
        for i in range(-1, -len(num_max) - 1, -1):
            try:
                min_digit = int(num_min[i])
            except:
                min_digit = 0

            temp_res = int(num_max[i]) + min_digit
            if is_carrying:
                temp_res += 1

            if temp_res >= 10:
                is_carrying = True
                temp_res -= 10
            else:
                is_carrying = False

            result += str(temp_res)

        if is_carrying:
            result += "1"

        return result[::-1]

        