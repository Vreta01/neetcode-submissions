class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for word in strs:
            for char in word:
                output += (str(ord(char)))
                output += ' '
            output += ','
        return output

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        words = s.split(',')[:-1]
        output = []
        for word in words:
            value = ''
            chars = word.strip().split(' ')
            for char in chars:
                if char:
                    val = str(chr(int(char)))
                    value += val
            output.append(value)
        return output