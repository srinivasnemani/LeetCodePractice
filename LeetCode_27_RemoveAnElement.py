from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                if nums[r] == val:
                    nums[r] = '_'
                    r = r - 1
                else:
                    nums[l] = nums[r]
                    nums[r] = '_'
                    r = r - 1
                    l = l + 1
            else:
                l = l + 1

        return r+1

