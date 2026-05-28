# Goal:
# Determine if the given string is a valid input,
# the string is valid iff
# - Every open bracket is closed by the same type of close bracket.
# - Open brackets are closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.
# If the string is determined to be valid then return True, otherwise we must return False

# Input:
# s= "([{}])" -> string

# Edge Cases:
# s = "" -> return ""
# s = 3 -> return not a string

# Test Cases:
# s = "[[" return False
# s = "[]" return True

# Approach
# -Initial Thoughts:
# it is very similar to checking a palindrome, we can compare if ( -> ) if it does we can add it onto the stack
# -we continue going once we are done we if everything matched then return True otherwise return False

# -Updated Approach:
# My initial approach was in the right track but a quick clarification, in a palindrome we check for symmetry,
# this problem is more about preserving order, therefore, it is suggested to explicitly create a map 
# tall tells the program what matches and what doesn't, 

class Solution:
    # Dry run
    def isValid(self, s: str) -> bool:
        brackets = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        stack = []

        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            elif ch in brackets.keys():
                if not stack:
                    return False
                elif stack[-1] == brackets[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

                
    



