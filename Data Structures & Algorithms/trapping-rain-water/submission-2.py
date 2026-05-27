class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        l, r=0, len(height)-1
        left, right=height[l], height[r]
        water=0
        while l<r:
            if left<right:
                l+=1
                left=max(left, height[l])
                water+=left-height[l]
            else:
                r-=1
                right=max(right, height[r])
                water+=right-height[r]
        return water
            
            

        