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

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

#___________________________________________________________________________

# Date Log: 08/05/24
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
# Qnumber = 167

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Time complexity: O(N) with no extra space
        
        l, r = 0, len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]

#___________________________________________________________________________

# Date Log: 08/05/24
# Link: https://leetcode.com/problems/container-with-most-water/description/
# Difficulty: Medium
# Qnumber = 11

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            
            area = (r - l) * min(height[r], height[l])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res

#___________________________________________________________________________
