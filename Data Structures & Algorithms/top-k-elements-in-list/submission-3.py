from collections import Counter
from typing import List

class Solution:
    """
    APPROACH: Bucket Sort (Frequency-to-Index Mapping)
    
    MENTAL MODEL:
    Flip the script: Instead of sorting numbers by frequency O(N log N), map 
    frequencies directly to array indices O(N). The frequency *is* the index.

    VISUAL WORKFLOW:
    1. Count:   [3, 3, 3, 1]  ->  Counter: {3: 3, 1: 1}
    2. Bucket:  Index (freq)  0    1    2    3
                Buckets      []   [1]  []   [3]
    3. Collect: Read buckets backward (Index 3 -> 2 -> 1) until top 'k' collected.

    COMPLEXITY:
    - Time:  O(N) -> O(N) count + O(N) bucket placement + O(N) backward sweep.
    - Space: O(N) -> O(N) hash map + O(N) tracking list structure.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Map each unique element to its frequency
        my_count = Counter(nums)
        result = []

        # Step 2: Create dynamic buckets where array index = element frequency.
        # Length is len(nums) + 1 to account for 0-based indexing, ensuring
        # index len(nums) exists if all elements are identical.
        # Must use list comprehension so each bucket is an independent list [].
        tracking_list = [[] for _ in range(len(nums) + 1)]

        # Step 3: Populate buckets (multiple elements can share the same frequency)
        for num, freq in my_count.items():
            tracking_list[freq].append(num)

        # Step 4: Sweep backward from highest possible frequency to lowest.
        # reversed() yields an iterator in O(1) space, guaranteeing O(N) total runtime.
        for inner_list in reversed(tracking_list):
            needed = k - len(result)
            
            # Early exit once we have collected k elements
            if needed <= 0:
                break
                
            # Extend result with up to 'needed' elements from current bucket.
            # Note: If inner_list is empty ([]), [][:needed] safely yields [] 
            # and performs a no-op, automatically skipping empty buckets.
            result.extend(inner_list[:needed])
            
        return result