class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0

        # Note to self:

        # So basically make sure that the elements that are not equal to val occupy the first slots

        # You don't have to remove val, just replace the first spots with non val values

        # Basically shifting the non-val values forward

        for i, num in enumerate(nums):
            if num != val:
                nums[count] = num
                count += 1

        return count
