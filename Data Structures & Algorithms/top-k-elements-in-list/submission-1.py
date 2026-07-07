class Solution:
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