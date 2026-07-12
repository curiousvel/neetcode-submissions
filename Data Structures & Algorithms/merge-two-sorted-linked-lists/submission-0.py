# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    🧠 MENTAL MODEL: The Zipper Merge & The Ghost Anchor (Dummy Node)
    
    Imagine zipping up a jacket where 'list1' represents the left teeth and 
    'list2' represents the right teeth. You compare the next tooth on each side, 
    and click the smaller one into place.
    
    The Genius Trick: The Dummy Node (Ghost Anchor)
    When starting a new linked list, figuring out which node is the 'head' usually 
    requires annoying 'if/else' checks. By creating a temporary 'dummy' node:
    1. You anchor the beginning of your chain so you never lose track of it.
    2. 'current' acts as your moving zipper slider, stitching the paths together.
    
    What happens at the end? 
    If one zipper track is longer than the other, you don't need to loop through it! 
    Because it's already sorted, you just take the leftover chain and snap the whole 
    thing onto the end of 'current.next' in a single operation.
    
    Complexity:
        - Time: O(N + M) -> Where N and M are the lengths of the two lists. We visit each node once.
        - Space: O(1) -> We only rearrange existing pointers; no new list nodes are created.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node. This node simplifies the logic for handling the head of the merged list.
        dummy = ListNode()

        # Initialize a pointer 'current' to the dummy node. This pointer will traverse the new merged list.
        current = dummy

        # Iterate while both lists have nodes remaining.
        while list1 and list2:
            # Compare the values of the current nodes in both lists.
            if list1.val < list2.val:
                # If list1's current node is smaller, append it to the merged list.
                current.next = list1
                # Move list1's pointer to the next node.
                list1 = list1.next
            else:
                # Otherwise (if list2's current node is smaller or equal), append list2's current node.
                current.next = list2
                # Move list2's pointer to the next node.
                list2 = list2.next
            
            # Move the 'current' pointer forward in the merged list.
            current = current.next

        # After the loop, one of the lists might still have remaining nodes.
        # Append the rest of the non-empty list to the merged list.
        if list1:
            current.next = list1
        else:
            current.next = list2

        # The dummy node's next pointer points to the head of the actual merged list.
        return dummy.next