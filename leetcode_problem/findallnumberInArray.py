from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            temp = abs(nums[i]) - 1
            if temp <= len(nums) - 1:
                if nums[temp] > 0:
                    nums[temp] *= -1
        
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i + 1)
        
        return result