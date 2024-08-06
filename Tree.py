#___________________________________________________________________________

# Date Log: 07/19/24
# Link: https://leetcode.com/problems/invert-binary-tree/description/
# Difficulty: Easy
# Qnumber = 226

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

#___________________________________________________________________________

# Date Log: 07/19/24
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Difficulty: Easy
# Qnumber = 104

# The following all have the same time and space complexity: O(N)

# Recursive DFS (Easiest Syntax)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative DFS with Stack

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        stack = [[root, 1]]
        result = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result
        
        
# BFS with Queue

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

#___________________________________________________________________________

# Date Log: 07/22/24
# Link: 
# Difficulty: Easy
# Qnumber = 110

#___________________________________________________________________________

# Date Log: 08/04/24
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Difficulty: Medium
# Qnumber = 235

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
#___________________________________________________________________________

# Date Log: 08/04/24
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium
# Qnumber = 102

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Time complexity: O(N) Space complexity: O(N)
        
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                if level:
                    res.append(level)
        return res
            
#___________________________________________________________________________

# Date Log: 08/05/24
# Link: https://leetcode.com/problems/validate-binary-search-tree/description/
# Difficulty: Medium
# Qnumber = 98

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Time Complexity: O(N)
        
        # recursive
        
        def valid(node, leftBoundary, rightBoundary):
            if not node:
                return True
            if not (leftBoundary < node.val) and (rightBoundary > node.val):
                return False
            return (valid(node.left, leftBoundary, node.val) and valid(node.right, node.val, rightBoundary))
        
        return valid(root, float("-inf"), float("inf"))
    
#___________________________________________________________________________


