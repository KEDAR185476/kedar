class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        max_length = 0

        # Find longest strictly increasing subarray
        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                # Extend subarray if next element is larger
                if nums[pos] > nums[pos - 1]:
                    curr_length += 1
                else:
                    # Break if sequence is not increasing anymore
                    break
            max_length = max(max_length, curr_length)

        # Find longest strictly decreasing subarray
        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                # Extend subarray if next element is smaller
                if nums[pos] < nums[pos - 1]:
                    curr_length += 1
                else:
                    # Break if sequence is not decreasing anymore
                    break
            max_length = max(max_length, curr_length)

        return max_length  # Return the longer of increasing or decreasing sequencesclass Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        # Buying separately is cheaper; item 3 is unnecessary
        if cost1 + cost2 <= costBoth:
            totalCost = cost1 * need1 + cost2 * need2
        else:
            # Buy item 3 first until one requirement is fulfilled
            cnt_3 = min(need1, need2)
            totalCost = cnt_3 * costBoth

            need1 -= cnt_3
            need2 -= cnt_3

            # Type 1 is still needed; choose the cheaper of items 1 and 3
            if need1 > 0:
                totalCost += need1 * min(cost1, costBoth)

            # Type 2 is still needed; choose the cheaper of items 2 and 3
            elif need2 > 0:
                totalCost += need2 * min(cost2, costBoth)

        return totalCost
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
