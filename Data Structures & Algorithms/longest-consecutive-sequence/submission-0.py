class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Convert the list to a set. 
        # This removes duplicates and allows O(1) constant time lookups.
        my_set = set(nums)
        longest = 0

        # Step 2: Iterate through each number in the original list.
        for val in nums:
            # RATIONALE FOR THIS IF-STATEMENT:
            # We only want to start counting a consecutive sequence if 'val' 
            # is the ABSOLUTE START of that sequence. If 'val - 1' is in the set, 
            # then 'val' is in the middle of a sequence, and we skip it.
            if val - 1 not in my_set:
                length = 0
                
                # Step 3: Count how far the sequence goes.
                # Since 'val' is the start, check for val, val+1, val+2, etc.
                while val + length in my_set:
                    length += 1
                
                # Step 4: Update the global maximum length found so far.
                longest = max(length, longest)
                
        return longest