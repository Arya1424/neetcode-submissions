class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1 for _ in range(len(nums))]
        prod=1
        for i in range(len(nums)):
            pre[i]*=prod
            prod*=nums[i]
        j=0
        prod=1
        for i in range(len(nums)-1, -1, -1):
            pre[i]*=prod
            prod*=nums[i]
        return pre

        