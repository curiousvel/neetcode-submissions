class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        The fundamental logic behind rotating an n x n 2D matrix 90 degrees clockwise in-place relies on a two-step geometric transformation: Transpose the matrix, then Reverse each row.

        Original Matrix:
        1 2 3
        4 5 6
        7 8 9

        Step 1: Transpose (swap along diagonal)
        1 4 7
        2 5 8
        3 6 9

        Step 2: Reverse Each Row (Final Result)
        7 4 1
        8 5 2
        9 6 3

        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        # or just do
        # for i in range(n):
        #   matrix[i].reverse()