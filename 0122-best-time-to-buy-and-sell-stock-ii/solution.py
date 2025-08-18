class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Add profit whenever today's price is higher than yesterday's.
        Time: O(n), Space: O(1)
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        """
        You buy at any valley and sell at the next peak. But rather than explicitly finding valleys and peaks, the greedy trick is:
            if price[i] > prices[i - 1], just take the profit from that jump.
        Because:
            - You could have bought at price[i - 1]
            - You could have sold at price[i]
            - So the profit is price[i] - price [i - 1]
        This approach accumlates all upward movements - the total profit.
        """
