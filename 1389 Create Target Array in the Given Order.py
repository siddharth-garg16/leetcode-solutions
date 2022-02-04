class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        #---using in-built insert function---
        # target = []
        # for i in range(0, len(nums)):
        #     target.insert(index[i], nums[i])
            
        # return target


        #---using list slicing---
        target = []
        for i in range(0, len(nums)):
            if index[i] == len(target):
                target.append(nums[i])
            else:
                target =target[:index[i]] + [nums[i]] + target[index[i]:]
                
        return target
