# Breakdown problem:
    # look at array,
    # if any value in the array appears more than once, return true
    # otherwise return false

# Input
    # arr -> int or str? -> '1' or 1  or both? --> int for this example :)
    # if arr empty --> return arr

# Output
    # true, false or arr

# Middle part
    # we could brute force and iterate 1 by 1
    # and compare against a list to see if it has appeared yet
    # however, due to time complexity O(n^2) this doesn't seem good
    # another way could be to create a hashmap and then mark it with 1 that way 
    # we know that number is already in the map, that way if we see a 1 then we know that
    # number is already there if it is --> true otherwise --> false

# Pseudocode
    # check to see if we have a valid input
    #################################################
    # if not nums:
        # return nums
    # elif nums not isInstance(int):
        # return "array needs to be an integer array"
    #################################################
    # create the hashmap and mark one if the spot is empty
    #################################################
    # map = {}
    # for num in nums:
            # map[num] = map.get(num, 0) + 1
        #  if map[num] >= 1:
            # return true
    # return fals




class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1        
        
            if map[num] > 1:
                return True
        return False
        
        





