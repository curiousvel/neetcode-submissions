class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        # Loop continues as long as 'n' has any set bits (1s) remaining.
        # Once all 1s are shifted out, 'n' becomes 0, and the loop terminates.
        while n:
            # Mask the number with 1 to isolate the lowest-order (rightmost) bit.
            # Example: 1101 & 0001 results in 0001 (True).
            # Example: 1100 & 0001 results in 0000 (False).
            if n & 1:
                count += 1
            
            # Shift bits to the right by 1 position to inspect the next bit.
            # This discards the bit we just checked and effectively performs n // 2.
            n = n >> 1
        
        return count