class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        #Base case is the integer being one
        def solution(n):

            if n == 1:
                return True
            if n < 1:
                return False
        
            return solution(n/2)
    
        return solution(n)
        