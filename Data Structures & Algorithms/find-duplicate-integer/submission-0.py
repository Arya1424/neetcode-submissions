class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            idx=abs(i)
            if nums[idx]<0:
                return idx
            else:
                nums[idx]=-nums[idx]
        return -1