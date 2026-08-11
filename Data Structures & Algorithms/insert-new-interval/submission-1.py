"""
Problem: Insert Interval (LeetCode 57)

High-Level Idea:
1. Linear Pass (3-Phase Sweep): Process non-overlapping and overlapping intervals 
   in a single left-to-right pass.
2. Phase 1 (Before): Append all intervals that end before `newInterval` starts 
   (`intervals[i][1] < newInterval[0]`).
3. Phase 2 (Merge): Merge all overlapping intervals (`intervals[i][0] <= newInterval[1]`) 
   by expanding `newInterval` bounds: min start and max end.
4. Append the updated `newInterval` to `res`.
5. Phase 3 (After): Append all remaining intervals that start after `newInterval` ends.

Complexity:
- Time: O(N) — Single linear pass through the intervals list.
- Space: O(N) — Memory used to store the output result list `res`.
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # Phase 1: Add all intervals that come strictly BEFORE newInterval
        # (Current interval ends before newInterval begins)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Phase 2: Merge all OVERLAPPING intervals with newInterval
        # (Current interval starts on or before newInterval ends)
        # Note: We know intervals[i][1] >= newInterval[0] because Phase 1 already 
        # filtered out all intervals ending strictly before newInterval[0]. 
        # Thus, checking intervals[i][0] <= newInterval[1] is sufficient to confirm     overlap.
        while i < n and intervals[i][0] <= newInterval[1]:
            # Expand newInterval bounds to encompass the overlap
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Append the fully merged newInterval
        res.append(newInterval)

        # Phase 3: Add all remaining intervals that come strictly AFTER newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res