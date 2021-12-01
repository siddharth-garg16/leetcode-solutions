class Solution(object):
    def search(self, arr, target):
        start = 0
        end = len(arr)-1
        
        while start<=end:
            middle=start+(end-start)//2
            
            if arr[middle]==target:
                return middle

            if arr[middle]<target:
                start=middle+1
            else:
                end=middle-1
        
        return -1