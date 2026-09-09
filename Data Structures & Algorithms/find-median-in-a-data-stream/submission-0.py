class MedianFinder:

    def __init__(self):
        # Max-heap for the smaller half (store negated values to simulate max-heap in Python)
        self.small = []
        # Min-heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Add to max-heap (small half)
        heapq.heappush(self.small, -num)
        
        # Step 2: Order Invariant Check (max of small <= min of large)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Step 3: Size Invariant Check (small can exceed large by at most 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)     # Popped actual value (e.g., 2)
            heapq.heappush(self.small, -val)    # Negated once to store in max-heap (e.g., -2)

    def findMedian(self) -> float:
        # Edge case check for empty data stream
        if not self.small:
            raise IndexError("findMedian called on empty data stream")

        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0