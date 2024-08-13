#___________________________________________________________________________

# Date Log: 07/23/24
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Qnumber = 49


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    res = defaultdict(list) 
    # res is a defaultdict where the default value for any new key is an empty list. 
    # This will store the groups of anagrams.
    
    for string in strs:
        
        charCount = [0] * 26
        
        for char in string:
            
            charCount[ord(char) - char("a")] += 1
            
            res[tupple(charCount)].append(string)
            # tuple(charCount) converts the charCount list to a tuple so it can be used as 
            # a dictionary key (lists cannot be used as dictionary keys because they are mutable).
            
    return res.values()
    
#___________________________________________________________________________

# Date Log: 07/23/24
# Link: https://leetcode.com/problems/top-k-frequent-elements/description/
# Difficulty: Medium
# Qnumber = 347

# Approach 1
# find the frequency of each element HashMap = {number : itsFreq}
# sort that HashMap in ascending order
#Time Complexity: O(n logn) --> not the best because we don't need to sort the whole thing we just need the top k elements
         
# Approach 2
# find the frequency of each element
# add each (key:value) pair to the Max Heap
# Pop the top k element of the heap
# O(k logn) where k is the most frequent element (given in the question)
        
# Optimal Solution
# Bucket sort
        
def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    count = {}
    freq = [[] for i in range len(nums) + 1]
            
    for number in nums:
        count[number] = 1 + count.get(number, 0)
    for number, countItem in count.items():
        freq[countItem].append(number)
                
    res = []
    for i in range(len(freq) -1, 0, -1):
        for number in freq[i]:
            res.append(number)
            if len(res) == k:
                return res
            
#___________________________________________________________________________

# Date Log: 07/26/24
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Qnumber = 347

prevMap = {} # index : value

for index, number in enumarate(nums):
    diff = target - number
    if diff in prevMap:
        return [prevMap[diff], i]
    prevMap[n] = i
    

#___________________________________________________________________________

# Date Log: 08/13/24
# Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
# Difficulty: Medium
# Qnumber = 128

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            if (num - 1) in numSet:
                continue
            
            currLongest = 0
            
            while num in numSet:
                currLongest += 1
                numSet.remove(num)
                num += 1
                
            longest = max(longest, currLongest)
                
        return longest

#___________________________________________________________________________

# Date Log: 08/13/24
# Link: https://leetcode.com/problems/valid-sudoku/
# Difficulty: Medium
# Qnumber = 36

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Time and Space Complexity: O(N^2)
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True
#___________________________________________________________________________

        

        
        
        
        
        
        
        
        

#___________________________________________________________________________