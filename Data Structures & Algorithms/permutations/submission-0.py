class Solution:
    """
    🧠 MENTAL MODEL: The Decision Tree (State Space Search)
    
    Think of building a permutation like filling 'n' empty slots one by one.
    At each step, you stand before a pool of numbers and make a choice.
    
    1. CHOOSE:  Pick an available number (not already in your current path) and place it in the slot.
    2. EXPLORE: Walk down that path to fill the remaining slots recursively.
    3. UNCHOOSE (Backtrack): Pull the number back out of the slot so you can try 
                             a different number in that exact same position.
                             
    Visualizing the Choices for [1, 2, 3]:
                  [ ]
               /   |   \
            [1]   [2]   [3]    <- Choose 1st element
            / \   / \   / \
          [2] [3]...           <- Choose 2nd element (skipping duplicates)
          
    Complexity:
        - Time: O(N * N!) -> There are N! permutations, and copying/searching takes O(N).
        - Space: O(N) -> The recursion stack and 'sol' array only grow as deep as the input array.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Get the length of the input array
        n = len(nums)
        # 'ans' will store all complete permutations
        # 'sol' (solution) will store the current permutation being built
        ans, sol = [], []

        def backtrack():
            # Base case: If the current permutation 'sol' has 'n' elements,
            # it means a complete permutation has been found.
            if len(sol) == n:
                # Append a copy of 'sol' to 'ans'. Using sol[:] is crucial
                # to append a snapshot, not a reference, as 'sol' will change.
                ans.append(sol.copy())
                return # End this branch of recursion

            # Recursive step: Iterate through each number in the original 'nums' array
            for x in nums:
                # Pruning condition: If 'x' is not already in the current permutation 'sol',
                # then it's a valid candidate to be added.
                if x not in sol:
                    # Choose: Add 'x' to the current permutation
                    sol.append(x)
                    # Explore: Recursively call backtrack to build the rest of the permutation
                    backtrack()
                    # Unchoose (Backtrack): Remove 'x' from 'sol' to revert the choice
                    # and allow other elements to be chosen for this position.
                    sol.pop()

        # Start the backtracking process with an empty current permutation
        backtrack()
        # Return all collected permutations
        return ans