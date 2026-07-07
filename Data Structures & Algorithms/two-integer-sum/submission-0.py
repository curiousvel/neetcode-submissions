class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {} # value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i]
            else:
                hmap[n] = i
