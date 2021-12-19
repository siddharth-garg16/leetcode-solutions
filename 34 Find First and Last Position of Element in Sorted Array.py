class Solution(object):
    def searchRange(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=self.binarySearch(arr, target, True)
        right=self.binarySearch(arr, target, False)
        
        return [left, right]
    
    def binarySearch(self, arr, target, leftSpace):
        start, end, index = 0, len(arr)-1, -1
        
        while start<=end:
            middle=start+(end-start)//2
            
            if arr[middle]<target:
                start=middle+1
            elif arr[middle]>target:
                end=middle-1
            else:
                index=middle
                if leftSpace:
                    end=middle-1
                else:
                    start=middle+1
                    
        return index