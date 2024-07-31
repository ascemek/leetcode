#___________________________________________________________________________

# Date Log: 07/14/24
# Link: https://leetcode.com/problems/valid-palindrome/description/
# Difficulty: Easy
# Qnumber = 125

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Approach #1
        # this approach is using extra memory since we create a new variable and use "cheat" built-in functions
        newString = "" #this is the new string that we will have once we get rid of the non-aphanumeric chars

        for char in s:
            if char.isalnum():
                newstring += char.lower()
        return newString == newString[::-1]
    
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Approach #2
        # With custom function and two pointers (right and left comparison approach)
        
        l, r = 0, len(s) - 1
        
        while(l < r):
            while(l < r and not self.alphaNum(s[l])):
                l += 1
            while(r > l and not self.alphaNum(s[r])):
                r -= 1    
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
            
    def alphaNum(self, char):
        return (ord("A") <= ord(char) <= ord("Z") or
                ord("a") <= ord(char) <= ord("z") or
                ord("0") <= ord(char) <= ord("9"))
        
#___________________________________________________________________________

# Date Log: 07/26/24
# Link: https://leetcode.com/problems/3sum/description/
# Difficulty: Medium
# Qnumber = 15


#___________________________________________________________________________
