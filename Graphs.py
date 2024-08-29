#___________________________________________________________________________

# Date Log: 08/28/24
# Link: https://leetcode.com/problems/number-of-islands/description/
# Difficulty: Medium
# Qnumber = 200

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islandNum = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    islandNum += 1
                    
        return islandNum
    
    def dfs(self, grid, r, c):
        
        rows, cols = len(grid), len(grid[0])
        
        if (r < 0 or
           c < 0 or
           r >= rows or
           c >= cols or
           grid[r][c] != "1"):
               return
        
        grid[r][c] = "0"
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
                    

#___________________________________________________________________________

# Date Log: 08/28/24
# Link: https://neetcode.io/problems/max-area-of-island
# Difficulty: Medium
# Qnumber = 695

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # DFS Solution
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        area = 0
        
        def dfs(r, c):
            if (r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] != 1 or
                (r, c) in visited):
                return 0
            
            visited.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
            
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
                
        return area

#___________________________________________________________________________

# Date Log: 08/28/24
# Link: https://leetcode.com/problems/clone-graph/
# Difficulty: Medium
# Qnumber = 133

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

#___________________________________________________________________________

