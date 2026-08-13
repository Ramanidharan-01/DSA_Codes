# Problem: 3492. Maximum Containers on a Ship
# Runtime: 0 ms (Beats 100.00%)
# Memory: 19.4 MB (Beats 19.95%)

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n*n, maxWeight//w)