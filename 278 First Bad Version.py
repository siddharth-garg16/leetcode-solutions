class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        
        while start < end:
            middle = (start+end)//2
            
            if isBadVersion(middle):
                end = middle
            else:
                start = middle + 1
                
        return start