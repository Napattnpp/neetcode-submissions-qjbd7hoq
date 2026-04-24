class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i (index) = day
        # price[i] = price of coin at ith day

        # i --> i+1 --> i+2 as index grow
        # price can increase or decrease

        # Buy at low pricec, then sell at high price

        sI, fI, max_profit = 0, 0, 0
        while True:
            if fI > len(prices)-1:
                break

            buy = prices[sI]
            sell = prices[fI]

            if buy > sell:
                sI = fI
            elif buy < sell:
                profit = sell - buy
                max_profit = max(profit, max_profit)
            fI += 1

        return max_profit
