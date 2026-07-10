class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []
    
        def backtrack(index, current_subset):
            # BASE CASE: If we've made a decision for every number, we're done!
            if index == len(nums):
                results.append(list(current_subset)) # Save a snapshot copy
                return
            
            # CHOICE 1: INCLUDE the current number (The "Yes" Branch)
            current_subset.append(nums[index])       # Choose
            backtrack(index + 1, current_subset)     # Explore down this path
            
            # CHOICE 2: EXCLUDE the current number (The "No" Branch)
            current_subset.pop()                     # Unchoose (backtrack!)
            backtrack(index + 1, current_subset)     # Explore the other path
            
        backtrack(0, [])

        return results