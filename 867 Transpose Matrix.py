class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = []
        
        for column in range(len(matrix[0])):
            transpose.append([])
            
            for row in range(len(matrix)):
                transpose[column].append(matrix[row][column])
                
        return transpose