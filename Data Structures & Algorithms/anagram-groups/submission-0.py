# input
# strs = ["",""]
# determine if anagram:
# --build hashmap if two strings have
# the same number of characters then is an anagram
# will will append it to or res list and 
# return the list and sublist
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}
        for word in strs:
            key = "".join(sorted(word))
        
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())



