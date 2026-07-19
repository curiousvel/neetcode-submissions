"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    Problem: Clone Graph (LeetCode 133)
    
    ============================================================================
    ALGORITHM: Two-Phase Iterative Copy (DFS Stack) 👥
    ============================================================================
    To copy a graph with cycles, we cannot just blindly copy deep structures, 
    or we will loop forever. We split the work into two independent phases:
    
    1. Node Creation & Mapping Phase:
       We use an iterative DFS stack to traverse the original graph. The moment 
       we discover any original node, we create a blank clone copy of it and 
       store it in a hash map: oldToNew[original_node] = cloned_node.
       
    2. Edge Connection Phase:
       Once all nodes are safely created and registered in our map, we iterate 
       through our map. For every original node, we look up its clone, look up 
       its original neighbors inside oldToNew, and link them together.
    ============================================================================
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Guard Clause: If the input graph is completely empty, return None
        if not node:
            return None
            
        # oldToNew map keeps track of the connection between original and copy nodes
        oldToNew = {}
        
        # Track which nodes have been discovered to avoid looping forever in cycles
        visited = set()
        
        # Initialize our iterative DFS stack with the starting node
        stack = [node]
        visited.add(node)
        
        # Immediately create the clone for our starting node and map it
        oldToNew[node] = Node(val=node.val)

        # PHASE 1: Discover all nodes and map old -> new instances
        while stack:
            curr = stack.pop()

            for nei in curr.neighbors:
                # If we haven't seen this neighbor node yet, it's newly discovered
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
                    # Create its blank clone copy immediately upon discovery
                    oldToNew[nei] = Node(val=nei.val)

        # PHASE 2: Revisit the mapped pairs and wire up their neighbor lists
        for old_node, new_node in oldToNew.items():
            for original_neighbor in old_node.neighbors:
                # Grab the cloned version of the neighbor out of our dictionary
                cloned_neighbor = oldToNew[original_neighbor]
                # Append the cloned neighbor to our cloned node's neighbor list
                new_node.neighbors.append(cloned_neighbor)

        # Return the clone of the node we started our traversal with
        return oldToNew[node]