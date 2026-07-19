# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Problem: Reorder List (LeetCode 143)
    
    ============================================================================
    ALGORITHM: Three-Phase Linked List Manipulation 🔗
    ============================================================================
    To reorder the list in-place to follow the L0 -> Ln -> L1 -> Ln-1 pattern, 
    the problem decomposes into three distinct structural phases:
    
    1. Split: Use a Slow/Fast pointer technique to locate the middle node. 
       Sever the connection between the first half and second half to create 
       two independent sub-lists.
       
    2. Reverse: Reverse the entirety of the second sub-list. This aligns the 
       nodes so that the end nodes are accessible in sequential forward order.
       
    3. Interleave: Systematically weave the nodes of the two lists together 
       by adjusting their next pointers until the second list is fully exhausted.
       
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> O(N) to find the mid, O(N) to reverse the second 
      half, and O(N) to interleave.
      
    - Space Complexity: O(1) -> All modifications are executed in-place by 
      reassigning object references; no stack or dynamic memory is allocated.
    ============================================================================
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""
        # A list with fewer than 3 nodes cannot be reordered
        if not head or not head.next or not head.next.next:
            return

        # Phase 1: Split the list at the midpoint and sever the bridge
        second_half_head = self._split_list(head)
        
        # Phase 2: Reverse the second half to prepare for interleaving
        second_half_head = self._reverse_list(second_half_head)

        # Phase 3: Interleave the two sub-lists together
        first_curr = head
        second_curr = second_half_head

        while second_curr:
            # Stash the next nodes in both sequences before overwriting references
            next_first = first_curr.next
            next_second = second_curr.next
            
            # Weave second_curr right between first_curr and next_first
            first_curr.next = second_curr
            second_curr.next = next_first

            # Shift the running trackers forward to their stashed destinations
            first_curr = next_first
            second_curr = next_second

    def _split_list(self, node: ListNode) -> ListNode:
        """Finds the middle node, severs the first half, and returns the second half head."""
        slow, fast = node, node

        # Move fast at double speed to land slow right at the midpoint partition
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # Sever the connection between the two halves to prevent cycles
        second_half_start = slow.next
        slow.next = None

        return second_half_start

    def _reverse_list(self, node: ListNode) -> ListNode:
        """Reverses a linked list in O(1) space and returns the new head pointer."""
        prev = None
        curr = node

        while curr:
            next_temp = curr.next  # Stash the remaining tail
            curr.next = prev       # Invert the pointer direction
            prev = curr            # Step prev forward
            curr = next_temp       # Step curr forward

        return prev