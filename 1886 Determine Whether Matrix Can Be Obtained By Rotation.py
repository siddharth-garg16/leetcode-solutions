class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if self.same(mat, target):
            return True
        elif self.same(self.rotation(mat), target):
            return True
        elif self.same(self.rotation(self.rotation(mat)), target):
            return True
        elif self.same(self.rotation(self.rotation(self.rotation(mat))), target):
            return True
        else:
            return False
    
    def rotation(self, matrix):
        n = len(matrix[0])
        
        for row in range(n):
            for col in range(row, n):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
                
        for row in matrix:
            for i in range(0,n//2):
                row[i], row[n-i-1] = row[n-i-1], row[i]
                
        return matrix
    
    def same(self, mat, target):
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j]==target[i][j]:
                    continue
                else:
                    return False
                
        return True