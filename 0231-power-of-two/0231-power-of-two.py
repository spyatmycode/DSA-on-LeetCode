class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        #Base case is the integer being one
        def solution(n):
            #The base case
            if n == 1:
                #This is 
                return True
            #The number is definitely not a power of two
            if n < 1:
                return False
            #Call solution function recursively with the integer/2
            return solution(n/2)
    
        return solution(n)
        