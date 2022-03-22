class Solution:
    def shipWithinDays(self, num: List[int], d: int) -> int:
        def isPossible(num,d,m):
            ws,c=0,1
            for i in range(len(num)):
                if ws+num[i]<=m:
                    ws+=num[i]
                else:
                    c+=1
                    if c>d or num[i]>m:
                        return False
                    ws=num[i]
            return True
        s,e,ans=0,sum(num),-1
        while s<=e:
            m=s+(e-s)//2
            if isPossible(num,d,m):
                ans=m
                e=m-1
            else:
                s=m+1
        return ans