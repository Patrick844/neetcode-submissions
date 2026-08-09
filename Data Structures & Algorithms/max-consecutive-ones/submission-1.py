class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive: int = 0
        count_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count_ones+=1
                max_consecutive = max(max_consecutive, count_ones)
            else:
                count_ones=0
        return max_consecutive
            

