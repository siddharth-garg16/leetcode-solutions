class Solution:
    #two pointer method
    # def findDuplicate(self, nums: List[int]) -> int:
    #
    #     slow = a[0]
    #     fast = a[a[0]]
    #
    #     while slow != fast:
    #         slow = a[slow]
    #         fast = a[a[fast]]
    #
    #     fast = 0
    #
    #     while slow != fast:
    #         slow = a[slow]
    #         fast = a[fast]
    #
    #     return slow


    #using sets
    # def findDuplicate(self, a: List[int]) -> int:
    #     s = set()
    #     for num in nums:
    #         if num in s:
    #             return num
    #         s.add(num)

    #sorting
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]