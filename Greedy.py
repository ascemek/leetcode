#___________________________________________________________________________

# Date Log: 09/07/24
# Link: https://leetcode.com/problems/jump-game/description/
# Difficulty: Medium
# Qnumber = 55

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Time Complexity: O(N)
        
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

#___________________________________________________________________________

# Date Log: 09/07/24
# Link: https://leetcode.com/problems/jump-game-ii/description/
# Difficulty: Medium
# Qnumber = 45

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0 
        l, r = 0, 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

#___________________________________________________________________________

# Date Log: 09/07/24
# Link: https://leetcode.com/problems/gas-station/description/
# Difficulty: Medium
# Qnumber = 134

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Time Complexity: O(N)
        
        if sum(gas) < sum(cost):
            return -1
        
        res = 0
        total = 0
        
        for i in range(len(gas)):
            
            total += gas[i] - cost[i]
            
            if total < 0:
                total = 0
                res = i + 1
                
        return res
        
#___________________________________________________________________________

# Date Log: 09/08/24
# Link: https://leetcode.com/problems/hand-of-straights/description/
# Difficulty: Medium
# Qnumber = 846

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # Time Complexity: O(nlogn)
        
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for num in count:
            count[num] = 1 + count.get(num, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first = minHeap[0]
            
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
        return True           

#___________________________________________________________________________

# Date Log: 09/09/24
# Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/
# Difficulty: Medium
# Qnumber = 1899

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set()
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3   

#___________________________________________________________________________

# Date Log: 09/09/24
# Link: https://leetcode.com/problems/partition-labels/description/
# Difficulty: Medium
# Qnumber = 763

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndex = {} # char -> lastIndex in s
        
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        size, end = 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])
            
            if i == end:
                res.append(size)
                size = 0
        return res
    
#___________________________________________________________________________

# Date Log: 09/10/24
# Link: 
# Difficulty: Medium
# Qnumber = 

#___________________________________________________________________________