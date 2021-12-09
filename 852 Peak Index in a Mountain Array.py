class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start=0
        end=len(arr)-1
        
        while start<=end:
            mid=start+(end-start)//2
            if arr[mid-1]>arr[mid]:
                end=mid-1
            elif arr[mid]<arr[mid+1]:
                    start=mid+1
            else:
                return mid