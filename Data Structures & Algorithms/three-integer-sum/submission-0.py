class Solution:
    """
    Problem: 3Sum (LeetCode 15)
    Approach: Sorting + Two Pointers
    
    ============================================================================
    INTERVIEW INTUITION:
    ============================================================================
    Fix the first number nums[i], then transform the rest of the problem into 
    2Sum using two pointers on a sorted array.
    
    To avoid duplicate triplets:
    1. Skip identical values for the fixed pivot nums[i].
    2. When a valid triplet is found, advance both pointers past duplicate 
       values before searching for the next sum.
      
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N^2)
      * Sorting takes O(N log N).
      * Outer loop runs O(N) times, and inner two-pointer search takes O(N) 
        per iteration -> O(N^2) overall.
        
    - Space Complexity: O(N) or O(1)
      * O(N) due to space required by Python's Timsort algorithm.
      * O(1) auxiliary space if we exclude sort space and the output list 'res'.
    ============================================================================
    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort to enable two pointers and duplicate skipping
        
        # Stop at len(nums) - 2 so at least 2 elements remain for 'left' and 'right'.
        # Since range() upper bound is exclusive:
        # Final indices will be i = n-3, left = n-2, right = n-1.
        for i in range(len(nums) - 2):
            
            # Optimization: In a sorted array, if the pivot > 0, three positive
            # numbers can never sum to 0. We can safely break early.
            if nums[i] > 0:
                break
                
            # Skip duplicate pivot elements to avoid identical triplet results
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 2: Set two pointers for the remaining sub-array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1   # Need a larger sum -> move left pointer rightward
                elif total > 0:
                    right -= 1  # Need a smaller sum -> move right pointer leftward
                else:
                    # Found a valid triplet!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Advance both pointers past current match
                    left += 1
                    right -= 1
                    
                    # Step 3: Skip duplicates by comparing against the elements 
                    # we just passed (left - 1 and right + 1)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res