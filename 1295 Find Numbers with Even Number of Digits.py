class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for number in nums:
            if int(math.log10(number)+1) % 2 == 0:
                count=count+1
            
        return count