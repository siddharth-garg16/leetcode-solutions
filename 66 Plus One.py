class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        places = 10**(n-1)
        for i in range(n):
            num = num + digits[i]*places
            places = places//10
                
        num = num+1
        return list(str(num))