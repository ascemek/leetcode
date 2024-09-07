#___________________________________________________________________________

# Date Log: 09/07/24
# Link: https://leetcode.com/problems/jump-game/description/
# Difficulty: Medium
# Qnumber = 55

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Time Complexity: O(N)
        
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

#___________________________________________________________________________

# Date Log: 09/07/24
# Link: https://leetcode.com/problems/jump-game-ii/description/
# Difficulty: Medium
# Qnumber = 45

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0 
        l, r = 0, 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

#___________________________________________________________________________

# Date Log: 09/07/24
# Link: https://leetcode.com/problems/gas-station/description/
# Difficulty: Medium
# Qnumber = 134

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
#___________________________________________________________________________