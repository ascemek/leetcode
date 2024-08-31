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
        
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            clone = Node(node.val)
            oldToNew[node] = clone
        
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        return dfs(node) if node else None

#___________________________________________________________________________

# Date Log: 08/29/24
# Link: https://neetcode.io/problems/islands-and-treasure
# Difficulty: Medium
# Qnumber = 286

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        distance = 0
        
        def addRoom(r, c):
            if (r < 0 or
               c < 0 or
               r >= rows or
               c >= cols or
               grid[r][c] == -1 or
               (r, c) in visited):
                return
            q.append([r, c])
            visited.add((r, c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            distance += 1
                    
#___________________________________________________________________________

# Date Log: 08/29/24
# Link: https://leetcode.com/problems/rotting-oranges/description/
# Difficulty: Medium
# Qnumber = 994

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0 
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    if (row < 0 or col < 0 or
                        row >= rows, col >= cols or
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
            
        return time if fresh == 0 else -1
    
#___________________________________________________________________________

# Date Log: 08/29/24
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# Difficulty: Medium
# Qnumber = 417

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or 
                heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
            
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
            
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.add([r, c])
        return res
        
#___________________________________________________________________________

# Date Log: 08/30/24
# Link: https://leetcode.com/problems/surrounded-regions/
# Difficulty: Medium
# Qnumber = 130

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # Time Complexity: O(n * m)
    
        rows, cols = len(board), len(board[0])
    
        def dfsCapture(r, c):
            
            if (r < o or c < 0 or 
                r >= rows or c >= cols 
                or board[r][c] != "O"):
                return
            board[r][c] = "T"
            dfsCapture(r + 1, c)
            dfsCapture(r - 1, c)
            dfsCapture(r, c + 1)
            dfsCapture(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and 
                    (r in [0, rows - 1] or c in [0, cols - 1])):
                        dfsCapture(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"   

#___________________________________________________________________________

# Date Log: 08/30/24
# Link: https://leetcode.com/problems/course-schedule/description/
# Difficulty: Medium
# Qnumber = 207

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # map each course to preReq list
        preReqMap = { i:[] for i in range(numCourses)}
        
        for course, preq in prerequisites:
            preReqMap[course].append(preReq)
        
        #all courses along the curr DFS path  
        visitedSet = set()
        def dfs(curCourse):
            if curCourse in visitedSet:
                return False
            if preReq == []:
                return True
            
            visitedSet.add(curCourse)
            for preReq in preReqMap:
                if not dfs(curCourse): return False
            visitedSet.remove(curCourse)
            preReqMap[curCourse] = []
            
        for course in range(numCourses):
            if not dfs(course): return False
        return True
        
#___________________________________________________________________________

# Date Log: 08/30/24
# Link: https://leetcode.com/problems/course-schedule-ii/description/
# Difficulty: Medium
# Qnumber = 210

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

#___________________________________________________________________________

# Date Log: 08/31/24
# Link: https://leetcode.com/problems/redundant-connection/description/
# Difficulty: Medium
# Qnumber = 684

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

#___________________________________________________________________________