#___________________________________________________________________________

# Date Log: 09/12/24
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Qnumber = 136

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
        res = 0
        
        for num in nums:
            res = res ^ num # XOR the numbers with each other
            
        return res
        
#___________________________________________________________________________

# Date Log: 09/12/24
# Link: https://leetcode.com/problems/number-of-1-bits/description/
# Difficulty: Easy
# Qnumber = 191

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
        res = 0
        
        while n > 0:
            res += n % 2
            n = n >> 1
            
        return res
#___________________________________________________________________________

# Date Log: 09/12/24
# Link: https://leetcode.com/problems/counting-bits/description/
# Difficulty: Easy
# Qnumber = 338

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # Time Complexity: O(N)
        
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

#___________________________________________________________________________

# Date Log: 09/14/24
# Link: https://leetcode.com/problems/reverse-bits/description/
# Difficulty: Easy
# Qnumber = 190

class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

#___________________________________________________________________________

# Date Log: 09/16/24
# Link: https://leetcode.com/problems/missing-number/description/
# Difficulty: 
# Qnumber = 268

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
       res = len(nums)
       
       for i in range(len(nums)):
           res ^= nums[i] ^ i
        return res
        
#___________________________________________________________________________

# Date Log: 09/20/2024
# Link: https://leetcode.com/problems/sum-of-two-integers/description/
# Difficulty: Medium
# Qnumber = 371

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        
        

#___________________________________________________________________________
