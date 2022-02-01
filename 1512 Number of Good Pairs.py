class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # --- double pointer method ---
        # good_pair_count = 0
        
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             good_pair_count+=1
                    
        # return good_pair_count

        #--- hashtable method (dictionary) ---
        good_pair_count = 0
        dct = {}
        for i in range(0, len(nums)):
            if nums[i] in dct:
                dct[nums[i]].append(i)
            else:
                dct[nums[i]] = [i]
                
        for key, values in dct.items():
            if len(values) >= 2:
                n = len(values)
                good_pair_count += n*(n-1)/2
                
        return int(good_pair_count)