# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Problem: Path Sum (LeetCode 112) - Iterative Approach
    
    ============================================================================
    ALGORITHM: Iterative DFS with Remaining Sum Tracking 🎒
    ============================================================================
    Instead of using recursion, we maintain an explicit stack. Each element on 
    the stack is a pair: (current_node, remaining_target_sum).
    
    As we step down to a child node, we subtract the current node's value from 
    the target. If we hit a leaf node and the remaining sum exactly matches 
    that leaf's value, we have found a valid root-to-leaf path.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> We visit each node at most once.
    - Space Complexity: O(H) -> The stack holds at most the height of the tree.
    ============================================================================
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Guard Clause: An empty tree has no nodes, so it cannot contain any path sum
        if not root:
            return False
            
        # Initialize stack with pairs: (node, target_sum_needed_at_this_level)
        stack = [(root, targetSum)]
        
        while stack:
            node, curr_target = stack.pop()
            
            # Check if we reached a leaf node
            if not node.left and not node.right:
                # If the leaf's value matches exactly what's left of our target, path found!
                if node.val == curr_target:
                    return True
            
            # Push right child onto stack first (so left child is processed first, standard DFS)
            # We subtract the current node's value from the target for the next level down
            if node.right:
                stack.append((node.right, curr_target - node.val))
                
            if node.left:
                stack.append((node.left, curr_target - node.val))
                
        # If the stack clears out and we never returned True, no valid path exists
        return False