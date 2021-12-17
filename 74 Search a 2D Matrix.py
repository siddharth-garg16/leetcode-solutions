class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows=len(matrix)-1
        columns=len(matrix[0])-1
        def BS(row):
            start=0
            end=columns
            while start<=end:
                middle=start+(end-start)//2
                if matrix[row][middle]==target:
                    return True
                elif matrix[row][middle]<target:
                    start=middle+1
                else:
                    end=middle-1
            return False
        for row in range(0, rows+1):
            if BS(row):
                return True
        return False