class Solution:
    """
    APPROACH: Binary Search on Inflection Point
    
    Mental Pattern:
    1. A rotated array splits into a Left (higher) and Right (lower) sorted portion.
    2. The target minimum element is the inflection point (the start of the Right Portion).
    3. Compare nums[mid] against nums[right] to determine which half is unsorted.
    4. If nums[mid] > nums[right], mid is in the Left Portion; the min is to the right.
    5. If nums[mid] <= nums[right], the right side is sorted; mid or a lower value is to the left.
    6. Use `left + (right - left) // 2` to calculate mid to prevent integer overflow.
    
    Complexity:
    - Time: O(log n) because the search space is divided in half each step.
    - Space: O(1) as it only uses a few pointer variables.
    """

# find the mid element
# if the mid > value then the min is on the the right side sorted array
# move the left to mid + 1 and continue
# if the mid value is <= right value, right = mid and continue
# when we reach the end the left will


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1
    
        # Notice it's < and not <= because we are shrinking the window 
        # until left and right converge on the single lowest element.
        while left < right:
            mid = (left + right) // 2 # or left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Minimum must be in the right unsorted part
                left = mid + 1
            else:
                # Minimum is either mid or to the left of mid
                right = mid
                
        # When left == right, they are both pointing at the minimum element
        return nums[left]