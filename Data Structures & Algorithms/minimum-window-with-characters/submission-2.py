class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char,0) + 1
        have = 0
        answer = ''
        left = 0
        for i in range(len(s)):
            if s[i] in need:
                need[s[i]] -= 1
                if need[s[i]] == 0:
                    have += 1

            while have == len(need):
                if i-left+1 < len(answer) or len(answer) == 0:
                    answer = s[left:i+1]
                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        have -= 1
                left += 1
        return answer