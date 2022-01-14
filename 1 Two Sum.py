class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #--- T.C. of O(n^2) bad for large data--------
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]


        #----optimised solution------
        complements = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in complements.keys():
                return [i, complements[nums[i]]]
            else:
                complements[complement]=i