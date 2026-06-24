#Best Time to Buy and Sell Stock

def bsStocks(prices):
    if not prices:
        return 0
        
    min_price = prices[0]
    max_profit = 0  # FIX: Start profit record at 0
    
    for current_price in prices:
        # 1. Calculate potential profit based on the lowest price seen *so far*
        profit = current_price - min_price
        
        # 2. Update our max profit if this is a new record
        if profit > max_profit:
            max_profit = profit
            
        # 3. Update our lowest valley if we find a cheaper price to buy at
        if current_price < min_price:
            min_price = current_price
            
    return max_profit

# Test it out!
print(bsStocks([7, 1, 5, 3, 6, 4])) # Output: 5 (Buy at 1, Sell at 6)
print(bsStocks([7, 6, 4, 3, 1]))    # Output: 0 (Prices only drop, no profit possible)




def msss(nums,target):
    left = 0
    current_sum = 0
    # Initialize min_length to infinity so any real window length will be smaller
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
           # Calculate the length of the current valid window
            current_window_length = right - left + 1
            
            # Update our record if this window is shorter than what we've seen before
            if current_window_length < min_length:
                min_length = current_window_length
            # Shrink phase: subtract the leftmost element and move the pointer
            current_sum -= nums[left]
            left += 1
            
    # If min_length never changed, it means no valid subarray was found
    return min_length if min_length != float('inf') else 0

print(msss([2, 3, 1, 2, 4, 3], 7)) # Output: 2 (The subarray is [4, 3])