"""Solution for making an array non-decreasing with minimum operations."""

class Solution(object):
"""Provide the solution for the minimum-operations problem."""

```
def minOperations(self, nums):
    """
    Calculate the minimum sum of operation values.

    :param nums: List of integers.
    :return: Minimum possible sum of x values.
    """
    total = 0

    # A decrease between two neighboring elements must be compensated.
    # Increasing the current and following elements can fix that decrease.
    for index in range(1, len(nums)):
        if nums[index] < nums[index - 1]:
            total += nums[index - 1] - nums[index]

    return total
```
