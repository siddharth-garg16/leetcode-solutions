class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start , end = 1, num
        
        while start <= end:
            mid = (start+end)//2
            if mid*mid == num:
                return True
            if mid*mid < num:
                start = mid+1
            else:
                end = mid-1
                
        return False