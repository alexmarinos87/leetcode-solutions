class Solution(object):
    def hIndex(self, citations):
        """
        Calculate the h-index, which is the maximum h such that
        the researcher has published h papers that have each
        been cited at least h times.

        Strategy:
        - Sort the citations in descending order.
        - Find the maximum index `i` such that citations[i] >= i + 1.

        Parameters
        ----------
        citations : List[int]

        Returns
        -------
        int
            The h-index of the researcher.
        """
        citations.sort(reverse=True)  # Sort descending
        h = 0

        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break

        return h

