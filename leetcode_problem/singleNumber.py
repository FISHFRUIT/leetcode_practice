from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        storge1 = []
        storge2 = []
        for i in range(0,len(nums)):
            if nums[i] in storge1:
                storge2.append(nums[i])
            storge1.append(nums[i])
        for i in range(0,len(storge1)):
            if storge1[i] not in storge2:
                return storge1[i]
    def singleNumber2(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            my_dict[num] = 0
        
        for i in range(0, len(nums)):
            my_dict[nums[i]] += 1

        for key, value in my_dict.items():
            if value == 1:
                return key
            
    # using XOR
    # ➤ Tính chất đặc biệt của XOR trong bài này:
    # a ^ a = 0

    # a ^ 0 = a

    # Giao hoán & kết hợp được: a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

    def singleNumber3(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a=a^i
        return a
        
