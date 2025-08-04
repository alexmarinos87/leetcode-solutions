class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        Determine the starting gas station index from which you can travel
        around the circuit once, or return -1 if it's not possible.

        Strategy:
        - If total gas < total cost, return -1 immediately.
        - Otherwise, greedily find the starting index by tracking tank level.

        Parameters
        ----------
        gas : List[int]
        cost : List[int]

        Returns
        -------
        int
            Starting index of the valid station, or -1 if not possible.
        """
        total_gas = 0      # total gas gain - total cost (for global feasibility)
        tank = 0           # current gas in tank
        start = 0          # candidate starting index

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_gas += gain
            tank += gain

            # If tank goes negative, can't reach next station from `start`
            if tank < 0:
                start = i + 1  # try next station as start
                tank = 0       # reset tank for next start attempt

        return start if total_gas >= 0 else -1
