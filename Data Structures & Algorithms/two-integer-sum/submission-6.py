class Solution:
    """
    APPROACH: Hash Map Complement Lookup (One-Pass)
    
    Mental Pattern:
    1. Instead of looking forward to find a matching pair (O(n^2)), we look backward 
       at numbers we have already seen.
    2. For the current number, we calculate its 'complement' (target - current_num).
    3. We check if this exact complement exists in our hash map of visited numbers (O(1)).
    4. If found, we have our pair! We return the complement's index and our current index.
    5. If not found, we store the current number and its index in the map and move forward.
    
    Complexity:
    - Time: O(n) where n is the length of the input array.
    - Space: O(n) to store up to n elements in the dictionary in the worst case.
    """
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