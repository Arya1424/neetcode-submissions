class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=nmax=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                n+=1
            else:
                nmax=max(n,nmax)
                n=1
        return max(n,nmax)
            
            


