#----brute force solution------------------------
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        neg_count = 0
        
        for rows in grid:
            if rows[n-1]>=0:
                continue
            else:
                neg_count += self.compute(rows)
                
        return neg_count
    
    def compute(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i]<0:
                count+=1
                
        return count


#-----optimised solution----------
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row_len = len(grid[0])
        col_len = len(grid)
        total = 0
        
        i, j = 0, row_len - 1
        
        while i < col_len and j >= 0:
            if grid[i][j] < 0:
                total += col_len - i
                j -= 1
            else:
                i += 1
                
        return total