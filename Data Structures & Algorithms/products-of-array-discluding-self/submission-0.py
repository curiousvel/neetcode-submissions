class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_b = [None] * len(nums)
        product_a = [None] * len(nums)
        res = [None] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                product_b[i] = nums[i]
            else:
                product_b[i] = nums[i]*product_b[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                product_a[i] = nums[i]
            else:
                product_a[i] = nums[i]*product_a[i+1]
        
        for i in range(len(nums)):
            if i != 0 and i != len(nums) -1:
                res [i] = product_b[i-1] * product_a[i+1]
            elif i == 0:
                res[i] = product_a[i+1]
            elif i == len(nums) - 1:
                res[i] = product_b[i-1]

        return res