# return the indices i and j such that their sum == a target and i != j
# this means nums[i] + nums[j] == target 
# a brute force attempt:
# iterate perform a sum on each of the elements, 
#  if sum == target return indices, this causes 
# n operations on n items -> O(n^2)

# hasmap attempt:
# create 2 hashmap with nums[i], nums[j] as the key and i,j as the value
# then if any of the sum of the keys == target, return the values of those keys
# this can give us our indices
# at most this is O(n) since 1 operation on n items

# in order to simplify this process we can find its complement:
# Complement:
# the complement of a number a wrt number b is defined as b-a.
# the coomplement tells us what we need to add to a to reach b
# complement = target - n
# if the complement is in the dictionary
# then we return the value at that index, and its index
# otherwise if we havent seen it yet add it to the map and set its value to i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in map:
                return [map[comp], i]
            map[n] = i

 