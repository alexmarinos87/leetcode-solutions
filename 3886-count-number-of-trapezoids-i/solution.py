class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        inv2 = (MOD + 1) // 2  # modular inverse of 2 under MOD

        # Count how many points lie on each horizontal line (same y)
        y_counts = Counter(y for x, y in points)

        # a_y = C(cnt_y, 2) for each y, only if cnt_y >= 2
        sumA = 0      # sum of a_y
        sumA2 = 0     # sum of a_y^2
        for cnt in y_counts.values():
            if cnt >= 2:
                a = cnt * (cnt - 1) // 2   # number of point-pairs on this y
                a %= MOD
                sumA = (sumA + a) % MOD
                sumA2 = (sumA2 + a * a) % MOD

        # total = (sumA^2 - sumA2) / 2  (mod MOD)
        total = (sumA * sumA - sumA2) % MOD
        total = total * inv2 % MOD

        return total

