# This problems involves checking for repetition, therefore at this time 
# we are not interested maintaining any sort of order or checking any frequency

# a data structure that proves helpful is a HashSet, since this data structure
# helps us lookup items in O(1) TC

# a brute force approach could be using 2 pointers and comparing one pointer to
# another pointer, but we would have to do this n times for n items causins O(n^2) TC and SC of O(1)
# since we are not creating new data structure we are just working on 1 data structure

# My approach is as follows:
    # Sanity checks (edge cases):
        # - check if array is empty --if-so--> return False
    # Algorithm:
        # - Initialize and assign an empty set() to a variable
        # - for every number in the array:
                # - if that number exists in the set then return True, because we have seen it
                # - if it is not on the set then add it to the set
            #  return False because you didn''t find a repeating number

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

        