class Solution(object):
    def maxArea(self, height):
        """
        Compute the maximum water a container can store using two lines.

        Approach:
        - Two pointers: left at start, right at end.
        - Area is limited by the shorter line: width * min(height[left], height[right]).
        - Move the pointer at the shorter line inward to seek a taller boundary.
        - Track the maximum area seen.

        Parameters
        ----------
        height : List[int]
            Non-negative integers representing line heights.

        Returns
        -------
        int
            The maximum area achievable.
        """
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            best = max(best, h * width)

            # Strategically move the shorter side inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
