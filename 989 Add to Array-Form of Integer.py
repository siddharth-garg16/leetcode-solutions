class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(num)
        place = 10**(l-1)
        
        n = 0
        for i in range(l):
            n += num[i]*place
            place = place//10
        
        return [int(x) for x in str(n+k)]