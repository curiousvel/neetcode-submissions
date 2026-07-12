class Solution:
    """
    🧠 MENTAL MODEL: The Running Valley & Peak Tracker
    
    Instead of checking every single pair of buying and selling days (which takes O(N^2) time), 
    we travel through time from left to right, maintaining two simple running records:
    
    1. 'minPrice' (The Lowest Valley): The cheapest buy-in price we've seen so far.
    2. 'maxP' (The Maximum Profit): The biggest payout we could get by selling 
       the stock at the current price, assuming we bought it at our lowest valley.
    
    As we step forward:
    - If the current price is a new lowest valley, we update our 'minPrice'.
    - Otherwise, we calculate the profit if we sold today, and update 'maxP' 
      if this profit beats our historical record.
    
    Complexity:
        - Time: O(N) -> We loop through the array exactly once.
        - Space: O(1) -> We only track two floating numbers in memory.
    """
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxP = 0

        for price in prices:
            # 1. Update the lowest valley seen so far
            minPrice = min(minPrice, price)
            
            # 2. Calculate potential profit if sold today
            profit = price - minPrice
            
            # 3. Capture the maximum profit achieved across the timeline
            maxP = max(maxP, profit)

        return maxP

        