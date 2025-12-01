class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def can_run(T: int) -> bool:
            total = 0
            for b in batteries:
                total += min(b, T)
                # Small optimisation: early exit if already enough
                if total >= n * T:
                    return True
            return total >= n * T

        total_energy = sum(batteries)
        low, high = 0, total_energy // n # max possible minutes

        while low < high:
            mid = (low + high +1) // 2 # bias upward
            if can_run(mid):
                low = mid # mid is feasible try for more
            else:
                high = mid - 1 # mid not feasible go smaller

        return low
