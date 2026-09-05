"""
Solution for the "Longest Arithmetic Subarray with One Replacement" problem.
"""

class Solution:
    """Provides method to compute maximum length of arithmetic subarray."""

    # pylint: disable=invalid-name
    def longestArithmetic(self, nums):
        """
        Return the maximum length of an arithmetic subarray after at most one replacement.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        # Differences between consecutive elements
        diffs = [nums[i + 1] - nums[i] for i in range(n - 1)]

        # Compress consecutive equal differences into runs
        runs = self._compress_runs(diffs)

        max_len = self._max_single_run_len(runs, nums, n)
        max_len = max(max_len, self._max_connected_runs_len(runs, nums, n))

        return max_len

    @staticmethod
    def _compress_runs(diffs):
        """Compress consecutive equal differences into runs."""
        runs = []
        i = 0
        m = len(diffs)
        while i < m:
            j = i
            while j < m and diffs[j] == diffs[i]:
                j += 1
            runs.append((i, j - 1, diffs[i], j - i))
            i = j
        return runs

    @staticmethod
    def _max_single_run_len(runs, nums, n):
        """Compute maximum length considering only single runs."""
        max_len = 0
        for start_idx, end_idx, diff, run_len in runs:
            # 1) No replacement
            max_len = max(max_len, run_len + 1)

            # 2) Extend by one element on either side (replace the boundary element)
            if start_idx > 0:          # left extension
                max_len = max(max_len, run_len + 2)
            if end_idx < n - 2:        # right extension
                max_len = max(max_len, run_len + 2)

            # 3) Extend by two elements on one side (replace the middle element)
            # Left: elements at start_idx-2 and start_idx-1, replace start_idx-1
            if start_idx >= 2:
                if nums[start_idx] - nums[start_idx - 2] == 2 * diff:
                    max_len = max(max_len, run_len + 3)
            # Right: elements at end_idx+2 and end_idx+3, replace end_idx+2
            if end_idx + 3 < n:
                if nums[end_idx + 3] - nums[end_idx + 1] == 2 * diff:
                    max_len = max(max_len, run_len + 3)
        return max_len

    @staticmethod
    def _max_connected_runs_len(runs, nums, n):
        """Compute maximum length by connecting runs with the same diff across gaps."""
        max_len = 0
        num_runs = len(runs)

        for i in range(num_runs):
            _, end1, diff, len1 = runs[i]

            # Case 1: Gap consists of a single run of length 1
            if i + 2 < num_runs:
                mid_run = runs[i + 1]
                right_run = runs[i + 2]
                if right_run[2] == diff and mid_run[3] == 1:
                    len2 = right_run[3]
                    # Replace the single element that creates the gap
                    if nums[end1 + 2] - nums[end1] == 2 * diff:
                        max_len = max(max_len, len1 + len2 + 2)

            # Case 2: Gap consists of a single run of length 2
            if i + 2 < num_runs:
                mid_run = runs[i + 1]
                right_run = runs[i + 2]
                if right_run[2] == diff and mid_run[3] == 2:
                    len2 = right_run[3]
                    # Replace the middle element of the two-difference gap
                    if nums[end1 + 3] - nums[end1 + 1] == 2 * diff:
                        max_len = max(max_len, len1 + len2 + 3)

            # Case 3: Gap consists of two runs of length 1
            if i + 3 < num_runs:
                mid1 = runs[i + 1]
                mid2 = runs[i + 2]
                right_run = runs[i + 3]
                if right_run[2] == diff and mid1[3] == 1 and mid2[3] == 1:
                    len2 = right_run[3]
                    # Replace the element between the two single-difference runs
                    if nums[end1 + 3] - nums[end1 + 1] == 2 * diff:
                        max_len = max(max_len, len1 + len2 + 3)

        return max_len
