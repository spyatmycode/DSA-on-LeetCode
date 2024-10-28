class Solution:
    def reverse(self, x: int) -> int:


        print(-2147483651 < pow(-2,31)) 

        result = (-abs(int(f"{abs(x)}"[::-1])) if f"{x}"[0] == "-" else int(f"{abs(x)}"[::-1]))


        return result if result < (pow(2, 31) - 1) and result > pow(-2,31) else 0
        