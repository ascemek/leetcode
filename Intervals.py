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

# Date Log: 09/05/24
# Link: https://leetcode.com/problems/merge-intervals/description/
# Difficulty: Medium
# Qnumber = 56

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Time Complexity: O(nlogn)
        
        intervals.sort()
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
                
        return res

#___________________________________________________________________________

# Date Log: 09/05/24
# Link: https://leetcode.com/problems/non-overlapping-intervals/description/
# Difficulty: Medium
# Qnumber = 435

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Time Complexity: O(nlogn)
        
        intervals.sort()
        res = 0
        
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
                
        return res
            
#___________________________________________________________________________

# Date Log: 09/05/24
# Link: https://neetcode.io/problems/meeting-schedule
# Difficulty: Easy
# Qnumber = 920

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        

#___________________________________________________________________________

# Date Log: 09/06/24
# Link: 
# Difficulty: Medium
# Qnumber = 

#___________________________________________________________________________