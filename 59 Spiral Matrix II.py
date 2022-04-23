class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = []
        for i in range(n):
            result.append([0]*n)
            
        top, left = 0, 0
        bottom, right = n, n
        num = 1
        
        while left<right and top<bottom:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            top += 1
            
            for i in range(top, bottom):
                result[i][right-1] = num
                num += 1
            right -= 1
            
            for i in range(right-1, left-1, -1):
                result[bottom-1][i] = num
                num += 1
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1):
                result[i][left] = num
                num += 1
            left += 1
            
        return result