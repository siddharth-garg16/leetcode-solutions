class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        diag_sum = 0
        n = len(mat)
        for i in range(n):
            diag_sum += mat[i][i]
            diag_sum += mat[i][n-i-1]
                    
        return diag_sum if n%2==0 else diag_sum-mat[n//2][n//2]