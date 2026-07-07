from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty hash set to keep track of the unique numbers 
        # we have encountered so far.
        hashset = set()

        # Iterate through every number in the input list.
        for n in nums:
            # Check if the current number already exists in our set.
            # In Python, lookups in a hash set take O(1) time on average.
            if n in hashset:
                return True  # A duplicate is found immediately.
            
            # If it's a new number, add it to the set so we remember it.
            hashset.add(n)
        
        # If the loop completes without hitting the 'return True' statement,
        # it means all numbers in the list are unique.
        return False