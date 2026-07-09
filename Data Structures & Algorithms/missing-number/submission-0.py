class Solution:
    """
    APPROACH: Math / Gauss Summation
    
    Mental Pattern:
    1. A complete array of size n containing numbers from 0 to n has a predictable total sum.
    2. Use Gauss's formula (n * (n + 1)) // 2 to calculate this expected total in O(1) time.
    3. Iterate through the given array to calculate the actual sum of the elements present.
    4. The difference between the expected sum and the actual sum is the missing number.
    
    Complexity:
    - Time: O(n) because we iterate through the array of size n exactly once to sum it.
    - Space: O(1) as we only use a single variable to track the sum.
    """
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0;
        for num in nums:
            total += num;

        # Or just calculate total using sum method - sum(nums)

        return (n * (n + 1)) // 2 - total