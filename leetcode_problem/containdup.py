from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dup = set()
        # for i in range(0,len(nums)):
        #     if nums[i] in dup:
        #         return True
        #     dup.add(nums[i])
        # return False
        arr = len(nums)
        setlen = len(set(nums))
        if arr==setlen:
            return False
        else:
            return True