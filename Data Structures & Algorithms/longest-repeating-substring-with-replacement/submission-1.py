class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        answer = 0
        max_count = ['',0]

        for i in range(len(s)):
            window[s[i]] = window.get(s[i],0) + 1
            if window[s[i]] > max_count[1]:
                max_count[0] = s[i]
                max_count[1] = window[s[i]]
            
            while i - left + 1 > k + max_count[1]:
                window[s[left]] -= 1
                left += 1
            answer = max(answer, i-left + 1)
        return answer
        
