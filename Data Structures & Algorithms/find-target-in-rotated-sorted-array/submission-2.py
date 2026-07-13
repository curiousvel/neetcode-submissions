class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        🧠 MENTAL MODEL: The Sorted Half Anchor (Search in Rotated Sorted Array)
        
        A rotated sorted array is always split into one perfectly sorted half 
        and one shifted/inflected half. We use the sorted half as our "anchor" 
        because its boundary values (min and max) are predictable and trustworthy.
        
        If a target does not fit into the predictable floor and ceiling of the 
        sorted half, it is "outside the range," forcing us to jump to the other half.

        COMPLEXITY:
            - Time Complexity: O(log N)
              We cut the search space exactly in half during every single step 
              by checking boundary floors and ceilings.
            - Space Complexity: O(1)
              No extra space is used; we only track integer pointers ('left', 'mid', 'right').
        """

        left, right = 0, len(nums) - 1

        # RULE 1: Use `<=` because when left == right, we are down to a single 
        # remaining element. If that final element is the target, using `<` 
        # would exit early and miss it (e.g., a single-element list [5], target 5).
        while left <= right:
            mid = (left + right) // 2

            # CRITICAL CHECK: We evaluate nums[mid] immediately.
            # If this matches, we exit. If it doesn't match, we know with 100% 
            # certainty moving forward that target CANNOT equal nums[mid].
            if nums[mid] == target:
                return mid

            # RULE 2: Use `<=` because if the array has only two elements left, 
            # 'left' and 'mid' will point to the exact same index. 
            # Using `<` would make (3 < 3) False, causing us to look at the wrong half.
            if nums[left] <= nums[mid]:  # Left half is sequentially sorted
                
                # RULE 3A (INCLUSIVE): target >= nums[left] because we haven't 
                # evaluated the 'left' boundary yet; the target could be sitting there.
                #
                # RULE 3B (EXCLUSIVE): target < nums[mid] because we ALREADY checked 
                # if nums[mid] == target above. We know it's not equal, so we check strictly below it.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is safely bounded inside the left half
                else:
                    left = mid + 1   # Target is outside this range, check the right messy half
            
            else:  # Right half is sequentially sorted
                
                # RULE 4A (EXCLUSIVE): nums[mid] < target because we already know 
                # target isn't at 'mid'. We strictly check above it.
                #
                # RULE 4B (INCLUSIVE): target <= nums[right] because we haven't 
                # evaluated the 'right' boundary yet; the target could be sitting there.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is safely bounded inside the right half
                else:
                    right = mid - 1  # Target is outside this range, check the left messy half
        
        return -1