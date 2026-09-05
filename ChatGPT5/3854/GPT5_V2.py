"""Solution for making an array parity alternating with minimum operations."""

class Solution(object):
"""Solve the parity-alternating array problem."""

```
# pylint: disable=too-few-public-methods
# pylint: disable=useless-object-inheritance

def makeParityAlternating(self, nums):  # pylint: disable=invalid-name
    """
    Return minimum operations and the smallest possible range.

    :type nums: List[int]
    :rtype: List[int]
    """
    even_first = self._solve_pattern(nums, 0)
    odd_first = self._solve_pattern(nums, 1)

    if even_first[0] < odd_first[0]:
        return list(even_first)

    if odd_first[0] < even_first[0]:
        return list(odd_first)

    return [
        even_first[0],
        min(even_first[1], odd_first[1])
    ]

@staticmethod
def _solve_pattern(nums, first_parity):
    """Solve one of the two possible parity patterns."""
    operation_count = 0
    intervals = []

    for index, value in enumerate(nums):
        required_parity = (first_parity + index) % 2

        if value % 2 == required_parity:
            # No operation is necessary. The value must remain unchanged
            # because we are looking for the minimum possible operation
            # count.
            intervals.append((value, value))
        else:
            # Exactly one operation changes the parity. Both value - 1
            # and value + 1 are therefore possible.
            operation_count += 1
            intervals.append((value - 1, value + 1))

    minimum_range = Solution._find_minimum_range(intervals)

    return operation_count, minimum_range

@staticmethod
def _find_minimum_range(intervals):
    """
    Find the smallest range containing at least one value from every set.

    Each interval represents the possible values of one array element
    after the minimum number of operations has been performed.
    """
    lower_bound = min(left for left, _ in intervals)
    upper_bound = max(right for _, right in intervals)

    left = 0
    right = upper_bound - lower_bound

    while left < right:
        range_size = (left + right) // 2

        if Solution._range_is_possible(intervals, range_size):
            right = range_size
        else:
            left = range_size + 1

    return left

@staticmethod
def _range_is_possible(intervals, range_size):
    """
    Check whether all possible-value sets fit into one range.

    For an interval [a, b], a range [x, x + range_size] intersects it
    exactly when:

        x <= b
        x + range_size >= a

    Thus x must lie between a - range_size and b.
    """
    possible_left = None
    possible_right = None

    for interval_left, interval_right in intervals:
        candidate_left = interval_left - range_size
        candidate_right = interval_right

        if possible_left is None:
            possible_left = candidate_left
            possible_right = candidate_right
        else:
            possible_left = max(possible_left, candidate_left)
            possible_right = min(possible_right, candidate_right)

        if possible_left > possible_right:
            return False

    return True
```
