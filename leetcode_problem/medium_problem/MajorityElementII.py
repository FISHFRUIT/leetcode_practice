from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = 0
        num_apper = []
        all_value = []
        for i in range(0,len(nums)):
            if nums[i] not in all_value:
                all_value.append(nums[i])
        while count < len(all_value):
            count_num = 0
            for i in range(0,len(nums)):
                if nums[i] == all_value[count]:
                    count_num = count_num + 1
                if i == len(nums)-1:
                    if count_num > len(nums)/3:
                        num_apper.append(all_value[count])
                    count = count + 1
                    count_num = 0
        return num_apper