# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    🧠 MENTAL MODEL: The Rigid Measuring Tape (Two-Pointer Gap)
    
    Imagine trying to find the N-th node from the end of a long hallway without 
    counting backwards. Instead, you hold a rigid measuring tape of length 'N'.
    
    1. Send your 'fast' pointer 'N' steps ahead into the hallway.
    2. Now, both 'slow' and 'fast' walk forward at the exact same pace.
    3. The moment 'fast' hits the very end wall, the 'slow' pointer is 
       guaranteed to be standing EXACTLY one step before the target node.
       
    The Dummy Node Shield:
    We attach a dummy node to the front. If N equals the length of the list 
    (meaning we need to delete the head node), 'slow' will stay safely on 
    the dummy node, allowing us to seamlessly bypass the original head.
    
    Complexity:
        - Time: O(L) -> Where L is the length of the list. We traverse the list in a single pass.
        - Space: O(1) -> We only use two pointers.
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to head
        dummy = ListNode(0, head)
        
        # Both pointers start at the dummy anchor
        slow = dummy
        fast = dummy

        # 1. Move 'fast' ahead by N + 1 steps to create the perfect gap
        for _ in range(n + 1):
            fast = fast.next

        # 2. Maintain the gap; move both until 'fast' runs off the board
        while fast:
            slow = slow.next
            fast = fast.next

        # 3. 'slow' is now standing right BEFORE the target node. Delete it!
        slow.next = slow.next.next

        # Return the actual new head (skipping our dummy anchor)
        return dummy.next