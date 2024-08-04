#___________________________________________________________________________

# Date Log: 07/14/24
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Qnumber = 704

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

# Date Log: 08/01/24
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Difficulty: Medium
# Qnumber = 153

# Time Complexity: O(log n)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            #if the given array is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1          
        return res     

#___________________________________________________________________________

# Date Log: 08/01/24
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Difficulty: Medium
# Qnumber = 33

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

#___________________________________________________________________________

# Date Log: 08/02/24
# Link: https://leetcode.com/problems/time-based-key-value-store/
# Difficulty: Medium
# Qnumber = 981

class TimeMap:

    def __init__(self):
        self.timeMap =  {} # key : list of [val, timestamp]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timeMap.get(key, [])
        
        # binary search
        l, r  = 0, len(values) - 1
        
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)   
        
#___________________________________________________________________________

#___________________________________________________________________________
