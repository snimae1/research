"""Solution for calculating the sum of GCD values of paired prefix GCDs."""

from math import gcd


class Solution:  # pylint: disable=too-few-public-methods
    """Provides a solution for the gcdSum problem."""

    def gcdSum(self, nums):  # pylint: disable=invalid-name
        """
        Calculate the sum of GCD values obtained from paired prefix GCDs.

        For every element, its GCD with the maximum value seen so far is
        calculated. The resulting values are sorted, and the smallest and
        largest remaining values are paired.

        :type nums: List[int]
        :rtype: int
        """
        prefix_gcd = []
        maximum = 0

        # Build the array containing gcd(nums[i], maximum_so_far).
        for number in nums:
            maximum = max(maximum, number)
            prefix_gcd.append(gcd(number, maximum))

        prefix_gcd.sort()

        gcd_sum = 0
        left = 0
        right = len(prefix_gcd) - 1

        # Pair the smallest remaining value with the largest remaining value.
        while left < right:
            gcd_sum += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return gcd_sum
