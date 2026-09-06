"""
Solution for maximizing total value with decay.
"""

class Solution(object):
    """
    Solves the max total value problem.
    """

    def maxTotalValue(self, value, decay, m):
        """
        Returns maximum total value modulo 1e9+7.
        :type value: List[int]
        :type decay: List[int]
        :type m: int
        :rtype: int
        """
        mod = 10**9 + 7
        total_pos, total_pos_sum = self._total_positive(value, decay)

        if m >= total_pos:
            return total_pos_sum % mod

        # Binary search for threshold value X
        low, high = 1, max(value)
        threshold_value = 1
        while low <= high:
            mid = (low + high) // 2
            cnt = self._count_ge(value, decay, mid, m)
            if cnt >= m:
                threshold_value = mid
                low = mid + 1
            else:
                high = mid - 1

        # Sum all gains strictly greater than threshold_value
        cnt_gt, sum_gt = self._sum_gt(value, decay, threshold_value + 1)
        remaining = m - cnt_gt
        total = sum_gt + remaining * threshold_value
        return total % mod

    @staticmethod
    def _total_positive(value, decay):
        """
        Returns (count, sum) of all positive gains.
        """
        total_pos = 0
        total_pos_sum = 0
        for v, d in zip(value, decay):
            t = (v + d - 1) // d
            total_pos += t
            total_pos_sum += t * v - d * t * (t - 1) // 2
        return total_pos, total_pos_sum

    @staticmethod
    def _count_ge(value, decay, threshold, max_count=None):
        """
        Counts selections with gain >= threshold, with optional early exit
        when count reaches max_count.
        """
        cnt = 0
        for v, d in zip(value, decay):
            if v >= threshold:
                cnt += (v - threshold) // d + 1
                if max_count is not None and cnt >= max_count:
                    return cnt
        return cnt

    @staticmethod
    def _sum_gt(value, decay, limit):
        """
        Returns (count, sum) of gains >= limit (i.e., strictly greater than
        threshold_value).
        """
        cnt_gt = 0
        sum_gt = 0
        for v, d in zip(value, decay):
            if v >= limit:
                t = (v - limit) // d + 1
                cnt_gt += t
                sum_gt += t * v - d * t * (t - 1) // 2
        return cnt_gt, sum_gt
