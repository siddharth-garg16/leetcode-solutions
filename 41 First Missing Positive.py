class Solution(object):
    def firstMissingPositive(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(arr):
            correctIndex=arr[i]-1
            if arr[i]>0 and arr[i]<=len(arr) and arr[i]!=arr[correctIndex]:
                arr[i],arr[correctIndex]=arr[correctIndex],arr[i]
            else:
                i=i+1
                
        for i in range(len(arr)):
            if arr[i]!=i+1:
                return i+1
                
        return len(arr)+1