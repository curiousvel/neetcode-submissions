# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    🧠 MENTAL MODEL: The In-Order Escalator
    
    A Binary Search Tree (BST) has a magical property: an "in-order" traversal 
    (Left -> Root -> Right) visits the nodes in perfectly sorted, ascending order.
    
    Instead of using recursion, we use a custom 'stack' to simulate this process:
    1. Go as deep LEFT as possible, pushing every node onto the stack. This acts 
       like an escalator taking us down to the smallest available value.
    2. Pop the top node off the stack (this is the current smallest value).
    3. Count it! If it's our k-th element, we return it immediately.
    4. Pivot to its RIGHT child and repeat the process.

    COMPLEXITY:
        - Time Complexity: O(H + k) -> Where H is the height of the tree. We spend 
          O(H) time driving down to the leftmost leaf, and then visit 'k' nodes. 
          In the best case (small k), this is significantly faster than O(N).
        - Space Complexity: O(H) -> The stack only holds up to the height of the 
          tree at any given moment. In a balanced tree, this is O(log N).
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0  # Counter to track which 'smallest' element we are currently on

        # The loop continues if we have nodes left to explore (cur) 
        # OR if there are parents waiting in the stack to be processed.
        while cur or stack:
            
            # STEP 1: Dive deep left.
            # We push all ancestors onto the stack so we can remember to 
            # come back up to them after processing their smaller left children.
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # STEP 2: Process the current smallest node.
            # When 'cur' becomes None, we've hit the bottom-left boundary.
            # The node at the top of the stack is officially the next smallest element.
            cur = stack.pop()
            n += 1  # We have successfully visited another sorted element
            
            # STEP 3: Early termination check.
            # The moment our counter matches 'k', we can stop completely.
            if n == k:
                return cur.val
            
            # STEP 4: Shift to the right sub-tree.
            # If this node has a right child, it is larger than 'cur' but smaller 
            # than the parent waiting in the stack. We must visit it next.
            cur = cur.right


