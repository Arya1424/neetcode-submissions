class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap=dict()
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in hmap:
                return [hmap[diff], i]
            hmap[nums[i]]=i
