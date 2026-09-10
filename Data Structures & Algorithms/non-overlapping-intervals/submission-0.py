class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort by end time to prioritize finishing early
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = float('-inf')

        # Step 2: Greedy selection pass
        for start, end in intervals:
            # If current interval starts after or at the previous end time, keep it
            if start >= prev_end:
                prev_end = end
            else:
                # Overlap detected: discard this interval
                removals += 1

        return removals