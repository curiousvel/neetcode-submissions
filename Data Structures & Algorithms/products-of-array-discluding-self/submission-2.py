# Symbolic mini-example: nums = [a, b, c, d]
# After prefix sweep (store left products): res = [1, a, a·b, a·b·c]
# Postfix sweep supplies right products to multiply: right-products = [b·c·d, c·d, d, 1]
# Final res = [b·c·d, a·c·d, a·b·d, a·b·c] — exactly each product excluding its own element.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # MENTAL MODEL:
        # We use two independent passes (Left-to-Right, then Right-to-Left).
        # In each pass, the boundary element starts by multiplying by 1.
        # This ignores its own value and perfectly satisfies the "except self" rule.
        
        # Pass 1: Left-to-Right (Prefix)
        prefix = 1
        for i in range(n):
            # Apply current prefix, then absorb nums[i] for the next position
            res[i] *= prefix
            prefix *= nums[i]

        # Pass 2: Right-to-Left (Postfix)
        postfix = 1
        for i in range(n - 1, -1, -1):
            # Multiply existing prefix result by current postfix, then absorb nums[i]
            res[i] *= postfix
            postfix *= nums[i]

        return res