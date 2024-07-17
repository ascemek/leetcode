#___________________________________________________________________________

# Date Log: 07/14/24
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1 #left pointer and right pointer indices
        
        while l <= r:
            m = (l + r) // 2
            if(target > nums[m]):
                l = m + 1
            elif(target < nums[m]):
                r = m - 1
            else:
                return m
        return -1       
        
#___________________________________________________________________________