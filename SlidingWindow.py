#___________________________________________________________________________

# Date Log: 07/30/24
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Difficulty: Medium
# Qnumber = 3

# Sliding window with a set() approach - time complexity: O(N), space complexity: O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
#___________________________________________________________________________

# Date Log: 07/30/24
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Difficulty: Medium
# Qnumber = 424

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0
        
        l = 0
        maxFreq = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])
            
            # while (r - l + 1) - max(count.values()) > k: # Approach #1
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    
#___________________________________________________________________________

# Date Log: 07/30/24
# Link: https://leetcode.com/problems/permutation-in-string/description/
# Difficulty: Medium
# Qnumber = 567



#___________________________________________________________________________