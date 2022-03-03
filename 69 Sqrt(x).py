class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        start, end = 1, x
        
        while start<=end:
            middle = (start+end)//2
            if middle*middle == x:
                return middle
            elif middle*middle < x:
                start = middle + 1
                ans = middle
            else:
                end = middle - 1
                
        return ans