"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        ========================================================================
        MENTAL MODEL: The Chronological Timeline Sweep
        ========================================================================
        Imagine drawing all meeting intervals onto a physical timeline. 
        If you look at random meetings, finding overlaps is tedious because you 
        have to compare every single meeting to every other meeting (O(N^2)).
        
        By SORTING the meetings by their start times, you arrange them neatly 
        from left to right. Now, you only need to check if adjacent meetings overlap:
        
          Meeting 1: |--------| (ends at i1.end)
          Meeting 2:      |--------| (starts at i2.start)
                          ^
                          Conflict! Meeting 2 starts before Meeting 1 finishes.
                          (i2.start < i1.end)
        ========================================================================
        """
        # STEP 1: Sort meetings chronologically by their start times.
        # This simplifies the problem so we only need to compare adjacent elements.
        intervals.sort(key=lambda x: x.start)

        # STEP 2: Sweep through the timeline and check adjacent pairs.
        for i in range(1, len(intervals)):
            i1 = intervals[i-1] # The previous meeting
            i2 = intervals[i]   # The current meeting

            # STEP 3: Check for overlap.
            # If the current meeting starts before the previous one ends, 
            # there is a double-booking conflict.
            if i2.start < i1.end:
                return False

        # If we made it through the entire schedule without overlaps, we are good to go!
        return True
