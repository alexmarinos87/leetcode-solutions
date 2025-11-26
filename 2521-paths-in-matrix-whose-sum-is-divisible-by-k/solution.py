class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # dp[i][j][r]
        # The number of paths to (i,j) whose path-sum modulo k equals r
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[j][r] = numbers of ways to reach cell in row currently processed
        # at column j with remainder r
        dp_prev = [[0] * k for _ in range(n)]

        # intialise first cell
        dp_prev[0][grid[0][0] % k] = 1

        # fill first row
        for j in range(1,n):
            val = grid[0][j]
            for r in range(k):
                if dp_prev[j-1][r] > 0:
                    dp_prev[j][ (r + val) % k ] = (dp_prev[j][(r + val) % k] + dp_prev[j-1][r]) % mod

        # Process remaining rows
        for i in range(1,m):
            dp_curr = [[0] * k for _ in range(n)]
            for j in range(n):
                val = grid[i][j]
                # From above
                for  r in range(k):
                    if dp_prev[j][r] > 0:
                        dp_curr[j][ (r + val) % k] = (dp_curr[j][(r + val) % k] + dp_prev[j][r]) % mod
                    # From left
                    if j > 0:
                        if dp_curr[j-1][r] > 0:
                            dp_curr[j][ (r + val) % k] = (dp_curr [j][(r + val) % k] + dp_curr[j-1][r]) % mod

            dp_prev = dp_curr # roll rows

        return dp_prev[-1][0]
