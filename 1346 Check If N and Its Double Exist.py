class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #-----brute force solution--------
        N = len(arr)
        
        for i in range(N):
            for j in range(N):
                if (arr[i]*2 == arr[j]) and (i!=j):
                    return True
                
        return False


        #------optimised solution----------
        N = len(arr)
        bucket = []
        for i in range(N):
            if (arr[i]*2 in bucket) or (arr[i]/2 in bucket):
                return True
            else:
                bucket.append(arr[i])
                
        return False
        