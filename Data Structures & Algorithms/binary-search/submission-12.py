class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_i = 0
        right_i = len(nums)-1

        while left_i <= right_i:
            mid_i = (right_i + left_i) // 2

            mid_num = nums[mid_i]
            if mid_num < target:
                left_i = mid_i + 1
            elif mid_num > target:
                right_i = mid_i - 1
            elif mid_num == target:
                return mid_i
        return -1