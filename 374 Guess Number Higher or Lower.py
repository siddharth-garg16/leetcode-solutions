class Solution:
    def guessNumber(self, n: int) -> int:
        start , end = 1, n
        
        while start <= end:
            middle = (start+end)//2
            
            if guess(middle) == 0:
                return middle
            
            if guess(middle) == 1:
                start = middle+1
            else:
                end = middle-1