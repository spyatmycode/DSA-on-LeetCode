class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complementMap = {}


        for i, num in enumerate(nums):
            if (target - num) in complementMap:
                return [i, complementMap[target - num]]
            else:
                complementMap[num] = i

        