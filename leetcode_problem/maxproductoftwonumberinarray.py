from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num1 = float('-inf')
        max_num2 = float('-inf')
        for i in range(len(nums)):
            if max_num1 <= nums[i]:
                max_num2 = max_num1
                max_num1 = nums[i]
            else:
                if max_num2 < nums[i]:
                    max_num2 = nums[i]
        return (max_num1 - 1) * (max_num2 - 1)
        