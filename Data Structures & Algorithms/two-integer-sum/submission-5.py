from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a hash map to map each visited number to its index.
        # Key: the number itself (int) -> Value: its index in the array (int)
        visited_nums = {}
        
        # Iterate through the list using enumerate to get both the index and the value.
        for current_index, current_num in enumerate(nums):
            # Calculate the required complement value that adds up to the target.
            complement = target - current_num
            
            # Check if this complement has already been seen in a previous iteration.
            # In Python, checking 'in' a dictionary takes O(1) time on average.
            if complement in visited_nums:
                # If found, return the index of the complement and the current index.
                # Because the complement was added earlier, visited_nums[complement] 
                # will always be the smaller index.
                return [visited_nums[complement], current_index]
            
            # If the complement isn't in the map, store the current number 
            # and its index for future lookups.
            visited_nums[current_num] = current_index
            
        # Return an empty list if no pair matches the target (per the problem constraints).
        return []