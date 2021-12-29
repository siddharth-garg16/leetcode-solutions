class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        start=max(nums)
        end=sum(nums)
        
        while start<end:
            middle=start+(end-start)//2
            total=0
            parts=1
            
            for num in nums:
                if(total+num>middle):
                    total=num
                    parts=parts+1
                else:
                    total=total+num
                    
            if parts>m:
                start=middle+1
            else:
                end=middle
        
        return end