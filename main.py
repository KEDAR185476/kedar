class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def quickselect(a, k):
            while True:class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))  # already a heap: each free server is keyed by its next turn

        handled, busy = [], []  # busy: (time it frees up, server)
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:  # done by time t
                heappush(free, i + (heappop(busy)[1] - i) % k)  # its first turn from i on
            if free:  # otherwise the request is dropped
                x = heappop(free) % k
                heappush(busy, (t + d, x))
                handled.append(x)

        return multimode(handled)
                if len(a) <= 1:
                    return a[0]
                p = random.choice(a)
                lo = [x for x in a if x < p]
                if k < len(lo):
                    a = lo
                    continue
                hi = [x for x in a if x > p]
                if k >= len(a) - len(hi):
                    k -= len(a) - len(hi)
                    a = hi
                    continue
                return p  # pivot sits at position k

        med = quickselect(nums, len(nums) // 2)
        return sum(abs(x - med) for x in nums)nyvygjvjvKiiy
8class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                reachable = dp[j] | (dp[j - 1] if j > 0 else set())

                dp[j] = {k ^ value for k in reachable}

        return min(dp[-1])wvjbks,
