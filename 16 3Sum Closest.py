class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    ans = s
                if s < target:
                    left += 1
                else:
                    right -= 1

        return ans