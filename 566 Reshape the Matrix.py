class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c == len(mat)*len(mat[0]):
            reshaped_matrix = []
            for i in range(r):
                reshaped_matrix.append([])
                
            temp = []
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    temp.append(mat[i][j])
                    
            for i in range(r):
                for j in range(c):
                    reshaped_matrix[i].append(temp.pop(0))
                    
            return reshaped_matrix
            
        
        return mat