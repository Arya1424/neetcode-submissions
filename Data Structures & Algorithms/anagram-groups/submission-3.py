class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words=defaultdict(list)
        for i in strs:
            count=[0]*26
            for s in i:
                count[ord(s)-ord('a')]+=1
            words[tuple(count)].append(i)
        return list(words.values())

        