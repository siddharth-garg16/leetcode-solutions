class Solution(object):
    def findErrorNums(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        while i<len(arr):
            correctIndex=arr[i]-1
            if arr[i]!=arr[correctIndex]:
                arr[i],arr[correctIndex]=arr[correctIndex],arr[i]
            else:
                i=i+1
                
        for i in range(len(arr)):
            if arr[i]!=i+1:
                return [arr[i],i+1]