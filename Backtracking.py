#___________________________________________________________________________

# Date Log: 08/06/24
# Link: https://leetcode.com/problems/combination-sum/description/
# Difficulty: Medium
# Qnumber = 39

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, curCombination, totalSum):
            if totalSum == target:
                res.append(curCombination.copy())
                return
            if i >= len(candidates) or totalSum > target:
                return
            
            curCombination.append(candidates[i])
            dfs(i, curCombination, totalSum + candidates[i])
            curCombination.pop()
            dfs(i + 1, curCombination, totalSum)
            
        dfs(0, [], 0)
            
        return res

#___________________________________________________________________________

# Date Log: 08/06/24
# Link: https://leetcode.com/problems/word-search/description/
# Difficulty: Medium
# Qnumber = 79

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] !=  board[r][c] or
                (r,c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
    return False
            
#___________________________________________________________________________

# Date Log: 08/19/24
# Link: https://leetcode.com/problems/subsets/description/
# Difficulty: Medium
# Qnumber = 78

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Time Complexity: O(n * 2^n) because there are 2^n subsets we can make
        
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(nums[i])
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # decision to NOT include nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        
        return res
    
#___________________________________________________________________________

# Date Log: 08/19/24
# Link: https://leetcode.com/problems/subsets-ii//description/
# Difficulty: Medium
# Qnumber = 90

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

#___________________________________________________________________________

# Date Log: 08/20/24
# Link: https://leetcode.com/problems/permutations/description/
# Difficulty: Medium
# Qnumber = 46

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # Time Complexity: n! * n^2
        # Space Complexity: n! * n
        
        perms = [[]]
        
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    new_perms.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
        
#___________________________________________________________________________

# Date Log: 08/20/24
# Link: https://leetcode.com/problems/combination-sum-ii/
# Difficulty: Medium
# Qnumber = 40

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        
#___________________________________________________________________________