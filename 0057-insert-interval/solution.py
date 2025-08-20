class Solution(object):
    def insert(self, intervals, newInterval):
        """
        Approach: Add all intervals that end before newInterval starts.
                  Merge all that overlap newInterval.
                  Append the rest.

        Complexity: O(n) time, O(n) output space.
        """
        res = []
        i, n = 0, len(intervals)
        ns, ne = newInterval

        # 1) keep intervals strictly before newInterval
        while i < n and intervals[i][1] < ns:
            res.append(intervals[i])
            i += 1

        # 2) merge overlaps with newInterval
        while i < n and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1
        res.append([ns, ne])

        # 3) append the rest
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

