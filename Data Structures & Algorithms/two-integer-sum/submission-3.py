class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap ={}
        for index, num in enumerate(nums):
            hashMap[num] = index
        
        for i in range(len(nums)):
            y = target - nums[i]
            if y in hashMap and (i!=hashMap[y]):
                return[i,hashMap[y]]

        