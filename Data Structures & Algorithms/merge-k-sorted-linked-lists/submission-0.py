# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    🧠 MENTAL MODEL: The Tournament Bracket (Divide & Conquer)
    
    Instead of adding list 2 to list 1, then list 3 to that result sequentially, 
    we group lists into pairs and merge them simultaneously. 
    
    Each round reduces the total number of lists by half:
    Round 1: K lists  -> K/2 pairs merged
    Round 2: K/2 lists -> K/4 pairs merged
    ...until 1 single consolidated list remains.

    COMPLEXITY:
        - Time Complexity: O(N log k) -> Where N is the total number of nodes across 
          all lists, and k is the number of linked lists. There are log(k) matching 
          rounds, and each round processes N nodes total.
        - Space Complexity: O(k) -> For storing the 'working_q' elements in memory.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # EDGE CASE GUARD: If the input array is completely empty, return None immediately.
        if not lists:
            return None

        # Shallow copy to preserve the original input structure
        working_q = lists.copy()

        # The tournament continues until only one master list is left
        while len(working_q) > 1:
            list_merged = []

            # Step across the queue in intervals of 2 to pair up adjacent lists
            for i in range(0, len(working_q), 2):
                l1 = working_q[i]
                # If an odd number of lists exist, the last list sits out this round (l2 = None)
                l2 = working_q[i+1] if (i + 1) < len(working_q) else None
                
                # Merge the pair and push the winner to the next round
                list_merged.append(self.mergeLists(l1, l2))

            # Upgrade the next round's participants
            working_q = list_merged

        return working_q[0] 
        
    def mergeLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy 

        # Standard two-pointer merge sorting strategy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach whichever remaining sublist hasn't been completely drained
        current.next = list1 if list1 else list2

        return dummy.next