from math import gcd
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = nums[0]
        for v in nums:
            g = gcd(g,v)
        return g==1