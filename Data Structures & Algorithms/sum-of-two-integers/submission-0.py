class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        ========================================================================
        MENTAL MODEL: The Hardware Half-Adder Circuit
        ========================================================================
        Think of adding two numbers like doing manual addition, but in binary:
        
          1. XOR (^) is "Addition without carrying":
             It adds the bits, but if both are 1, it resets to 0 (1 ^ 1 = 0).
             
          2. AND (&) shifted left (<< 1) is "The Carry-over":
             It identifies where both bits are 1 (which generates a carry),
             and shifts that carry over to the next column on the left.
             
        We repeat this cycle until there are no carries left (b == 0).
        ## CPP Solution:
        int getSum(int a, int b) {
            while (b != 0) {
                int carry = (a & b) << 1;
                a = a ^ b;
                b = carry;
            }
            return a;
        }
        ========================================================================
        """
        # Mask to keep numbers within 32-bit bounds (0xffffffff is 32 ones in binary)
        mask = 0xFFFFFFFF
        
        while b:
            # STEP 1: Calculate the carry bits and shift them left.
            # Mask both 'a' and 'b' to simulate 32-bit hardware overflow.
            carry = ((a & b) & mask) << 1
            
            # STEP 2: Add 'a' and 'b' without carrying.
            a = (a ^ b) & mask
            
            # STEP 3: Set 'b' to the carry. The loop continues to add the carries back in.
            b = carry
            
        # STEP 4: Python handling for negative numbers.
        # If the 32nd bit is 1, the number is negative in 32-bit two's complement.
        # This line converts the 32-bit unsigned representation back to a Python signed int.
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)