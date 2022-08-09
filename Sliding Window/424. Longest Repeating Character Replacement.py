class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count =  Counter()
        maxCount = 0
        answer = 0
        l = 0 
        
        for r,char in enumerate(s):
            
            count[char] += 1
            
            maxCount = max(maxCount, count[char])
            
            while maxCount + k < r -l + 1:
                count[s[l]] -= 1
                l += 1
            answer = max(answer, r- l + 1)
        return answer  
