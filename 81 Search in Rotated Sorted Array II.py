class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[start]:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                start += 1

        return False