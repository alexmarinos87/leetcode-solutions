class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        Approach: Two pointers (start and end of the array); shrink the window from the side with the shorter height.
        Why it fits: We want to maximise area = min(height[l], height[r]) * (r - l).
        Invariants: l < r always; at each step, the current container is evaluated for area. We move the pointer pointing to the shorter height to potentially find a taller one.
        Correctness: Every pair (1, r) is considered such that only pairs that can beat the current max are retained. The area is maximised without skipping any potential maximum.
        Complexity: Time O(n), Space O(1), where n = number of lines (height array length).
        """
        l, r = 0, len(height) - 1 # initialise two pointers
        best = 0 # initiliase max area tracker
        while l < r: # iterate while within bounds
            h = min(height[l], height[r]) # height of the container
            best = max(best,h * (r - l)) # computation of width
            if height[l] < height[r]: # move the pointer from the shorter side
                l += 1 # try to find taller line on left
            else:
                r -= 1 # try to find taller line on right
        return best
        """
        Explanation:
        We compute the area using the shorter line and update the max area (best) if it's higher than previous. Then we move the pointer from the shorter side inward, looking for potentially better pairs.
        """