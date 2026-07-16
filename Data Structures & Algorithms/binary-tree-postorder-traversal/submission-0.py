# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Problem: Binary Tree Post-Order Traversal (Iterative)
    
    ============================================================================
    ALGORITHM: Inverse Pre-Order Traversal (Reversal Trick) ⏪
    ============================================================================
    Standard Pre-Order: Root -> Left -> Right
    Inverse Pre-Order:  Root -> Right -> Left
    
    By performing an Inverse Pre-Order traversal using a stack, we can simply
    reverse the final output array at the end to get the exact Post-Order sequence:
    
    [Root -> Right -> Left]  ---REVERSED--->  [Left -> Right -> Root]
    
    This elegant approach allows us to solve the post-order traversal iteratively
    without needing complex state-tracking pointers or visited sets.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> We visit every node in the tree exactly once.
    - Space Complexity: O(H) -> The stack size scales with the height of the tree 
      (worst-case O(N) for a skewed tree, best-case O(log N) for balanced).
    ============================================================================
    """
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # Edge Case: Return empty list if the tree is empty
        if not root:
            return []
            
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            # STACK TRICK: Since a stack is LIFO (Last-In, First-Out),
            # we push Left first so that Right is on top. 
            # This ensures Right gets popped first, generating Root -> Right -> Left.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Reverse the entire result list to yield Left -> Right -> Root
        return res[::-1]
        