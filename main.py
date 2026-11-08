class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def quickselect(a, k):
            while True:
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
