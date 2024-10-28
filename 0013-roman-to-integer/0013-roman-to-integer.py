class Solution:
    def romanToInt(self, s: str) -> int:

        romanTable = {
            "I":1,
            "V": 5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        exceptionTable = {
            "I": ["V", "X"],
            "C":["D","M"],
            "X":["L", "C"]
        }

        base10 = 0

        i = 0

        while i < len(s):

            

            if i+1 < len(s) and s[i] in exceptionTable and s[i + 1] in exceptionTable[s[i]]:
                base10 += (romanTable[ next((item for item in exceptionTable[s[i]] if item == s[i+1]), None) ] - romanTable[s[i]])
                i+=2
                
            else:
                base10 += romanTable[s[i]]
                i+=1
        

        return base10
            
            
                
        