class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for key in c:
            if c[key]>1:
                return True
        return False