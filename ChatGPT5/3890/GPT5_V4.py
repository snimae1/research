"""Find all good integers represented by two distinct pairs of cubes."""


class Solution(object):
    """Solve the problem of finding good integers."""

    # pylint: disable=invalid-name, too-few-public-methods

    def findGoodIntegers(self, n):
        """
        Find all integers <= n with at least two representations as a^3 + b^3.

        :param n: Upper limit for the generated integers.
        :type n: int
        :return: Sorted list of all good integers.
        :rtype: List[int]
        """

        # Find the largest possible value for a and b.
        limit = 1
        while limit * limit * limit <= n:
            limit += 1
        limit -= 1

        # Count how many different pairs produce each sum.
        sum_counts = {}

        for a in range(1, limit + 1):
            cube_a = a * a * a

            for b in range(a, limit + 1):
                cube_b = b * b * b
                current_sum = cube_a + cube_b

                # All following values of b would produce an even
                # larger sum.
                if current_sum > n:
                    break

                sum_counts[current_sum] = (
                    sum_counts.get(current_sum, 0) + 1
                )

        # Keep only sums that have at least two distinct pairs.
        good_integers = [
            value
            for value, count in sum_counts.items()
            if count >= 2
        ]

        good_integers.sort()

        return good_integers
