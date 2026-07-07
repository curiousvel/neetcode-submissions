class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        # ====================================================================
        # STRUCTURE A: Bit-by-Bit Approaches (Methods 1 & 2)
        # Loops up to 32 times (or 64 times) depending on the integer bit-width.
        # ====================================================================
        while n:
            # --- Method 1: Bitwise Masking ---
            # Isolates the last bit using a bitwise AND.
            if n & 1:
                count += 1
            
            # --- Method 2: Modulo Arithmetic Logic ---
            # In base-2, checking 'n % 2' returns the remainder when dividing by 2.
            # This mathematically extracts the rightmost binary digit (0 or 1).
            # Examples: 13 % 2 = 1 (Binary 1101) | 12 % 2 = 0 (Binary 1100).
            # count += n % 2

            # Shift right by 1 to inspect the next bit (equivalent to n //= 2)
            n = n >> 1
            
        return count


    def hammingWeightMethod3(self, n: int) -> int:
        count = 0
        
        # ====================================================================
        # STRUCTURE B: Brian Kernighan's Algorithm (Method 3)
        # Time Complexity: O(k), where k is ONLY the number of set bits (1s).
        # ====================================================================
        while n:
            # --- Method 3: Subtract-and-Mask Bit Clearing ---
            # Subtracting 1 flips all bits from the right up to the first '1'.
            # ANDing 'n' with 'n - 1' completely clears that lowest set bit to 0.
            # Example: 
            #   n     = 12 (1100)
            #   n - 1 = 11 (1011)
            #   n & (n - 1) -> (1100 & 1011) = 8 (1000) <-- A single '1' is gone!
            
            n = n & (n - 1)
            
            # Since we successfully erased exactly one '1', increment the count.
            count += 1
            
            # (No bit-shifting 'n >> 1' is needed here, as n drops to 0 much faster!)
            
        return count