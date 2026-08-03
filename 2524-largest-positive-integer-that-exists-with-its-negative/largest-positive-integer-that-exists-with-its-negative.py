class Solution(object):
    def findMaxK(self, nums):
        ans=-1
        n=set(nums)
        for i in n:
            if i>0 and -i in n:
                ans=max(ans,i) 
        return ans