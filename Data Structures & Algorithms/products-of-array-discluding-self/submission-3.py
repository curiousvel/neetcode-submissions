from typing import List

class Solution:
    """
    APPROACH: Two-Pass Accumulative Products (Prefix & Postfix Accumulation)
    
    Mental Pattern:
    1. Total Product Except Self = (Product of everything to Left) * (Product of everything to Right).
    2. We perform a Left-to-Right pass to calculate and store all left (prefix) products directly in 'res'.
    3. We perform a Right-to-Left pass to calculate right (postfix) products on the fly, multiplying them
       into the existing values inside 'res'.
       
    Symbolic Blueprint Matrix (nums = [a, b, c, d]):
    -----------------------------------------------------------------------------------------
    Index i           | 0            | 1            | 2            | 3            | Running Var
    -----------------------------------------------------------------------------------------
    Initial res       | 1            | 1            | 1            | 1            | -
    After Prefix Pass | 1            | a            | a·b          | a·b·c        | prefix loops: 1 -> a -> a·b -> a·b·c
    Postfix Multiplier| b·c·d        | c·d          | d            | 1            | postfix loops: 1 <- d <- c·d <- b·c·d
    -----------------------------------------------------------------------------------------
    Final res Value   | b·c·d        | a·c·d        | a·b·d        | a·b·c        | Complete!
    
    Complexity:
    - Time: O(n) where n is the length of the input array (two sequential linear passes).
    - Space: O(1) auxiliary space (the output array does not count toward space complexity).
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Pass 1: Left-to-Right (Prefix Construction)
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        # Pass 2: Right-to-Left (Postfix Integration)
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res