from collections import Counter
from bisect import bisect_right
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Step 1: Count spell occurrences
        count = Counter(power)
        # Step 2: Calculate total damage per unique value
        damage = {num: num * count[num] for num in count}
        # Step 3: Sort unique damage values
        unique = sorted(damage.keys())
        n = len(unique)

        # Step 4: Dynamic programming table
        dp = [0] * n
        dp[0] = damage[unique[0]]

        # Step 5: Fill DP efficiently using binary search
        for i in range(1, n):
            cur = unique[i]
            # Find last index j with unique[j] <= cur - 3
            j = bisect_right(unique, cur - 3) - 1

            # If found, we can safely add dp[j]
            include_cur = damage[cur] + (dp[j] if j >= 0 else 0)
            # Or we skip this one
            dp[i] = max(dp[i - 1], include_cur)

        # Step 6: The final answer
        return dp[-1]

