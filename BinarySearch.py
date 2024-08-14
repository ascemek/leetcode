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

# Date Log: 08/14/24
# Link: https://leetcode.com/problems/koko-eating-bananas/description/
# Difficulty: Medium
# Qnumber = 875

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = math.ceil(sum(piles) / h), max(piles)
        res = r
        
        while l <= r:
            
            k = (l + r) // 2
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / k)
                
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

#___________________________________________________________________________

# Date Log: 08/14/24
# Link: https://leetcode.com/problems/search-a-2d-matrix/description/
# Difficulty: Medium
# Qnumber = 74

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Time Complexity: log(n) + log(m)
        
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l, r = 0, COLS - 1
        
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        
#___________________________________________________________________________