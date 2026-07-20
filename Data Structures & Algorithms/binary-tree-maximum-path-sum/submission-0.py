# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Problem: Binary Tree Maximum Path Sum (LeetCode 124) - Recursive
    
    ============================================================================
    ALGORITHM: Post-Order Traversal with Path Clamping 🌲
    ============================================================================
    1. Visit left and right children first (Bottom-Up / Post-Order).
    2. Clamp any negative child gains to 0 (we drop paths that decrease sum).
    3. Calculate 'local_split_path' = node.val + left_gain + right_gain.
       Update global max_sum if local_split_path beats it.
    4. Return single-branch path contribution to parent:
       node.val + max(left_gain, right_gain).
       
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> Each node is visited exactly once.
    - Space Complexity: O(H) -> Recursion depth depends on tree height H.
    ============================================================================
    """
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        # Initialize max_sum to negative infinity to safely handle trees with all negative values
        self.max_sum = float('-inf')
        
        def max_gain(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            
            # Post-Order step: Recursively get max gain from left and right subtrees
            # Clamp to 0 so we don't carry negative path sums upwards
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # 1. Price of a new path with 'node' as the highest split point (Local Curve)
            price_newpath = node.val + left_gain + right_gain
            
            # Update global max_sum if the split path through this node is superior
            self.max_sum = max(self.max_sum, price_newpath)
            
            # 2. Return max gain node can contribute to its parent (Straight Branch)
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return int(self.max_sum)
        