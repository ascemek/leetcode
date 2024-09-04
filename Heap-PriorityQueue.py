#___________________________________________________________________________

# Date Log: 09/02/24
# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
# Difficulty: Easy
# Qnumber = 703

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#___________________________________________________________________________

# Date Log: 09/03/24
# Link: https://leetcode.com/problems/last-stone-weight/
# Difficulty: Easy
# Qnumber = 1046

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)
            
            if secondStone > firstStone:
                heapq.heappush(stones, firstStone - secondStone)
                
        return abs(stones[0]) if stones else 0

#___________________________________________________________________________

# Date Log: 09/03/24
# Link: https://leetcode.com/problems/k-closest-points-to-origin/description/
# Difficulty: Medium
# Qnumber = 973

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
            
        heapq.heapify(minHeap)
        res = []
        
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res
            
#___________________________________________________________________________

# Date Log: 09/03/24
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Difficulty: Medium
# Qnumber = 215

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        

#___________________________________________________________________________
