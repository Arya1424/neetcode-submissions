class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in s:
                return [s[diff]+1,i+1]
            else:
                s[numbers[i]]=i