class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        result=[]
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if len(substring) == len(set(substring)):
                    result.append(len(substring))
        return max(result)
