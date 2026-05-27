class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, r=0, 1
        maxlen=1
        while r<len(s):
            while s[r] in s[l:r] and l<r:
                l+=1 
            maxlen=max(maxlen, r-l+1)
            r+=1
        return maxlen


        