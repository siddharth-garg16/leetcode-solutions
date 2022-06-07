class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #brute force solution
        #         n = len(nums)
        #         counts = []

        #         for i in range(n-1):
        #             count = 0
        #             for j in range(i+1, n):
        #                 if nums[i]>nums[j]:
        #                     count += 1
        #             counts.append(count)
        #         counts.append(0)

        #         return counts

        righties = []
        l = len(nums)
        res = [0] * l
        for i in range(l - 1, -1, -1):
            res[i] = bisect.bisect_left(righties, nums[i])
            bisect.insort_left(righties, nums[i])
        return res