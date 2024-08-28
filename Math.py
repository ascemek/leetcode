#___________________________________________________________________________

# Date Log: 08/27/24
# Link: https://leetcode.com/problems/self-dividing-numbers/
# Difficulty: Easy
# Qnumber = 728

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = []
        
        for i in range(left, right + 1):
            
            is_self_dividing = True
            
            for digit in str(i):
                if digit = "0" or i % int(digit) != 0:
                    is_self_dividing = False
                    break
                
            if is_self_dividing:
                res.append(i)
                
        return res

#___________________________________________________________________________