from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r: int, c: int, visited: set):
            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Valid boundaries, not visited yet, and height is EQUAL or HIGHER (climbing uphill)
                if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, visited)

        # Step 1: Run DFS from Pacific borders (Top & Left)
        for c in range(cols):
            dfs(0, c, pacific_visited)         # Top border
        for r in range(rows):
            dfs(r, 0, pacific_visited)         # Left border

        # Step 2: Run DFS from Atlantic borders (Bottom & Right)
        for c in range(cols):
            dfs(rows - 1, c, atlantic_visited)  # Bottom border
        for r in range(rows):
            dfs(r, cols - 1, atlantic_visited)  # Right border

        # Step 3: Find intersection of cells reachable by both oceans
        return list(pacific_visited & atlantic_visited)

