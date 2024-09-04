#___________________________________________________________________________

# Date Log: 09/04/24
# Link: https://leetcode.com/problems/insert-interval/description/
# Difficulty: Medium
# Qnumber = 57

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                
        res.append(newInterval)
        return res

#___________________________________________________________________________