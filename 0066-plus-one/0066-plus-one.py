class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string = [f"{num}" for num in digits]

        subresult = int("".join(string)) + 1

        return [int(num) for num in str(subresult)]
        