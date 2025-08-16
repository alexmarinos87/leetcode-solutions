class Solution(object):
    def insert(self, intervals, newInterval):
        """
        Insert Interval (LeetCode 57)

        Approach
        --------
        Linear scan (O(n)):
        - Add all intervals that end before newInterval starts.
        - Merge all intervals that overlap with newInterval by expanding its bounds.
        - Append the merged newInterval.
        - Append the remaining intervals.

        Parameters
        ----------
        intervals : List[List[int]]
            Non-overlapping intervals sorted by start.
        newInterval : List[int]
            Interval to insert.

        Returns
        -------
        List[List[int]]
            Intervals after insertion and merging, still sorted and non-overlapping.
        """
        res = []
        i = 0
        n = len(intervals)
        ns, ne = newInterval

        # 1) Add intervals ending before newInterval starts
        while i < n and intervals[i][1] < ns:
            res.append(intervals[i])
            i += 1

        # 2) Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1
        res.append([ns, ne])

        # 3) Append the rest
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

