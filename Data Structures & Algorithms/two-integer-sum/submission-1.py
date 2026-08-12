class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(len(nums)):
            for y in range(i+1,len(nums)):
                if nums[i] + nums[y] == target:
                    answer.append(i)
                    answer.append(y)
                    break
        return answer
        