from typing import List

class Solution:
    """
    Problem: Number of Islands
    
    ============================================================================
    ALGORITHM: Grid-Scanning & Flood Fill (DFS) 🌊
    ============================================================================
    We systematically scan a 2D grid row-by-row and column-by-column. The process 
    operates via two coordinated phases:
    
    1. The Global Scanner (Nested For-Loops):
       We search for unvisited land ('1'). When found, it means we have discovered
       the starting boundary of a brand-new island, so we increment our counter.
       
    2. The Flood Fill (DFS Helper):
       Once a piece of land is found, we immediately trigger a Depth-First Search. 
       The DFS explores all 4 cardinal directions (Up, Down, Left, Right). 
       
       To avoid an infinite loop or double-counting, we change each visited '1' 
       to '0' (water) on the fly. This effectively "sinks" the entire connected 
       island before returning control back to our global scanner.
       
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(M * N) -> Where M is the number of rows and N is columns. 
      Every cell is visited a constant number of times by the loops and DFS.
      
    - Space Complexity: O(M * N) -> In the worst case (the entire grid is land), 
      the recursion stack depth can grow to the size of the entire grid.
    ============================================================================
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # If the grid is completely empty, there are no islands to count
        if not grid:
            return 0
            
        # m = total rows, n = total columns in the grid
        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            # BASE CASE / STOPPING CONDITION:
            # If we step outside the grid boundaries, OR if the cell we are on 
            # is water ('0') or already visited, stop and turn back.
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            
            # TRACKING VISITED: 
            # Change '1' to '0' immediately. This marks it as "visited" so 
            # future recursive calls don't process it again and cause an infinite loop.
            grid[i][j] = '0'
            
            # EXPLORATION:
            # Look in all 4 directions from the current cell to find and "sink" 
            # the rest of this connected piece of land.
            dfs(i, j + 1) # Look Right
            dfs(i, j - 1) # Look Left
            dfs(i + 1, j) # Look Down
            dfs(i - 1, j) # Look Up      

        # SCAN PHASE: Go through every single row (i) and column (j) one by one
        for i in range(m):
            for j in range(n):
                # If we encounter a '1', it is the start of a completely new island
                if grid[i][j] == '1': 
                    islands += 1      # Record that we found an island
                    dfs(i, j)         # Call DFS to completely clear/sink this island
                    
        return islands # Return the grand total of islands found