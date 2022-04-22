class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump, N, i = 0, len(nums)-1, 0
        
        while i < N and i <= maxjump:
            if maxjump >= N:
                break
            maxjump = max(maxjump, i+nums[i])
            i += 1
        return maxjump >= N