class Solution(object):
    def findMinArrowShots(self, points):
        """
        Approach: Sort intervals by xend. Shoot one arrow at the end of the first interval.
                  For each next interval [s,e], if s <= shoot_pos, it's already burst;
                  otherwise we need a new arrow at e.

        Complexity: O(n log n) time for sorting, O(1) extra space (output excluded).
        """
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        arrows = 1
        shoot = points[0][1]
        for s, e in points[1:]:
            if s <= shoot:     # overlaps (inclusive) → same arrow works
                continue
            arrows += 1
            shoot = e          # place new arrow at this interval's end
        return arrows
