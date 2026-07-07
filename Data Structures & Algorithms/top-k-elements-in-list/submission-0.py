class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_count = Counter(nums)

        heap = []

        for n, freq in my_count.items():
            heapq.heappush(heap, (freq, n))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]




        