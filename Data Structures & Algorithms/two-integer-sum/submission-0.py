# the goal of this problem, is to look at an unsorted array of integers nums and then a target
# my job is to determine if nums[i] + nums[j] == target, if it does return i,j

# input
# nums = [3,4,5,6]
# target = 7

# approach
# two pointer technique because we can check if window  = target, if it does
# return the indices, otherwise increase the right.
# if you found no matches then increase the left and check again,
# once done if no match return None

# edge cases
# nums = [] -> return []
# len(nums) == 1 -> return nums

# test cases:
# nums = [1,2] target = 3 return [0,1]
# nums = [3,4,5,6], target = 7 return [0,1]



# Pseudocode:

# if not nums:
#   return []
# elif len(nums) == 1:
    # return nums

# left = nums[i]
# right = nums[i+j]
# for every item in nums:
    # if nums[i] + nums[j] == target:
    #   return target
    # else:
        # left +=1
# return None

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        elif len(nums) == 1:
            return nums
        
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums) ):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None





        