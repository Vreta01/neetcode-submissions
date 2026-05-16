class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')] += 1
            count = tuple(count)
            if count in counts:
                counts[count].append(word)
            else:
                counts[count] = [word]
        return list(counts.values())