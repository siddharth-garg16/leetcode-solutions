class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        total = rows*cols
        count, step, change_in_step = 1, 1, 1
        dir_idx = 0
        directions = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
        result = [[rStart, cStart]]
        
        while count < total:
            for i in range(step):
                rStart, cStart = rStart+directions[dir_idx][0], cStart+directions[dir_idx][1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                    count += 1
                    
            dir_idx = (dir_idx + 1) % 4
            if change_in_step % 2 == 0:
                step += 1
            change_in_step +=1
            
        return result