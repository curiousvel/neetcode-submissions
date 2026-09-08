class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        
        # 1. DEFINE & INITIALIZE STATE
        # dp[i] = length of LIS ending at index i.
        # Base case: Each number alone forms an increasing sequence of length 1.
        dp = [1] * n

        # 2. OUTER LOOP (Target boundary)
        # Evaluates every index i as the potential end of a sequence.
        for i in range(1, n):
            
            # 3. INNER LOOP (Historical Predecessors)
            # Scans all previous elements j to find valid candidates to extend.
            for j in range(i):
                
                # 4. TRANSITION CONDITION
                # Check if current element nums[i] can legally follow nums[j].
                if nums[i] > nums[j]:
                    # Recurrence relation: Take the best known sequence ending at j,
                    # add 1 for nums[i], and update dp[i] if it improves the max length.
                    dp[i] = max(dp[i], dp[j] + 1)

        # 5. EXTRACT GLOBAL ANSWER
        # The longest sequence can end at any index, so we return the max in dp.
        return max(dp)