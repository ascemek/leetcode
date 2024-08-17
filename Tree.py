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
# Link: https://leetcode.com/problems/balanced-binary-tree/description/
# Difficulty: Easy
# Qnumber = 110

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

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

# Date Log: 08/06/24
# Link: https://leetcode.com/problems/same-tree/description/
# Difficulty: Easy
# Qnumber = 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Recursive DFS - Time Complexity: O(p + q)
        
        if(not p and not q):
            return True
        if(not p or not q) or (p.val != q.val):
            return False
        
        return (self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))
        
#___________________________________________________________________________

# Date Log: 08/09/24
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Difficulty: Medium
# Qnumber = 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root

#___________________________________________________________________________

# Date Log: 08/15/24
# Link: https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy
# Qnumber = 543

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # The DFS is returning the height of the tree. 
        # @Time Complexity: O(N)
        # Space Complexity: O(height) => in other words O(N)
        
        self.res = 0
        
        def dfs(curr):
            
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res

#___________________________________________________________________________

# Date Log: 08/16/24
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Difficulty: Medium
# Qnumber = 199

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        

#___________________________________________________________________________

