class Solution(object):
    def merge(self, intervals):
        """
        Approach: Sort by start; append or merge with the last range.
        Complexity: O(n log n) time for sort, O(n) space for output.
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        for s, e in intervals:
            if not merged or s > merged[-1][1]:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
        return merged

