from typing import List

def maxProfit(prices: List[int]) -> int:
    # Returns an empty arrray if prices is zero
    if not prices:
        return 0
    
    # Assign the max profit and the minimum price to two variables
    min_price = prices[0]
    max_profit = 0

    # Iterate through the array comparing the current price to the max and min values
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Example 1
print("Example 1")
prices = [7,1,5,3,6,4]
print(f"The max profit for {prices} is {maxProfit(prices)}")