class Solution:
    def isValid(self, s: str) -> bool:

        result = True

        stackMap = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        stackOne = []


        for bracket in s:


            if bracket in stackMap:
                stackOne.append(bracket)

            elif len(stackOne) > 0 and bracket in stackMap.values() and bracket == stackMap[stackOne[-1]]:
                stackOne.pop()

            print(bracket,stackOne, result)

            else:
                return False


        if len(stackOne) !=0:
            return False
        
        else:
            return True
        



            


        