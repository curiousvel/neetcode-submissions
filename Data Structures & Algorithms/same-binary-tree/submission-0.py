# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    🧠 MENTAL MODEL: Synchronized Mirror Walk (Parallel Traversal)
    
    To prove two trees are identical, you must walk through them in lockstep. 
    Imagine you have a video game controller that moves an avatar in Tree P 
    and an avatar in Tree Q simultaneously.
    
    At every single step, you check for perfect symmetry:
    1. Are both avatars standing on solid ground (nodes)? -> Keep moving.
    2. Did both avatars hit a wall (None) at the same time? -> Good, that's a match.
    3. Did one avatar hit a wall while the other is on a node? -> Desync! (False)
    4. Are they on different numbers? -> Desync! (False)
    
    If they survive the current spot, they must both successfully duplicate 
    this synchronized walk down the LEFT path AND the RIGHT path.
    
    Complexity:
        - Time: O(min(N, M)) -> We visit at most the total number of nodes in the smaller tree.
        - Space: O(min(H1, H2)) -> The call stack depth equals the height of the shorter tree.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: If both nodes are None, they are considered identical (end of a branch).
        if not p and not q:
            return True

        # Base Case 2: If only one of the nodes is None, they are not identical.
        if (p and not q) or (q and not p):
            return False

        # Base Case 3: If both nodes exist but their values are different, they are not identical.
        if p.val != q.val:
            return False

        # Recursive Step: If current nodes are identical in structure and value,
        # recursively check their left subtrees AND their right subtrees.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)