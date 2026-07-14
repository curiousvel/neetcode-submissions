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

"""
    #Alternate solution with minheap
    class Solution:
    ```
    🧠 MENTAL MODEL: The Min-Heap Escalator (Stream Processing)
    
    Instead of merging entire lists together at once, we pool the heads of all 
    k lists into a Min-Heap. The heap acts like an automated escalator that 
    always presents the smallest available node at the top.
    
    1. Fill the heap with the initial head node from every non-empty list.
    2. Pop the smallest node out, link it to our final merged list.
    3. Re-fill the heap by pushing the immediate next node from the list we just popped from.
    
    This keeps our heap size restricted to a maximum of 'k' elements at any given moment.

    COMPLEXITY:
        - Time Complexity: O(N log k) -> Where N is the total number of nodes across 
          all lists, and k is the number of linked lists. Every push/pop operation 
          takes log(k) time, and we perform this for all N nodes.
        - Space Complexity: O(k) -> The heap holds at most one node from each of the k lists.
    ```
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        heap = []
        
        # STEP 1: Load the heap with the first element of each list.
        # We include the unique list index `i` as a tie-breaker tuple entry.
        # If two nodes share the same value, Python will evaluate `i` next, 
        # preventing it from comparing the raw ListNode objects (which causes a crash).
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
                
        # STEP 2: Drain the heap, stitching the smallest nodes together.
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Append the extracted winner to our master list
            current.next = node
            current = current.next
            
            # STEP 3: Replace the empty slot in the heap.
            # If the list we just popped from has more elements, immediately 
            # push its next node into the heap to stay in the running.
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
"""