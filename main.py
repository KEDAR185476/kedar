class Solution {

    private int segmentCost(char[] s, int l, int m, List<Integer>[] factors) {
        int best = m;
        for (int d : factors[m]) {
            int groups = m / d; // Each group contains groups characters
            int changes = 0;
            for (int offset = 0; offset < d; offset++) {
                for (int t = 0; t < groups / 2; t++) {
                    // Pair characters from opposite ends of the group
                    if (
                        s[l + offset + t * d] !=
                        s[l + offset + (groups - 1 - t) * d]
                    ) {
                        changes++;
                    }
                }
            }
            best = Math.min(best, changes);
        }
        return best;
    }

    private int solve(int seg, int start, int n, int[][] cost, int[][] memo) {
        if (seg == 1) {
            // Only one segment remains
            return cost[start][n - 1];
        }
        if (memo[seg][start] != -1) {
            // Already computed
            return memo[seg][start];
        }
        int best = n;
        int limit = n - 1 - 2 * (seg - 1); // Leave room for seg-1 segments after the first segment
        for (int e = start + 1; e <= limit; e++) {
            best = Math.min(
                best,
                cost[start][e] + solve(seg - 1, e + 1, n, cost, memo)
            );
        }
        memo[seg][start] = best;
        return best;
    }

    public int minimumChanges(String s, int k) {
        int n = s.length();
        char[] ch = s.toCharArray();
        List<Integer>[] factors = new ArrayList[n + 1];
        Arrays.setAll(factors, x -> new ArrayList<>());
        // Precompute the proper divisors of each number
        for (int d = 1; d <= n / 2; d++) {
            for (int m = d * 2; m <= n; m += d) {
                factors[m].add(d);
            }
        }
        int[][] cost = new int[n][n];
        for (int l = 0; l + 1 < n; l++) {
            for (int r = l + 1; r < n; r++) {
                // Each substring must have length at least 2
                cost[l][r] = segmentCost(ch, l, r - l + 1, factors);
            }
        }
        int[][] memo = new int[k + 1][n];
        for (int seg = 0; seg <= k; seg++) {
            Arrays.fill(memo[seg], -1);
        }
        return solve(k, 0, n, cost, memo);
    }
}class Solution {
class Solution {

    public String digitSum(String s, int k) {
        while (s.length() > k) {
            StringBuilder tmp = new StringBuilder(); // The string after each round
            int n = s.length();
            for (int i = 0; i < n; i += k) {
                int val = 0;
                for (int j = i; j < Math.min(i + k, n); ++j) {
                    val += s.charAt(j) - '0';
                }
                tmp.append(val);
            }
            s = tmp.toString();
        }
        return s;
    }
}
    public String digitSum(String s, int k) {
        while (s.length() > k) {
            StringBuilder tmp = new StringBuilder(); // The string after each round
            int n = s.length();
            for (int i = 0; i < n; i += k) {
                int val = 0;
                for (int j = i; j < Math.min(i + k, n); ++j) {
                    val += s.charAt(j) - '0';
                }
                tmp.append(val);
            }
            s = tmp.toString();
        }
        return s;
    }
}
class Solution {
    public int numOfSubarrays(int[] arr) {
        Arrays.parallelPrefix(arr, Integer::sum);  // arr becomes its own prefix sums, in place
        long odd = Arrays.stream(arr).map(p -> p & 1).sum();  // odd prefix sums
        return (int) (odd * (arr.length + 1 - odd) % 1_000_000_007);  // the empty prefix is even
    }
}
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
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
