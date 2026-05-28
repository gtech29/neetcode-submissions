# Goal:
###
# determine the maximum profit that can be achieved by buy and selling neetcoin,
# I would choose to buy the coin on the day with the highest price 
# and sell on the day with the lowest price 
# a brute force attempt would be to iterate through n days and perform n operations
# we would need to track the max profit, then track the curr value do an operation and then 
# return the max profit, this causes O(n^2) TC
#  instead we could use a window approach,
# we could shrink the window if our subtraction is greater than the max profit, then when we are done
# return the max profit

# Input
# prices = [] -> int array
# price = the price of the neetcoin on the ith day

# Output
# return max_profit

# Need:
# look at the price of each day and determine if that is the highest price so far that the coin can be sold
# and also determine if thats the lowest price to buy

# max_profit = 0
# l = prices[0]
# r = prices[1:]
# 
# while prices: <-ths is out of bounds r needs to be less than prices
#  if prices[r] > prices[l]: <- remember left is your current day, right is what is ahead of you
#      max_profit = prices[r] - prices[l]
#                               <- how could we find the max between two numbers?
#  else:
#       l += prices[1:] <- l becomes r because cheaper price is always better
#       r += 1
# return max_profit
#   
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1
        return maxP

        