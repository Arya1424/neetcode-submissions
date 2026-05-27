class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add the new char at the right of the window
            index = ord(s2[r]) - ord('a')
            if s1Count[index] == s2Count[index]:
                matches -= 1
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1

            # Remove the old char at the left of the window
            index = ord(s2[l]) - ord('a')
            if s1Count[index] == s2Count[index]:
                matches -= 1
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1

            l += 1

        return matches == 26
