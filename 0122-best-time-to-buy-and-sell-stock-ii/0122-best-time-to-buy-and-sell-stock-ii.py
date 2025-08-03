class Solution(object):
    def maxProfit(self, prices):
        """
        Calculate the maximum profit by making unlimited transactions
        (buy/sell) where you can buy and sell on the same day.

        Greedy strategy: Add up every price increase between consecutive days.

        Parameters
        ----------
        prices : List[int]

        Returns
        -------
        int
            Maximum profit from all allowed transactions.
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]  # Buy at i-1, sell at i

        return profit
