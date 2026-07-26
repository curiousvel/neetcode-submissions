from collections import defaultdict

class Solution:
    """
    PATTERN: Graph Cycle Detection / Topological Sort (3-State DFS)
    PROBLEM: Course Schedule (LeetCode 207)
    
    ===========================================================================
    💡 HIGH-LEVEL IDEA:
    A valid course schedule is only possible if the prerequisite graph has 
    NO directed cycles (it forms a Directed Acyclic Graph / DAG). 
    
    We detect cycles by simulating traversal using 3-state graph coloring:
      - 0 (UNVISITED): Not explored yet.
      - 1 (VISITING) : Currently exploring on the active DFS path.
      - 2 (VISITED)  : Fully explored and verified to be cycle-free.
      
    If DFS ever lands on a node marked 1 (VISITING), we've looped back onto 
    our active path—meaning a cycle exists and completion is impossible!
    ===========================================================================
    
    COMPLEXITY:
    - Time:  O(V + E) -> Touch every course node (V) and edge (E) at most once.
    - Space: O(V + E) -> O(V + E) for adjacency list, O(V) state array & call stack.
    """
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list: course -> list of dependencies
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # State definitions
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(node: int) -> bool:
            state = states[node]
            if state == VISITED:
                return True
            if state == VISITING:
                return False  # Cycle detected!

            # Mark node as actively being visited
            states[node] = VISITING

            # Recursively explore all neighbor nodes
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # Mark node as fully processed & safe
            states[node] = VISITED
            return True

        # Check every component (handles disconnected graphs)
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True