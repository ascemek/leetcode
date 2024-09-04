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
        
        # maxHeap solution: Time Complexity: O(N + klogn)
        # O(N) for heapify + We pop k times and popping an element is logn with maxHeap)
        
        res = []
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        while k > 0:
            poppedElement = heapq.heappop(nums)
            res.append(poppedElement)
            k -= 1
        return -res[-1]

#___________________________________________________________________________

# Date Log: 09/04/24
# Link: https://leetcode.com/problems/task-scheduler/
# Difficulty: Medium
# Qnumber = 621

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time      

#___________________________________________________________________________

# Date Log: 09/04/24
# Link: https://leetcode.com/problems/design-twitter/description/
# Difficulty: Medium
# Qnumber = 355

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set) # userId -> set of followeeId
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

#___________________________________________________________________________