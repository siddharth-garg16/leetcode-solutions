class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        #---method1---
        # for i in range(len(nums)):
        #     if len(str(nums[i]))%2==0:
        #         count+=1
        # return count


        #---method2---
        for num in nums:
            if int(math.log10(num))%2==1:
                count+=1
                
        return count