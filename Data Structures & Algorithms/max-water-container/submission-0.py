class Solution:
    """
    APPROACH: Two Pointers (Greedy Shrinking)
    
    MENTAL MODEL:
    Start with the maximum width (outermost boundaries). To find a larger area
    as width decreases, we must greedy-search for a taller height by moving 
    the pointer at the shorter wall.
    
    VISUAL WORKFLOW:
    Width = right - left
    Height = min(heights[left], heights[right])
    Area = Width * Height

    COMPLEXITY:
    - Time:  O(N) -> Single pass with two pointers converging inward.
    - Space: O(1) -> Only uses two pointer variables and a max_area tracker.
    """
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            # 1. Width is the index distance
            width = right - left
            
            # 2. Height is bottlenecked by the shorter wall
            h = min(heights[left], heights[right])
            
            # 3. Calculate area & track max
            area = width * h
            max_area = max(max_area, area)

            # 4. Greedy Move: Eliminate the shorter wall
            # If both are equal, we can decrement either one
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area