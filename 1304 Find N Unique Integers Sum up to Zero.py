class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [-1, 1]
        
        res = []
        
        if n%2==0:
            for i in range(n//2):
                res.append(-(i+1))
                res.append(i+1)
        else:
            for i in range(n//2):
                res.append(-(i+1))
                res.append(i+1)
            res.append(0)
        
        return res
        