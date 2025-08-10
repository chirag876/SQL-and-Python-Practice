'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.'''


def maxstocksprofit(prices):
    maxprof = 0
    minprice = float('inf') # Start with a very large value
    
    for prc in prices:
        if prc <minprice: # Keep track of the minimum price seen so far
            minprice = prc
        profit = prc-minprice # Calculate profit if selling today
        
        if profit>maxprof: # Update max profit
          maxprof = profit
    return maxprof

prices = [7,1,5,3,6,4]
print("max profit:", maxstocksprofit(prices))