"""Solution for computing sum of GCDs of paired prefixGcd elements."""

import math

class Solution(object):
    """Class providing method to compute gcd sum based on prefix maxima."""

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Build prefix_gcd array
        prefix_gcd = []
        current_max = nums[0]
        for num in nums:
            current_max = max(current_max, num)
            g = math.gcd(num, current_max)
            prefix_gcd.append(g)

        # Step 2: Sort the array
        prefix_gcd.sort()

        # Step 3: Pair up and sum gcd of pairs
        total = 0
        n = len(prefix_gcd)
        for i in range(n // 2):
            total += math.gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])

        return total
