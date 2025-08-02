class Solution(object):
    def maxProfit(self, prices):
        """
        Calculate the maximum profit by making as many transactions
        as needed, buying and selling on every profitable opportunity.

        Greedy approach: sum up all price increases between consecutive days.

        Parameters
        ----------
        prices : List[int]

        Returns
        -------
        int
            Maximum profit from unlimited transactions.
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:               # If price increases
                profit += prices[i] - prices[i - 1]     # Sell and take the profit

        return profit
