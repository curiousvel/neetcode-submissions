from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    🧠 MENTAL MODEL: The Snapshot Level Isolation (BFS)
    
    A standard Breadth-First Search sweeps across a tree row by row. However, 
    because a queue constantly grows as children are discovered, we need a way 
    to separate the current row from the next row.
    
    We solve this using a "Snapshot Window":
    1. At the start of a level, we measure the queue's size: 'qLen = len(queue)'.
    2. We run a loop exactly 'qLen' times. This guarantees we only process 
       the nodes belonging to the current row.
    3. Any children discovered during this loop are safely appended to the back 
       of the queue and will sit patiently until the next row's snapshot.

    COMPLEXITY:
        - Time Complexity: O(N) -> We visit every node in the tree exactly once.
        - Space Complexity: O(N) -> In the worst case (a perfectly balanced tree), 
          the leaf level holds N/2 nodes, meaning the queue will hold up to half 
          the tree's nodes at once.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # EDGE CASE GUARD: If the tree is empty, exit immediately to prevent NoneType crashes.
        if not root:
            return []
        
        result = []
        queue = deque()

        # Start with the root node
        queue.append(root)

        while queue:
            level = []
            
            # THE SNAPSHOT: Freeze the queue length right now. This represents 
            # exactly how many nodes exist on this current level.
            qLen = len(queue)

            for _ in range(qLen):
                node = queue.popleft()

                # Build the values in the level
                level.append(node.val)
                
                # Expand to the next level (pushed to the back of the queue)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Once the snapshot loop finishes, our level row is fully complete
            result.append(level)
        
        return result