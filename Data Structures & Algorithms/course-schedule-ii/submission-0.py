from collections import defaultdict

class Solution:
    """
    PATTERN: Graph Cycle Detection & Topological Sort (3-State DFS)
    PROBLEM: Course Schedule II (LeetCode 210)
    
    ===========================================================================
    💡 HIGH-LEVEL IDEA:
    We use DFS to detect cycles and build a valid Topological Ordering.
    
    By building the graph as course -> prerequisites:
      - We recursively visit all prerequisites of a course first.
      - Once all prerequisites for a course are fully processed (VISITED), we 
        append the current node to 'res' (Post-Order Traversal).
      - This naturally orders prerequisites BEFORE dependent courses!
      
    If a cycle is detected at any point (encountering a VISITING node), an 
    ordering is impossible, so we return an empty list [].
    ===========================================================================
    
    COMPLEXITY:
    - Time:  O(V + E) -> Visited every course node (V) and edge (E) at most once.
    - Space: O(V + E) -> O(V + E) for adjacency list, O(V) state array & call stack.
    """
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []
        graph = defaultdict(list)

        # Build graph: course -> prerequisite
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # State definitions
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(node: int) -> bool:
            if states[node] == VISITED:
                return True
            if states[node] == VISITING:
                return False  # Cycle detected, impossible to complete

            # Mark active path
            states[node] = VISITING

            # Visit prerequisites first
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # Mark processed & append node after its prerequisites are done
            states[node] = VISITED
            res.append(node)
            return True

        # Process all courses (handles disconnected graphs)
        for node in range(numCourses):
            if not dfs(node):
                return []

        return res