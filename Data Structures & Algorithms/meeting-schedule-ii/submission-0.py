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
    MENTAL MODEL: The Subway Turnstile 🚇
    ============================================================================
    Instead of tracking entire "meeting blocks" [start, end], we treat start times 
    and end times as completely independent events sorted chronologically. We then 
    sweep through time from left to right, comparing the next arrival against 
    the next departure.
    
    We evaluate our timeline using two distinct cases:
    
    - CASE 1 (Arrival first): starts[start_ptr] < ends[end_ptr]
      A new meeting starts BEFORE the oldest active meeting ends.
      -> Action: Allocate a brand new room (used_rooms + 1).
      
    - CASE 2 (Departure / Overlap first): (else block)
      The next chronological event is a meeting ending. This covers:
        A) GAP: A meeting ends completely before the next one even starts.
        B) OVERLAP: A meeting ends at the EXACT same time a new one starts.
      -> Action: Free up an existing room (used_rooms - 1).
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N log N) -> Sorting the starts/ends arrays takes O(N log N).
    - Space Complexity: O(N) -> To store sorted timelines of starts and ends.
    ============================================================================
    """
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0
        
        # Chronological split of arrivals and departures
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        start_ptr = 0
        end_ptr = 0
        
        used_rooms = 0
        max_rooms = 0
        
        while start_ptr < len(intervals):
            # CASE 1: A new meeting starts BEFORE the oldest active meeting ends.
            # We have no choice but to allocate a brand new room.
            if starts[start_ptr] < ends[end_ptr]:
                used_rooms += 1
                start_ptr += 1
                
            # CASE 2: The next chronological event is a meeting ending.
            else:
                # This covers two scenarios:
                #   A) An active meeting ends completely in the gap before the next one starts.
                #   B) An active meeting ends at the EXACT same time a new one starts (overlap).
                # In both scenarios, we free up the current room first.
                used_rooms -= 1
                end_ptr += 1
            
            # Record the peak room usage
            max_rooms = max(max_rooms, used_rooms)
            
        return max_rooms