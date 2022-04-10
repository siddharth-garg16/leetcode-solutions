class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        
        while start <= end:
            mid = (start+end)//2
            if mid*(mid+1)//2 == n:
                return mid
            if mid*(mid+1)//2 < n:
                start = mid+1
                ans = mid
            else:
                end = mid-1
        
        return ans