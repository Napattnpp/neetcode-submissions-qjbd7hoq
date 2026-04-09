class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        c = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                c += 1
        return False if count == 0 else True