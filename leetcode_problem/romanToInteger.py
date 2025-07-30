class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = my_dict[s[len(s)-1]]
        # print(f"{my_dict[s[0]]} Đây là cách lấy giá trị từ dictionary hay một hashmap")  
        # so sánh cái bên trái với cái bên phải, nếu nhỏ hơn thì trừ, nếu lớn hơn thì cộng  
        for i in range(len(s) - 2, -1, -1):
            if my_dict[s[i]] < my_dict[s[i+1]]:
                result -= my_dict[s[i]]
            else:
                result += my_dict[s[i]]
        return result