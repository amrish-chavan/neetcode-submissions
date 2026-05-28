class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) == len(t):
            return sorted(s) == sorted(t)  
        else:
            return False