class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maxVal = nums[0]
        change = 2
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                change -= 1
            if change == 0:
                return nums[i + 1]

        return maxVal