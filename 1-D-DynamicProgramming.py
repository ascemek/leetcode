#___________________________________________________________________________

# Date Log: 08/10/24
# Link: https://leetcode.com/problems/climbing-stairs/description/
# Difficulty: Easy
# Qnumber = 70

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # DP - Bottom Up Solution. Time Complexity: O(N)
        
        oneStepPointer, twoStepPointer = 1, 1
        for i in range(n - 1):
            temp = oneStepPointer
            oneStepPointer = oneStepPointer + twoStepPointer
            twoStepPointer = temp
        return oneStepPointer
    
#___________________________________________________________________________
    
# Date Log: 08/11/24
# Link: https://leetcode.com/problems/house-robber/description/
# Difficulty: Medium
# Qnumber = 198

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [rob1, rob2, n, n+1, ...]
        
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
    
#___________________________________________________________________________

# Date Log: 08/12/24
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Difficulty: Easy
# Qnumber = 746

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # DP - Time Complexity: O(N), Space Complexity: O(1)
        
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])
        
#___________________________________________________________________________

# Date Log: 08/12/24
# Link: https://leetcode.com/problems/house-robber-ii/description/
# Difficulty: Medium
# Qnumber = 213

# Time Complexity: O(N), Space Complexity: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        rob1, rob2 = 0, 0
        
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
            
        return rob2
#___________________________________________________________________________

# Date Log: 08/12/24
# Link: https://leetcode.com/problems/house-robber-iii/description/
# Difficulty: Medium
# Qnumber = 337

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # Time Complexity: O(N)
        # [withRoot, withoutRoot]
        
        def dfs(root):
            
            if not root:
                return [0, 0]
            
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            
            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)
            
            return [withRoot, withoutRoot]
        
    return max(dfs(root))

#___________________________________________________________________________
