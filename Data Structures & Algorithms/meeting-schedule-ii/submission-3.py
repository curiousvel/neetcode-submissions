"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Definition for an Interval.
# class Interval:
#     def __init__(self, start=0, end=0):
#         self.start = start
#         self.end = end

class Solution:
    """
    Problem: Meeting Rooms II (LeetCode 253)
    
    ============================================================================
    MENTAL MODEL: Peak Watermark / Room Handover 🔑
    ============================================================================
    Instead of tracking individual meeting blocks [start, end], we treat start times 
    and end times as independent chronological events. We sweep from left to right,
    comparing the next starting meeting against the earliest ending meeting.
    
    We track the PEAK number of rooms needed ('max_rooms') across two cases:
    
    - CASE 1 (New Room Required): start[start_p] < end[end_p]
      A new meeting starts BEFORE the earliest active meeting finishes.
      -> Action: Allocate an additional physical room (max_rooms + 1).
      -> Advance start_p to process the next meeting.
      
    - CASE 2 (Immediate Room Handover): start[start_p] >= end[end_p]
      An active meeting ends BEFORE or at the EXACT same time the next meeting starts.
      -> Action: Hand over the vacated room directly to the new meeting (-1 + 1 = 0 net change).
      -> Net rooms needed stays UNCHANGED (max_rooms remains the same).
      -> Advance BOTH start_p and end_p simultaneously (one meeting finishes, one takes over).
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N log N) -> Sorting the start and end timelines takes O(N log N).
    - Space Complexity: O(N) -> To store the separate sorted arrays of start and end times.
    ============================================================================
    """
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        # Extract and sort start and end times independently to track events chronologically
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        start_p = end_p = 0
        max_rooms = 0

        # Sweep through all start events
        while start_p < len(intervals):
            # Case 1: Next meeting starts BEFORE the earliest ongoing meeting finishes
            if start[start_p] < end[end_p]:
                max_rooms += 1  # Allocate a new room (increases peak watermark)
                start_p += 1    # Move to process the next meeting start
            
            # Case 2: Room handover (-1 freed, +1 claimed = 0 net change to peak)
            else:
                start_p += 1    # New meeting claims the room
                end_p += 1      # Old meeting finishes, releasing its room

        return max_rooms