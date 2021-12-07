class Solution(object):
    def peakElementIndex(self, mountain_arr):
        start=0
        end=mountain_arr.length()-1
        
        while start<end:
            mid=start+(end-start)//2
            
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                start=mid+1
            else:
                end=mid
            
        return start
            
            
    def orderAgnosticBS(self, mountain_arr, target, left, right):
        start=left
        end=right
        
        if mountain_arr.get(start)<mountain_arr.get(end):
            while start<=end:
                mid=start+(end-start)//2
                if target<mountain_arr.get(mid):
                    end=mid-1
                elif target>mountain_arr.get(mid):
                    start=mid+1
                else:
                    return mid
                
        else:
            while start<=end:
                mid=start+(end-start)//2
                if target>mountain_arr.get(mid):
                    end=mid-1
                elif target<mountain_arr.get(mid):
                    start=mid+1
                else:
                    return mid
                
        return -1
            
        
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        peakIndex=self.peakElementIndex(mountain_arr)
        
        leftSearch = self.orderAgnosticBS(mountain_arr, target, 0, peakIndex)
        rightSearch = self.orderAgnosticBS(mountain_arr, target, peakIndex, mountain_arr.length()-1)
        
        if leftSearch != -1:
            return leftSearch
        elif rightSearch != -1:
            return rightSearch
        elif mountain_arr.get(peakIndex)==target:
            return peakIndex
        else:
            return -1