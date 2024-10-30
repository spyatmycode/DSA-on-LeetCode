class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        p = 0
        k = 0

        right = 0


        while right + 1 < len(nums):

            if nums[right] == nums[right + 1]:
                nums.pop(right)
            else:
                right += 1

        
        return len(nums)

        