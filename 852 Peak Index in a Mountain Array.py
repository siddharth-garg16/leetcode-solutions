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
            
            
 #solution 2------covers some edge cases
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr)-1
        
        while start<end:
            mid = (start+end)//2
            if arr[mid]<arr[mid+1]:
                start = mid+1
            else:
                end = mid
                
        return start
