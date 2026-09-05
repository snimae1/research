"""Module providing a solution to find good integers."""

# pylint: disable=too-few-public-methods
class Solution:
    """Class containing method to find good integers."""

    # pylint: disable=invalid-name
    def findGoodIntegers(self, n):
        """
        Return all good integers less than or equal to n.

        A good integer x has at least two distinct pairs (a, b) with a <= b,
        positive integers, such that x = a^3 + b^3.
        """
        count = {}
        # Since a^3 + b^3 <= n <= 10^9, a and b are at most 1000.
        # Compute a safe maximum for a.
        max_a = int(n ** (1 / 3)) + 2  # +2 to avoid rounding errors

        for a in range(1, max_a + 1):
            a3 = a * a * a
            if a3 > n:
                break
            # b runs from a to the maximum possible value.
            max_b = int((n - a3) ** (1 / 3)) + 1
            for b in range(a, max_b + 1):
                b3 = b * b * b
                sum_cubes = a3 + b3
                if sum_cubes > n:
                    break
                count[sum_cubes] = count.get(sum_cubes, 0) + 1

        # All sums with at least two different pairs (a, b)
        result = [num for num, cnt in count.items() if cnt >= 2]
        result.sort()
        return result
