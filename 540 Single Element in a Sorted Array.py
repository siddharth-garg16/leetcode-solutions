class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        
        start, end = 0, len(nums)-1
        last = len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            if (mid==0 and nums[mid]!=[mid+1]) or (mid==last and nums[mid]!=nums[mid-1]) or (nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
                return nums[mid]
            elif (mid%2==0 and nums[mid]==nums[mid-1]) or (mid%2==1 and nums[mid]==nums[mid+1]):
                end = mid-1
            else:
                start = mid+1