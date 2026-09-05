"""Find all integers that can be represented as two cubes in two ways."""

class Solution(object):
"""Solve the problem of finding good integers."""

```
# Pylint muss hier die LeetCode-Schnittstelle akzeptieren.
# pylint: disable=invalid-name, too-few-public-methods

def findGoodIntegers(self, n):
    """
    Find all integers <= n with at least two representations as a^3 + b^3.

    Args:
        n (int): Upper limit for the generated integers.

    Returns:
        list[int]: Sorted list of all good integers.
    """

    # Determine the largest possible value for a and b.
    # Since a^3 + b^3 <= n, neither a nor b can be larger
    # than the cube root of n.
    limit = 1
    while limit * limit * limit <= n:
        limit += 1
    limit -= 1

    # Store how many different pairs (a, b) produce each sum.
    # Only pairs with a <= b are considered, so each pair
    # is counted exactly once.
    sum_counts = {}

    for a in range(1, limit + 1):
        cube_a = a * a * a

        for b in range(a, limit + 1):
            cube_b = b * b * b
            current_sum = cube_a + cube_b

            # b only gets larger, so all following sums would
            # also be too large.
            if current_sum > n:
                break

            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1

    # An integer is good if at least two distinct pairs
    # (a, b) produce the same sum.
    good_integers = [
        value
        for value, count in sum_counts.items()
        if count >= 2
    ]

    good_integers.sort()
    return good_integers
```
