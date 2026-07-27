from collections import defaultdict

class Solution:
    """
    Problem: Number of Connected Components in an Undirected Graph (LeetCode 323)

    High-Level Idea:
    1. Build an adjacency list representation of the undirected graph.
    2. Maintain a `visited` set to track explored nodes across components.
    3. Iterate through all nodes from 0 to n-1. Encountering an unvisited node 
    signals the discovery of a brand-new connected component ("island").
    4. Trigger a DFS from that node to visit and mark all nodes belonging to 
    that specific component, preventing them from triggering new counts.

    Complexity:
    - Time: O(V + E) — Each node and edge is traversed a constant number of times.
    - Space: O(V + E) — Adjacency list storage and O(V) space for call stack/visited set.
    """

    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build the undirected adjacency list graph representation
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        components = 0
        
        # DFS helper: recursively explores and marks all nodes in the current component
        def dfs(node: int) -> None:
            visited.add(node)
            for neighbor in graph[node]:
                # Only recurse into unexplored neighbors to prevent infinite loops
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Check every potential node ID in the graph (0 to n-1)
        for i in range(n):
            # An unvisited node indicates an uncounted connected component
            if i not in visited:
                components += 1
                # Exhaustively explore all connected nodes in this component
                dfs(i)  
                
        return components