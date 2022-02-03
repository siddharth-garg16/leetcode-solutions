class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        sums = 0

        for i in range(0, len(nums)):
            sums = sums + nums[i]
            running_sum.append(sums)

        return running_sum