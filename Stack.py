#___________________________________________________________________________

# Date Log: 07/12/24
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy

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
