class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for i in strs:
            count=[0]*26
            for ch in i:
                count[ord(ch)-ord('a')] +=1
            groups[tuple(count)].append(i)
        return list(groups.values())

        