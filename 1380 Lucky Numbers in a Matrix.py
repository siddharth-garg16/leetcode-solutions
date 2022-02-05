class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        result = []
        
        mins = []
        for rows in matrix:
            mins.append(min(rows))
            
        for columns in range(n):
            max = 0
            for rows in range(m):
                if matrix[rows][columns]>max:
                    max = matrix[rows][columns]
            if max in mins:
                result.append(max)
                
        return result