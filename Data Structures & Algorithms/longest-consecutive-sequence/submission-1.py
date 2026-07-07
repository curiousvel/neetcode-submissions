from typing import List

class Solution:
    """
    APPROACH: Intelligent Sequence Anchor Filtering (Hash Set Lookahead)
    
    Mental Pattern:
    1. To find the longest consecutive sequence in O(n) time, we must avoid re-processing 
       numbers that belong to the same sequence multiple times.
    2. We convert the array into a hash set to gain O(1) membership lookups.
    3. STRATEGY (Finding the Sequence Anchor): A number is the absolute start (anchor) of a 
       sequence if and only if (num - 1) does NOT exist in our set. 
    4. If (num - 1) exists, we skip it entirely because it will be naturally handled when 
       the loop hits its sequence anchor.
    5. Once an anchor is caught, we use a while loop to peek forward (num + length) to count 
       the continuous streak and update our global max.
       
    Symbolic Blueprint Trace (nums = [100, 4, 200, 1, 3, 2]):
    -----------------------------------------------------------------------------------------
    Val   | Anchor Check (val - 1 not in set?) | Action Taken / Streak Counts
    -----------------------------------------------------------------------------------------
    100   | 99 not in set? -> TRUE             | Anchor! Counts: 100 -> Streak = 1
    4     | 3 in set?     -> FALSE            | Skipped (part of a sequence starting lower)
    200   | 199 not in set?-> TRUE             | Anchor! Counts: 200 -> Streak = 1
    1     | 0 not in set?  -> TRUE             | Anchor! Counts: 1 -> 2 -> 3 -> 4 -> Streak = 4
    3     | 2 in set?     -> FALSE            | Skipped
    2     | 1 in set?     -> FALSE            | Skipped
    -----------------------------------------------------------------------------------------
    Max Streak Recorded = 4
    
    Complexity:
    - Time: O(n) where n is the length of the input array. Although there is a nested while loop, 
            each unique element is visited at most twice (once by the outer loop, and at most once 
            by the inner while loop across the entire runtime).
    - Space: O(n) to store the elements inside our hash set.
    """
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