# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Problem: Diameter of Binary Tree (LeetCode 543)
    
    ============================================================================
    STRUCTURAL RELATIONSHIP: Node Heights & Path Lengths 🌳
    ============================================================================
    The diameter of a binary tree is the length of the longest path between any 
    two nodes. For any individual node, the longest path passing through it is:
    
        local_diameter = left_subtree_height + right_subtree_height
        
    We use a Depth-First Search (DFS) helper to visit every node. At each node, 
    we perform a dual action:
    
    1. Calculate Local Path: Sum the heights of its left and right child subtrees.
       Update our global maximum tracker if this local path is the longest seen.
       
    2. Return Node Height: Return the maximum height of its deepest branch up to 
       its parent, adding 1 to represent the current node itself:
       height = 1 + max(left_subtree_height, right_subtree_height)
       
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> Every node is visited exactly once.
    - Space Complexity: O(H) -> Recursion stack matches the height of the tree.
    ============================================================================
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = 0 

        def dfs(node):
            # WHY WE NEED NONLOCAL:
            # Python variables in an outer scope are read-only by default inside nested functions.
            # Without 'nonlocal', assigning 'longest_diameter = max(...)' would cause Python 
            # to create a local variable instead of updating the actual tracker above.
            nonlocal longest_diameter  
            
            # Base Case: An empty node contributes 0 to the height of a branch
            if not node:
                return 0
            
            # 1. Recursively find the height of the left and right child subtrees
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            # 2. Calculate the longest path passing through the current node
            diameter = left_h + right_h
            
            # 3. Update the global maximum if the local path is larger
            longest_diameter = max(longest_diameter, diameter)

            # 4. Return the height of this node's subtree up to its parent
            # (Height of the deeper child branch + 1 for the current node)
            return 1 + max(left_h, right_h)

        dfs(root)
        return longest_diameter