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
        
        count = {}
        freq = [[] for i in range len(nums)]


        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        
        
        
        
        

#___________________________________________________________________________