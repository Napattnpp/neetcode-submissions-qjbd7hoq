class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0

        for n in nums:
            # Check if it's the start of a sequence
            if (n - 1) not in unique_nums:
                # It's the start of a sequence
                length = 0
                while (n + length) in unique_nums:
                    length += 1
                    longest = max(length, longest)
        return longest