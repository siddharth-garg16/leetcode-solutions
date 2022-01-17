class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        for row in range(n):
            for col in range(row, n):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
                
        for row in matrix:
            for i in range(0,n//2):
                row[i], row[n-i-1] = row[n-i-1], row[i]