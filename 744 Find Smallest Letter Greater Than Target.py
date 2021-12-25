class Solution(object):
    def nextGreatestLetter(self, arr, target):
        start=0
        end=len(arr)-1
        
        if arr[0]>target or arr[end]<=target:
            return arr[0]
    
        while start<=end:
            middle=start+(end-start)//2
            
            if arr[middle]<=target:
                start=middle+1
            else:
                end=middle-1
            
        return arr[start]