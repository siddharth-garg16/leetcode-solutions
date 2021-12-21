class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new = []
        
        for i in range(0, n):
            new.append(nums[i])
            new.append(nums[i+n])
        
        return new