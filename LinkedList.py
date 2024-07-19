#___________________________________________________________________________

# Date Log: 07/15/24
# Link: https://leetcode.com/problems/reverse-linked-list/description/
# Difficulty: Easy
# Qnumber = 206




#___________________________________________________________________________

# Date Log: 07/16/24
# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Difficulty: Easy
# Qnumber = 21

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        DummyNode = ListNode()
        tail = DummyNode

        while(list1 and list2):
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return DummyNode.next
    
#___________________________________________________________________________

# Date Log: 07/18/24
# Link: https://leetcode.com/problems/linked-list-cycle/description/
# Difficulty: Easy
# Qnumber = 141

# This problem can be done by using a hashmap and checking if the visited node is already in the hashmap
# but this would require O(N) space complexity and O(N) time complexity because we create a hashmap (requires extra memory)

# This approach below is O(1) space complexity and O(N) time complexity --> the most optimal solution

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast =  head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#___________________________________________________________________________
