class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateMap = {}
        for num in nums:
            if num not in duplicateMap:
                duplicateMap[num] = 1
            else:
                return True
        return False