class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return all(i in t for i in s)
        return sorted(s) == sorted(t)
        