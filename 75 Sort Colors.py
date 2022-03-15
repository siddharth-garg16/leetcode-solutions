class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #-------------solution 1--------------
        # zeroes = 0
        # ones = 0
        # twos = 0
        
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zeroes += 1
        #     elif nums[i] == 1:
        #         ones += 1
        #     else:
        #         twos += 1
                
        # for i in range(len(nums)):
        #     if zeroes > 0:
        #         nums[i] = 0
        #         zeroes -= 1
        #     elif ones > 0:
        #         nums[i] = 1
        #         ones -= 1
        #     else:
        #         nums[i] = 2
        #         twos -= 1

        #------------solution 2--------------
        left, right = 0, len(nums)-1
        i = 0
        
        while i <= right:
            if nums[i]==0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            if nums[i]==2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                i -= 1
            i += 1