from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        MENTAL MODEL: The "Yes/No" Decision Tree
        ----------------------------------------
        Imagine you are packing a bag from a list of items. For every single item 
        at 'index', you face a strict binary choice:
        1. YES (Include): Put the item in the bag and move to the next item.
        2. NO  (Exclude): Take it out of the bag (the pop() step), and move to 
                          the next item without it.
                            
        By exploring both the "Yes" and "No" branches for every number until we 
        reach the end of the list, we guarantee we capture every possible subset.
        """
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