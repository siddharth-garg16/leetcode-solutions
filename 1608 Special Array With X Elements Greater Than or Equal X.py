class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        for i in range(max_num+1):
            count = 0
            for num in nums:
                if num >= i:
                    count += 1
            if count == i:
                return count
            
        return -1