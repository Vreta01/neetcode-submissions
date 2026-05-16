class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(str(len(word)) + '#' + word)
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            word = s[i:i+length]
            output.append(word)
            i = i + length
        return output