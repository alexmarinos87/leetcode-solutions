class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        Greedy reset on negative tank.
        If total(gas) < total(cost) -> -1; else a unique start exists.
        Time: O(n), Space: O(1)
        """
        total = 0 # sum of all (gas[i] - cost[i])
        tank = 0 # running tank since current start
        start = 0 # candidate start index
        
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            tank += gain
            if tank < 0:
                # Can't reach i+1 from current start, move start to i+1
                start = i + 1
                tank = 0
        
        return start if total >= 0 else  -1

        """
        Explanation:
        - Scan diff[i] = gas[i] - cost[i].
        - If your running sum (tank) ever dips below  0 at i, no index from the previous start up to i can be a valid start, because they all fail before (or at) i.
        - Reset to i+1 and continue. If the global total is negative, you can't finish from anywhere. 
        """