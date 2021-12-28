class Solution(object):
    def missingNumber(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        N=len(arr)
        supposed_sum = N*(N+1)//2
        actual_sum=0
        for i in range(N):
            actual_sum = actual_sum + arr[i]
            
        return (supposed_sum - actual_sum)