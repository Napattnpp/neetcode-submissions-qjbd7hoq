class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = dict()
        for num in nums:
            if num in dict1:
                return True
            else:
                dict1[num] = 1
        return False
