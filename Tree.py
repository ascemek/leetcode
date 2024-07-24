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