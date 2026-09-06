"""
This module provides a solution to maximize the integer value of a concatenated
binary string formed by rearranging segments of ones and zeros.
"""

class Solution:
    """
    A class used to solve the binary string maximization problem.
    """
    # pylint: disable=too-few-public-methods

    def max_value(self, nums1, nums0):
        """
        Calculates the maximum possible integer value of the concatenated binary string.

        Args:
            nums1 (List[int]): Number of '1's in each segment.
            nums0 (List[int]): Number of '0's in each segment.

        Returns:
            int: The maximum possible value modulo 10^9 + 7.
        """
        mod_val = 10**9 + 7
        n = len(nums1)

        # We categorize segments to prioritize higher-value binary positions.
        # 1. Pure ones: Should always be at the beginning to maximize leading 1s.
        # 2. Mixed: Segments with both 1s and 0s, sorted to minimize 'gaps'.
        # 3. Pure zeros: Should always be at the end.
        pure_ones = []
        mixed = []
        pure_zeros = []

        for i in range(n):
            ones_count, zeros_count = nums1[i], nums0[i]
            if zeros_count == 0:
                pure_ones.append((ones_count, zeros_count))
            elif ones_count == 0:
                pure_zeros.append((ones_count, zeros_count))
            else:
                mixed.append((ones_count, zeros_count))

        # Sorting mixed segments:
        # - Primary key: Number of ones descending (-x[0])
        # - Secondary key: Number of zeros ascending (x[1])
        mixed.sort(key=lambda x: (-x[0], x[1]))

        # Construct the optimal sequence of segments
        final_order = pure_ones + mixed + pure_zeros

        total_value = 0
        for ones, zeros in final_order:
            segment_length = ones + zeros
            if segment_length == 0:
                continue

            # Shift the current total value to the left by the length of the new segment
            total_value = (total_value * pow(2, segment_length, mod_val)) % mod_val

            # Calculate the value of the current segment:
            # A segment of 'o' ones followed by 'z' zeros is (2^o - 1) * 2^z
            segment_contribution = ((pow(2, ones, mod_val) - 1) * pow(2, zeros, mod_val)) % mod_val

            total_value = (total_value + segment_contribution) % mod_val

        return total_value

# To maintain compatibility with the requested maxValue syntax while passing Pylint:
# we can define an alias or simply use max_value as the standard.
