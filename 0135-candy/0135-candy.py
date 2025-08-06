class Solution(object):
    def candy(self, ratings):
        """
        Distribute candies to children such that:
        - Each child has at least one candy.
        - Children with a higher rating than their neighbors get more candies.

        Strategy:
        - Assign one candy to each child initially.
        - Left-to-right pass: If current rating > left neighbor, give one more candy than left.
        - Right-to-left pass: If current rating > right neighbor, ensure more candies than right.

        Parameters
        ----------
        ratings : List[int]
            List of integers representing ratings of each child.

        Returns
        -------
        int
            Minimum total candies needed to distribute.
        """
        n = len(ratings)
        candies = [1] * n  # Step 1: Every child gets at least 1 candy

        # Step 2: Left to right (check left neighbour)
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to left (check right neighbour)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
