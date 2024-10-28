class Solution:
    def reverse(self, x: int) -> int:


        #note to self: you're supposed to use the reversed value to check the conditions not x value


        result = (-abs(int(f"{abs(x)}"[::-1])) if f"{x}"[0] == "-" else int(f"{abs(x)}"[::-1]))


        return result if result < (pow(2, 31) - 1) and result > pow(-2,31) else 0
        