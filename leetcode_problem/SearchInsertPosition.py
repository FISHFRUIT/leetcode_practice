from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target not in nums:
            if target > nums[len(nums)-1]:
                return len(nums)
            for i in range(0,len(nums)):
                if nums[i] > target:
                    return nums.index(nums[i])