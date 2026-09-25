class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # 1. Traverse left to right along top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # 2. Traverse top to bottom along right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # 3. Traverse right to left along bottom row (if row exists)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # 4. Traverse bottom to top along left column (if column exists)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result