from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_real = (pivot + mid) % len(nums)
            if nums[mid_real] > target:
                right = mid - 1
            elif nums[mid_real] < target:
                left = mid + 1
            else:
                return mid_real
        
        return -1
