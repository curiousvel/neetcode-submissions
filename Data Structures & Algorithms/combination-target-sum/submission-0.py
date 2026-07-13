class Solution:
    """
    🧠 MENTAL MODEL: The Decision-Tree Fork (Stay or Skip)
    
    To find combinations that add up to a target without generating duplicate sets, 
    we treat each step like a fork in the road for the current element:
    
    1. THE "STAY" CHOICE (Left Branch): Take the current number, add it to our running 
       total, and STAY at the exact same index so we can potentially take it again.
    2. THE "SKIP" CHOICE (Right Branch): Do not take the current number (or stop taking it), 
       and move strictly to index + 1 to explore the remaining numbers.
       
    This ensures that once we finish exploring a number and skip past it, we never look 
    back at it, naturally keeping our combinations structurally unique.

    COMPLEXITY:
        - Time Complexity: O(2^T) -> Where T is the target divided by the minimum element value. 
          In the worst case, the tree splits into two choices at every level down to max depth T.
        - Space Complexity: O(T) -> The maximum depth of the recursion call stack, bounded by T.
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, current_solution = [], []

        def backtrack(index, total):
            # BASE CASE 1: Perfect Match! Save a copy of our current path.
            if total == target:
                result.append(current_solution.copy())
                return

            # BASE CASE 2: Overstretching or Out of Bounds. Dead end, turn back.
            if total > target or index >= len(nums):
                return

            # 🟢 BRANCH 1: "STAY" AND EXPLORE (Include the current element)
            current_solution.append(nums[index])
            
            # WHY WE ADD TO TOTAL: Because we just committed to including 'nums[index]' 
            # in our current solution array, we must add its value to our running 'total'
            # to bring us closer to the target sum. We pass the exact same 'index' 
            # down to let the next recursive call decide if it wants even more copies of it.
            backtrack(index, total + nums[index])
            
            # 🔴 CLEAN UP: Backtrack by popping the element out before trying the next branch.
            current_solution.pop()
            
            # 🔵 BRANCH 2: "SKIP" AND EXPLORE (Exclude the current element)
            # WHY WE DO NOT ADD TO TOTAL: Because we popped the element out, it is no longer 
            # part of this branch's solution path. Since we didn't keep the number, our running 
            # 'total' remains completely unchanged. We pass 'index + 1' to move on and test 
            # the next available numbers against this exact same total.
            backtrack(index + 1, total)

        backtrack(0, 0)
        return result