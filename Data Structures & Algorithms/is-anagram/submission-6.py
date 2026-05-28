# Core Concept: check if each element of string s = each elements of string t
# let s = "abba" we need to check if each element in s = to each element of t = "baab"
# if it does, then return True otherwise return False

# By definition, a property of an anagram is that order does not matter,
# in this use case we are focusing on frequency,
# since we lose track of count of items when using a set. using a hashmap data structure can prove helpful in this case. 

# My aproach:
    # Sanity check:
        # - ensure both strings are valid inputs meaning they are not empty and they are actually strings
        # - check for length of s and t if lengths are not equal to each other then,
        #       they can never be an anagram.

    # Algorithm:
        # create one dictionary that will hold the frequency of each item in s
        # then the map would look like {a:2,b:2} then the second hash table would look like {a:2,b:2} 
        # then we just compare each maps values and if they match we return True

# Pseudocode:
    # Sanity Checks:
    # valid_string = isinstance(s, str)
    # if not valid_string or not isinstance(t, str) :
        # return False
    # elif not s or not t:
        # return False
    # elif s.length != t.length:
        # return False
    
    # s1 = {}
    # t1 = {}
    # for r in s:
        # if i not in s1:
            # s1 = s1.get(i,0) + 1
    # for u in t:
        # if u not in t1:
            # t1 = t1.get(i,0) + 1
    # if s1.values() == t1.values():
        # return True
    # else:
        # return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid_input = isinstance(s, str)
        if not valid_input or not isinstance(t, str) or not s or not t or len(s) != len(t) :
            return False
        
        s1 = {}
        t1 = {}
        for r in s:
            s1[r] = s1.get(r,0) + 1
        
        for u in t:
            t1[u] = t1.get(u,0) + 1
        
        if s1 == t1:
            return True
        return False


        