from collections import defaultdict

class Solution:
    """
    PATTERN: Undirected Graph Traversal / Cycle Detection (DFS)
    PROBLEM: Graph Valid Tree (LeetCode 261)
    
    ===========================================================================
    💡 HIGH-LEVEL IDEA:
    An undirected graph of N nodes is a valid tree if and only if:
      1. It has NO directed/undirected cycles.
      2. It is fully connected (all N nodes belong to a single component).
      
    We use DFS starting from node 0 to check for cycles:
      - Keep track of visited nodes and pass the 'parent' node to avoid 
        treating the edge back to the immediate predecessor as a cycle.
      - If DFS hits an already-visited node that is NOT the parent, a cycle 
        exists!
      - Finally, verify that the total visited nodes equals N (fully connected).
    ===========================================================================
    
    COMPLEXITY:
    - Time:  O(V + E) -> Touch every node (V) and edge (E) at most once.
    - Space: O(V + E) -> Space for adjacency list, visited set, and recursion stack.
    """
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Quick check: A tree with N nodes must have exactly N - 1 edges
        if len(edges) != n - 1:
            return False

        # Build undirected graph adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Track visisted nodes
        visited = set()

        def has_cycle(node: int, parent: int) -> bool:
            visited.add(node)

            for neighbor in graph[node]:
                # Skip the edge back to the immediate parent
                if neighbor == parent:
                    continue

                # 2. Real Cycle Check: 
                # If the neighbor is visited AND it's NOT our parent, 
                # we've looped back around via a DIFFERENT path -> True Cycle!
                if neighbor in visited or has_cycle(neighbor, node):
                    return True

            return False

        # 1. Cycle check starting from node 0
        if has_cycle(0, -1):
            return False

        # 2. Connectivity check: verify all N nodes were reached
        return len(visited) == n