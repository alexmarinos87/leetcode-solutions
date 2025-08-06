class Solution(object):
    def trap(self, height):
        """
        Calculate how much water can be trapped after raining given an elevation map.

        Strategy:
        - Use two pointers (left, right) to traverse the array from both ends.
        - Keep track of the maximum bar seen so far from both sides (left_max, right_max).
        - Water trapped at each position depends on the smaller of the two maximums.

        Parameters
        ----------
        height : List[int]
            Non-negative integers representing the elevation map.

        Returns
        -------
        int
            Total units of trapped rain water.
        """
        n = len(height)
        if n == 0:
            return 0

        left, right = 0, n - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
