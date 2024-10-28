class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []


        for i, num in enumerate(nums):

            if i > 0 and nums[i - 1] == num:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                threeSum = num + nums[right] + nums[left]

                if threeSum < 0:
                    left += 1
                
                elif threeSum > 0:
                    right -= 1

                else:

                    result.append([num, nums[right], nums[left]])

                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
        

        return result

                    
        