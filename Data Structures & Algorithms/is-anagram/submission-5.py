# Need:
# hashmap, compare against t if anagram then return true otherwise return false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        fm_s = {}
        fm_t = {}
        for c in range(len(s)):
            fm_s[s[c]] = fm_s.get(s[c], 0) + 1           
            fm_t[t[c]] = fm_t.get(t[c], 0) + 1
        return fm_s == fm_t
        