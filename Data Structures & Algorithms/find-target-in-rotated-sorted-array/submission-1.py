class Solution:
    """
    🧠 MENTAL MODEL: The Sorted Half Anchor (Search in Rotated Sorted Array)
    
    A rotated sorted array is always split into one perfectly sorted half 
    and one shifted/inflected half. We use the sorted half as our "anchor" 
    because its boundary values (min and max) are predictable and trustworthy.
    
    If a target does not fit into the predictable floor and ceiling of the 
    sorted half, it is "outside the range," forcing us to jump to the other half.

    Example Array: [4, 5, 6, 7, 0, 1, 2]

    COMPLEXITY:
        - Time Complexity: O(log N)
          We cut the search space exactly in half during every single step 
          by checking boundary floors and ceilings.
        - Space Complexity: O(1)
          No extra space is used; we only track integer pointers ('left', 'mid', 'right').
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Immediate check: If this matches, we exit right away.
            # This guarantees that 'target' CANNOT equal 'nums[mid]' below.
            if nums[mid] == target:
                return mid

            # =================================================================
            # SIDE A: The LEFT half is our Clean Shelf 🟢
            # =================================================================
            if nums[left] <= nums[mid]:
                
                # Check the Clean Shelf boundaries:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 🟢 It's on this shelf! Stay here and search.
                else:
                    # 🔴 Not on the shelf! Dive into the Messy Right Zone.
                    left = mid + 1   
            
            # =================================================================
            # SIDE B: The RIGHT half is our Clean Shelf 🟢
            # =================================================================
            else:
                
                # Check the Clean Shelf boundaries:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 🟢 It's on this shelf! Stay here and search.
                else:
                   # 🔴 Not on the shelf! Dive into the Messy Left Zone.
                    right = mid - 1  
        
        return -1