class Solution(object):
    def findMinArrowShots(self, points):
        """
        Minimum Number of Arrows to Burst Balloons (LeetCode 452)

        Approach
        --------
        Greedy by earliest end (O(n log n)):
        - Sort intervals by xend ascending.
        - Shoot one arrow at the end of the first interval.
        - For each next interval [s, e], if s > current_arrow_x, it can't be
          burst by the current arrow → shoot a new arrow at e and update current.
          Otherwise, it's already covered.

        Parameters
        ----------
        points : List[List[int]]
            Each element is [xstart, xend], xstart < xend.

        Returns
        -------
        int
            Minimum number of vertical arrows needed to burst all balloons.
        """
        if not points:
            return 0

        points.sort(key=lambda p: p[1])  # sort by end
        arrows = 0
        curr_end = None

        for s, e in points:
            if curr_end is None or s > curr_end:
                arrows += 1
                curr_end = e  # place arrow at the current interval's end

        return arrows

