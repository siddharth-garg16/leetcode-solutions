class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s = set()

        def binarySearch(l, r, ele):
            while l <= r:
                mid = (l + r) // 2
                if ele == nums[mid]:
                    return mid
                elif ele > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return 0

        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    x = target - (nums[i] + nums[j] + nums[k])
                    if binarySearch(k + 1, len(nums) - 1, x):
                        tmp = []
                        tmp.append(nums[i])
                        tmp.append(nums[j])
                        tmp.append(nums[k])
                        tmp.append(x)
                        s.add(tuple(tmp))
        for i in s:
            res.append(i)
        return res

    # res = []
    # n = len(nums)
    # nums.sort()
    #
    # for i in range(n - 3):
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #
    #     for j in range(i + 1, n - 2):
    #         if j > (i + 1) and nums[j] == nums[j - 1]:
    #             continue
    #
    #         reqSum = target - nums[i] - nums[j]
    #
    #         low = j + 1
    #         high = n - 1
    #
    #         while low < high:
    #             if (nums[low] + nums[high]) == reqSum:
    #                 res.append([nums[i], nums[j], nums[low], nums[high]])
    #                 while low < high and nums[low] == nums[low + 1]:
    #                     low += 1
    #                 while low < high and nums[high] == nums[high - 1]:
    #                     high -= 1
    #                 low += 1
    #                 high -= 1
    #             elif (nums[low] + nums[high]) < reqSum:
    #                 low += 1
    #             else:
    #                 high -= 1
    # return res