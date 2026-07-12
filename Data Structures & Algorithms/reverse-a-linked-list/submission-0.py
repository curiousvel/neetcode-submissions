# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    🧠 MENTAL MODEL: The Three-Pointer Train Track
    
    Instead of recursion, imagine you are moving down the track and flipping 
    the arrows one-by-one as you pass them. 
    
    To flip an arrow without losing your place, you only need 3 pointers:
    1. 'prev': The node behind you (starts as None).
    2. 'curr': The node you are currently standing on (starts at head).
    3. 'nxt':  The node ahead of you (your safety net so you don't lose the rest of the list).
    
    The 4-Step Dance inside the loop:
    1. Save the node ahead:          nxt = curr.next
    2. Flip the current arrow back:  curr.next = prev
    3. Step 'prev' forward:          prev = curr
    4. Step 'curr' forward:          curr = nxt
    """
    def reverseList(self, head: Optional[TreeNode]) -> Optional[TreeNode]:
        prev = None
        curr = head
        
        # BASE / TERMINATING CONDITION: 
        # Keep going until 'curr' runs off the end of the list (becomes None)
        while curr:
            nxt = curr.next    # 1. Save the next node
            curr.next = prev   # 2. Reverse the link (point backward)
            
            prev = curr        # 3. Move prev forward
            curr = nxt         # 4. Move curr forward
            
        # When curr becomes None, 'prev' is left standing on the new head!
        return prev
        