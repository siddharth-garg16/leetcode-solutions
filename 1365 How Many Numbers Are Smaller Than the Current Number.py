class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #---double pointer method---
        # res = []

        # for i in range(0, len(nums)):
        #     count = 0
        #     for j in range(0, len(nums)):
        #         if nums[j] < nums[i]:
        #             count+=1
        #     res.append(count)
            
        # return res


        #bucket sort technique
        bucket = [0]*101
        for num in nums:
            bucket[num]+=1
        
        smaller_num_before = 0
        for i in range(0, len(bucket)):
            prev = bucket[i]
            bucket[i] = smaller_num_before
            smaller_num_before += prev
            
        return [bucket[num] for num in nums]
