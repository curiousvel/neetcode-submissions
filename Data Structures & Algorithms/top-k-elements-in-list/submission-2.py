from collections import Counter
from typing import List

class Solution:
    """
    APPROACH: Optimized Bucket Sort (Frequency-to-Index Mapping)
    
    Mental Pattern:
    1. Instead of sorting elements by frequency (O(n log n)), we use an inverted 
       array where the array indices represent frequencies (Bucket Sort).
    2. We first count frequencies using a hash map (O(n)).
    3. We allocate an array of empty buckets of size len(nums) + 1. The maximum possible 
       frequency of any element is len(nums) (if all items are identical).
    4. We iterate through the frequency map and append each number to the bucket corresponding 
       to its frequency index (e.g., if '7' appears 3 times, it goes into bucket[3]).
    5. Finally, we traverse the buckets backward (from highest frequency to lowest) and 
       collect elements until we have exactly k numbers.
    
    Complexity:
    - Time: O(n) where n is the number of elements in the input list.
    - Space: O(n) to store the frequency map and the bucket list structure.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        my_count = Counter(nums)
    
        result = []

        # Bucket Sort: Use the frequency as the list index.
        # Size is len(nums) + 1 to safely handle the worst-case scenario 
        # where all elements are identical (frequency == len(nums)).
        tracking_list = [[] for _ in range(len(nums) + 1)]

        # Group numbers by their frequency
        for n, freq in my_count.items():
            tracking_list[freq].append(n)

        # Iterate backward from highest frequency to lowest
        for inner_list in reversed(tracking_list):
            needed = k - len(result)
            
            if needed <= 0:
                break
                
            # Collect up to 'needed' elements from the current bucket
            result.extend(inner_list[:needed])
            
        return result