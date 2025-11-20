class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        #1. sort intervals by end
        intervals.sort(key=lambda x: (x[1], -x[0]))

        #2 keep track of chosen numbers
        ans = 0
        mx = -1 # largest chosen number so far
        secondmax = -1 # second largest chosen number so far


        #3 for each interval
        for start, end in intervals:
            # case a: both mx and secondmax are within the interval
            if mx >= start and secondmax >= start:
                continue
            # case b: only mx is inside
            if mx >= start:
                secondmax = mx
                mx = end
                ans += 1
            else:
            # neither is inside add two points end -1 and end
                    secondmax = end -1
                    mx = end
                    ans += 2
        return ans
