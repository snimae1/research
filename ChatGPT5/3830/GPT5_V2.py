"""Solution for finding the longest alternating subarray
after removing at most one element.
"""

class Solution:
"""Provide a solution for the alternating subarray problem."""

```
def longestAlternating(self, nums):
    """
    Return the maximum length of an alternating subarray
    after removing at most one element.

    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)

    # Compare adjacent elements:
    # 1 means increasing, -1 means decreasing, 0 means equal.
    comparisons = [
        self._comparison(nums[index], nums[index + 1])
        for index in range(length - 1)
    ]

    # Find the best answer without removing an element.
    answer = self._longest_alternating(comparisons)

    # Try removing one element between two neighboring comparisons.
    for index in range(1, length - 1):
        new_comparison = self._comparison(
            nums[index - 1],
            nums[index + 1],
        )

        if new_comparison == 0:
            continue

        left = self._alternating_left(comparisons, index - 1)
        right = self._alternating_right(comparisons, index)

        if left == 0:
            left = 1

        if right == 0:
            right = 1

        previous = (
            comparisons[index - 2]
            if index >= 2
            else None
        )
        following = (
            comparisons[index + 1]
            if index + 1 < length - 1
            else None
        )

        left_valid = (
            previous is None
            or previous != 0
            and previous != new_comparison
        )

        right_valid = (
            following is None
            or following != 0
            and following != new_comparison
        )

        if left_valid and right_valid:
            candidate = left + right + 1
            answer = max(answer, candidate)

    return answer

@staticmethod
def _comparison(first, second):
    """Return the comparison direction between two numbers."""
    if first < second:
        return 1
    if first > second:
        return -1
    return 0

@staticmethod
def _longest_alternating(comparisons):
    """Return the longest alternating sequence of comparisons."""
    best = 1
    current = 1
    previous = None

    for comparison in comparisons:
        if comparison == 0:
            current = 1
            previous = None
        elif previous is None:
            current = 2
            previous = comparison
        elif comparison != previous:
            current += 1
            previous = comparison
        else:
            current = 2
            previous = comparison

        best = max(best, current)

    return best

@staticmethod
def _alternating_left(comparisons, index):
    """Count alternating comparisons ending at the given index."""
    count = 0

    while index >= 0 and comparisons[index] != 0:
        if (
            index < len(comparisons) - 1
            and comparisons[index] == comparisons[index + 1]
        ):
            break

        count += 1
        index -= 1

    return count

@staticmethod
def _alternating_right(comparisons, index):
    """Count alternating comparisons starting at the given index."""
    count = 0

    while index < len(comparisons) and comparisons[index] != 0:
        if (
            index > 0
            and comparisons[index] == comparisons[index - 1]
        ):
            break

        count += 1
        index += 1

    return count
```
