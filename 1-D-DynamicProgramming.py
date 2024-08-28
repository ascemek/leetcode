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

# Date Log: 08/22/24
# Link: https://leetcode.com/problems/longest-palindromic-substring/description/
# Difficulty: Medium
# Qnumber = 5

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0
        
        def isPalindrome(l, r):
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curPalLen = l - r + 1
                if curPalLen > resLen:
                    res = s[l:r+1]
                    resLen = curPalLen
                l, r = l - 1, r + 1
        
        for i in range(len(s)):
            # odd length s
            isPalindrome(i, i)
            
            # even length s
            isPalindrome(i, i + 1)
            
        return res
        
#___________________________________________________________________________

# Date Log: 08/23/24
# Link: https://leetcode.com/problems/palindromic-substrings/description/
# Difficulty: Medium
# Qnumber = 647

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # Time Complexity: O(N^2)
        
        res = 0
        
        for i in range(len(s)):
            # odd length substring
            res += self.countPali(s, i, i)
            # even length substring
            res += self.countPali(s, i, i + 1)
        return res
    
    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l, r = l - 1, r + 1
        return res
        
#___________________________________________________________________________

# Date Log: 08/23/24
# Link: https://leetcode.com/problems/decode-ways/description/
# Difficulty: Medium
# Qnumber = 91

class Solution:
    def numDecodings(self, s: str) -> int:
        
        # Recursive - O(N) Memory solution
        
        dp  = {len(s) : 1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if(i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)        
        
#___________________________________________________________________________

# Date Log: 08/25/24
# Link: https://leetcode.com/problems/coin-change/description/
# Difficulty: Medium
# Qnumber = 322

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Time Complexity: O(amount * len(coins))
        # Memory Complexity: O(amount)
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for amount in range(1, amount + 1):
            for coin in coins:
                if amount - coins >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

#___________________________________________________________________________

# Date Log: 08/26/24
# Link: https://leetcode.com/problems/coin-change/description/
# Difficulty: Medium
# Qnumber = 139

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

#___________________________________________________________________________