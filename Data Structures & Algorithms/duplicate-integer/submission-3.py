class Solution:
    """
    APPROACH: Hash Set Lookup Tracking
    
    Mental Pattern:
    1. Duplicate detection requires remembering elements we have already encountered.
    2. We use a hash set to store elements as we traverse the list sequentially (O(n)).
    3. For every element, we perform an O(1) look ahead check against our hash set.
    4. If the item is already present, we have caught a duplicate early and return True.
    5. If the loop completes without a hit, all elements are uniquely distinct.
    
    Complexity:
    - Time: O(n) where n is the length of the input list.
    - Space: O(n) to store up to n elements in the hash set in the worst case.
    """
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