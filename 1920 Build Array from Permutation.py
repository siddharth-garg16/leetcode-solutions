class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0, n):
            nums[i] = nums[i] + (nums[nums[i]] % n) * n

        for i in range(0, n):
            nums[i] = nums[i] / n

        return nums