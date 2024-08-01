#___________________________________________________________________________

# Date Log: 07/12/24
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Qnumber = 20

# 20. Valid Paranthese 

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        #check if there is even number of chars
        if(len(s)%2 != 0):
            return False

        for char in s:
            if char in closeToOpen:
                # if stack is not empty and the last element is matching with one of the clostTOpen braces
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop() # remove that from the stack
                else:
                    return False
            else: 
                stack.append(char)
        return True if not stack else False # return true if the stack is empty


#___________________________________________________________________________

# Date Log: 07/31/24
# Link: https://leetcode.com/problems/min-stack/description/
# Difficulty: Medium
# Qnumber = 155

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#___________________________________________________________________________

# Date Log: 07/31/24
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Difficulty: Medium
# Qnumber = 150

# Time Complexity: O(N), Space Complexity: O(N)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(char))
        return stack[0]
                
#___________________________________________________________________________

# Date Log: 07/31/24
# Link: 
# Difficulty: Medium
# Qnumber = 22

# Time Complexity: O(), Space Complexity: O()


#___________________________________________________________________________
        
        
