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
    
# Date Log: 08/11/24
# Link: https://leetcode.com/problems/house-robber/description/
# Difficulty: Medium
# Qnumber = 198

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

#___________________________________________________________________________