"""Maintain whether a good subsequence exists after each update."""

from math import gcd

class Solution:
"""Solve the dynamic good-subsequence problem."""

```
def countGoodSubseq(self, nums, p, queries):
    """
    Determine how many updates leave at least one good subsequence.

    :param nums: List[int] containing the initial array.
    :param p: Required GCD of a good subsequence.
    :param queries: Updates in the form [index, value].
    :return: Number of queries after which a good subsequence exists.
    """
    size = self._tree_size(len(nums))
    values = self._normalise_values(nums, p)
    tree = self._build_tree(values, size)
    divisible_count = sum(value != 0 for value in values)
    result = 0

    for index, value in queries:
        divisible_count = self._apply_update(
            nums, values, tree, size, index, value, p,
            divisible_count
        )

        if self._has_good_subsequence(
            values, tree, size, divisible_count, len(nums)
        ):
            result += 1

    return result

@staticmethod
def _tree_size(length):
    """Return the first power of two greater than or equal to length."""
    size = 1
    while size < length:
        size *= 2
    return size

@staticmethod
def _normalise_values(nums, p):
    """
    Divide values divisible by p by p.

    A zero represents a value that cannot belong to a good subsequence.
    """
    return [
        value // p if value % p == 0 else 0
        for value in nums
    ]

@staticmethod
def _build_tree(values, size):
    """Build a segment tree containing GCD values."""
    tree = [0] * (2 * size)

    for index, value in enumerate(values):
        tree[size + index] = value

    for node in range(size - 1, 0, -1):
        tree[node] = gcd(tree[node * 2], tree[node * 2 + 1])

    return tree

@staticmethod
def _update_tree(tree, size, index, value):
    """Update one element of the GCD segment tree."""
    node = size + index
    tree[node] = value
    node //= 2

    while node:
        tree[node] = gcd(tree[node * 2], tree[node * 2 + 1])
        node //= 2

@classmethod
def _apply_update(
    cls, nums, values, tree, size, index, value, p, divisible_count
):
    """Apply one query and return the new number of divisible values."""
    if nums[index] % p == 0:
        divisible_count -= 1

    nums[index] = value

    if value % p == 0:
        divisible_count += 1
        normalised = value // p
    else:
        normalised = 0

    values[index] = normalised
    cls._update_tree(tree, size, index, normalised)

    return divisible_count

@classmethod
def _has_good_subsequence(
    cls, values, tree, size, divisible_count, length
):
    """Check whether a valid proper subsequence exists."""
    if divisible_count == 0:
        return False

    if tree[1] != 1:
        return False

    if divisible_count < length:
        return True

    return cls._can_remove_one_element(values, tree, size)

@staticmethod
def _can_remove_one_element(values, tree, size):
    """
    Check whether removing at least one element can preserve GCD 1.

    This method uses prefix/suffix GCDs only for the positions that
    contain values divisible by p.
    """
    prefix_gcd = 0
    suffix_gcd = [0] * (len(values) + 1)

    for index in range(len(values) - 1, -1, -1):
        suffix_gcd[index] = gcd(suffix_gcd[index + 1], values[index])

    for index, value in enumerate(values):
        if gcd(prefix_gcd, suffix_gcd[index + 1]) == 1:
            return True

        prefix_gcd = gcd(prefix_gcd, value)

    return False
```
