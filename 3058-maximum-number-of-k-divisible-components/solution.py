class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.components = 0

        def dfs(node: int, parent: int) -> int:
            sub = values[node]
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_sum = dfs(nei, node)
                sub += child_sum

            if sub % k == 0:
                self.components += 1
                return 0

            return sub % k

        dfs(0, -1)
        return self.components

