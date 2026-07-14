class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        # A standard 32-bit integer has a fixed length of 32 bits
        length = 32 
        
        for i in range(length):
            # 1. Grab the rightmost bit of n
            bit = n & 1
            
            # 2. Shift that bit to its reversed position and merge it into result
            result = result | (bit << (32 - 1 - i))
            
            # 3. Shift n to the right to process the next bit
            n = n >> 1

        return result

