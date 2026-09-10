class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # Step 1: Sort chronologically by start time
        intervals.sort(key=lambda x: x[0])

        merged = []

        # Step 2: Linear sweep
        for interval in intervals:
            # Local aliases to keep syntax clean
            # If merged is empty or no overlap, add current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap detected: expand the end boundary of the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged