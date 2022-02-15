class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        row = [0]*m
        column = [0]*n
        
        for idx in indices:
            row[idx[0]]+=1
            column[idx[1]]+=1
            
        return sum([1 for i in row for j in column if (i+j)%2])