class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #------------solution 1--------
        # pre = []
        # post = []
        # result = []
        
        # product = 1
        
        # for i in range(len(nums)):
        #     pre.append(product)
        #     product = product*nums[i]
            
        # product = 1
            
        # for i in range(len(nums)-1,-1,-1):
        #     post.insert(0, product)
        #     product = product*nums[i]
            
        # for i in range(len(nums)):
        #     result.append(pre[i]*post[i])
            
        # return result


        #-----------solution 2 with non extra space of pre[] and post[]
        output = []
    
        pre = 1
        for i in range(len(nums)):
            output.append(pre)
            pre = pre*nums[i]
            
        post = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i]*post
            post = post*nums[i]
            
        return output