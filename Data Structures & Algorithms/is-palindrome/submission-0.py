import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = s.lower()
        res = re.sub(r'[^a-zA-Z0-9]', '', n)
        l= 0
        r = len(res) - 1

        while l < r:
            if res[l] == res[r]:
                l += 1
                r -= 1
            elif res[l] != res[r]:
                return False
        return True
            


        