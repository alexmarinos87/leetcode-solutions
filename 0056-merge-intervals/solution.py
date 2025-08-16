class Solution(object):
    def merge(self, intervals):
        """
        Merge Intervals (LeetCode 56)

        Approach
        --------
        Sort + linear sweep (O(n log n)):
        - Sort intervals by start time.
        - Keep a current merged interval [cur_start, cur_end].
        - For each [s, e]:
          * If s <= cur_end, they overlap → extend cur_end = max(cur_end, e).
          * Otherwise, push [cur_start, cur_end] and start a new current interval.
        - Append the last current interval at the end.

        Parameters
        ----------
        intervals : List[List[int]]
            List of [start, end] pairs (order may be arbitrary).

        Returns
        -------
        List[List[int]]
            List of merged, non-overlapping intervals sorted by start.
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = []
        cur_start, cur_end = intervals[0][0], intervals[0][1]

        for s, e in intervals[1:]:
            if s <= cur_end:  # overlap
                if e > cur_end:
                    cur_end = e
            else:
                merged.append([cur_start, cur_end])
                cur_start, cur_end = s, e

        merged.append([cur_start, cur_end])
        return merged

