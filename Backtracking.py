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
        
        # Time Complexity: O(2^n) * O(n) --> 
        # 2^n because we make a choice include or not include and the second part (* n)
        # is because we copy the elemeets to the res
        # Space Complexity: O(N)
        
        res = []
        candidates.sort()
        
        def dfs(i, curCombination, totalSum):
        
            if totalSum == target:
                res.append(curCombinaton.copy())
                return
                
            if totalSum > target or i == len(candidates):
                return
            
            # include candidates[i]
            curCombination.append(candidates[i])
            dfs(i + 1, curCombinaton, totalSum + candidates[i])
            curCombination.pop()
            
            # NOT include candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curCombination, totalSum)
            
        dfs(0, [], 0)
        
        return res
    
#___________________________________________________________________________

# Date Log: 08/21/24
# Link: https://leetcode.com/problems/combination-sum-ii/
# Difficulty: Medium
# Qnumber = 131

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        curPartion =  []
        
        def dfs(i):
            if i == len(s):
                res.append(curPartion.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    curPartion.append(s[i:j+1])
                    dfs(j + 1)
                    curPartion.pop()
                    
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        
#___________________________________________________________________________

# Date Log: 08/22/24
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Difficulty: Medium
# Qnumber = 17

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz" }
        
        def backtrack(i, curStr):
            
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
                
        if digits:
            backtrack(0, "")
            
        return res

#___________________________________________________________________________
