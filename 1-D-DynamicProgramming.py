#___________________________________________________________________________

# Date Log: 08/10/24
# Link: https://leetcode.com/problems/climbing-stairs/description/
# Difficulty: Easy
# Qnumber = 70

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
    
    #___________________________________________________________________________