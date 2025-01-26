def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')  # Initialize with a very high value
    max_profit = 0

    for price in prices:
        # Update the minimum price so far
        if price < min_price:
            min_price = price
        # Calculate the profit if sold at current price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5
