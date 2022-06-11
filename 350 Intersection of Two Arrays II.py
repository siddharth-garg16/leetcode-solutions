class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #-----solution using hashmap-----
        result = []
        hashmap = {}
        
        for val1 in nums1:
            if val1 in hashmap:
                hashmap[val1]+=1
            else:
                hashmap[val1]=1
                
        for val2 in nums2:
            if val2 in hashmap:
                if hashmap[val2]>0:
                    result.append(val2)
                    hashmap[val2]-=1
                    
        return result