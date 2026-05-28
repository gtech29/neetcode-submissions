# Goal:
# traverse array, look at the current position i, count how many times the value at position i appears,
#  if frequency of i > 1 then return True, otherwise return False

# Input
# int arr nums = [1,2,3,4]

# Need:
# value at arr[i]
# frequency_map ={}
# store frequency of each item i
# if freq_map[i].values() > 1:
#       return True
# else: 
    # return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}
        for ch in nums:
            freq_map[ch] = freq_map.get(ch, 0) + 1

            for i in freq_map.values():
                if i > 1:
                    return True
        return False 