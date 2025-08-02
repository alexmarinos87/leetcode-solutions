class Solution(object):
    def maxProfit(self, prices):
        """
        Find the maximum profit from one buy and one sell operation.

        Traverse the list once while keeping track of the minimum price
        seen so far and the maximum profit if sold today.

        Parameters
        ----------
        prices : List[int]

        Returns
        -------
        int
            The maximum profit possible. Return 0 if no profit is possible.
        """
        min_price = float('inf')  # Set to infinity initially
        max_profit = 0            # Track best profit seen

        for price in prices:
            if price < min_price:
                min_price = price  # Buy at the lowest price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)  # Update max profit if needed

        return max_profit
