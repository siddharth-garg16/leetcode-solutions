class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        if letters[N-1]<=target:
            return letters[0]
        
        start, end = 0, N-1
        while start <= end:
            mid = (start+end)//2
            if letters[mid] > target:
                ans = letters[mid]
                end = mid-1
            else:
                start = mid+1
                
        return ans