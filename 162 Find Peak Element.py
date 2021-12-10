class Solution(object):
    def findPeakElement(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(arr)==1: return 0
        
        start=0
        end=len(arr)-1
        
        while start<end:
            mid=start+(end-start)//2
            
            if arr[mid]>arr[mid+1]:
                end=mid
            else:
                start=mid+1
                
        return start