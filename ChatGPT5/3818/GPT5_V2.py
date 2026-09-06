"""Solution for finding the minimum prefix removal length."""

class Solution:
"""Provide solutions for the prefix removal problem."""

```
def minimumPrefixLength(self, nums):  # pylint: disable=invalid-name
    """Return the minimum prefix length to remove.

    The remaining suffix must be strictly increasing.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of elements that must be removed from
        the beginning of the list.
    """
    index = len(nums) - 1

    # Find the start of the longest strictly increasing suffix.
    while index > 0 and nums[index - 1] < nums[index]:
        index -= 1

    return index
```
