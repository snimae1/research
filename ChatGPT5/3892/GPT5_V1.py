class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        if k == 0:
            return 0

        # Maximum possible number of peaks in a cycle
        max_peaks = n // 2
        if k > max_peaks:
            return -1

        INF = 10 ** 18

        def solve(first_taken):
            """
            DP on the cycle by fixing whether index 0 is chosen as a peak.
            """
            # dp[i][prev_taken][cnt] = minimum cost after processing indices < i
            # prev_taken = whether i-1 is a peak
            dp = [[[INF] * (k + 1) for _ in range(2)] for __ in range(n + 1)]

            if first_taken:
                cost0 = max(0, max(nums[n - 1], nums[1]) + 1 - nums[0])
                dp[1][1][1] = cost0
            else:
                dp[1][0][0] = 0

            for i in range(1, n):
                for prev in range(2):
                    for cnt in range(k + 1):
                        cur = dp[i][prev][cnt]
                        if cur == INF:
                            continue

                        # Do not choose i
                        if cur < dp[i + 1][0][cnt]:
                            dp[i + 1][0][cnt] = cur

                        # Choose i as a peak
                        if cnt == k:
                            continue
                        if prev:
                            continue

                        # Adjacent to first peak?
                        if i == n - 1 and first_taken:
                            continue

                        left = nums[i - 1]
                        right = nums[(i + 1) % n]
                        need = max(left, right) + 1
                        cost = max(0, need - nums[i])

                        if cur + cost < dp[i + 1][1][cnt + 1]:
                            dp[i + 1][1][cnt + 1] = cur + cost

            ans = INF
            for last_taken in range(2):
                ans = min(ans, dp[n][last_taken][k])
            return ans

        ans = min(solve(False), solve(True))
        return -1 if ans == INF else ans
