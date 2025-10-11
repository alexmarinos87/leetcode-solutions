from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        damage = {num: num * count[num] for num in count}
        unique = sorted(damage.keys())
        n = len(unique)
        dp = [0] * n
        dp[0] = damage[unique[0]]

        # loop from second element onward
        for i in range (1,n):
            cur = unique[i]
            best_without_conflict = 0
            # look backwards for the last non conflicting number
            for j in range(i-1,-1,-1):
                if cur - unique[j] >= 3:
                    best_without_conflict = dp[j]
                    break
            dp[i] = max(dp[i-1], damage[cur] + best_without_conflict)
            
        return dp[-1]