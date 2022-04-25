class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.append(i)
                    columns.append(j)
                    
        for r in rows:
            self.rowChange(matrix, r)
            
        for c in columns:
            self.columnChange(matrix, c)
                    
        
    def rowChange(self, mat, row):
        for i in range(len(mat[0])):
            mat[row][i]=0
    
    def columnChange(self, mat, col):
        for i in range(len(mat)):
            mat[i][col]=0