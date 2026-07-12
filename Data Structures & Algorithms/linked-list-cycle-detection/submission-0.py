# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    🧠 MENTAL MODEL: The Track and Field Loop (Floyd's Tortoise & Hare)
    
    Imagine two runners on a running track:
    - 'slow' (The Tortoise): Moves forward by 1 step at a time.
    - 'fast' (The Hare): Moves forward by 2 steps at a time.
    
    If the track is a straight line (no cycle), the fast runner will quickly 
    reach the end (None) and the race stops.
    
    However, if the track has a loop, the fast runner will get trapped inside 
    it and start running in circles. Because the fast runner gains 1 step of 
    distance on the slow runner during every single turn, the gap between them 
    will eventually shrink to zero. 
    
    They are guaranteed to collide at the exact same node!
    
    Complexity:
        - Time: O(N) -> If no cycle, fast reaches the end in N/2 steps. If there 
                       is a cycle, fast catches slow in linear time.
        - Space: O(1) -> We only use two pointers, regardless of how big the list is.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # BASE / TERMINATING CONDITION: 
        # If fast or fast.next becomes None, we've hit a dead end -> No cycle!
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps

            # If they land on the exact same node object, a loop exists
            if slow == fast:
                return True
        
        return False