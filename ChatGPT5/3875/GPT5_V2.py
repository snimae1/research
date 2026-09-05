"""Solution for determining whether an array can be made uniform."""

# pylint: disable=invalid-name,too-few-public-methods

class Solution(object):
"""Determine whether all resulting values can have the same parity."""

```
def uniformArray(self, nums1):
    """
    Determine whether nums1 can be transformed into an all-odd
    or all-even array.

    :param nums1: List of distinct integers.
    :return: True if a uniform parity is possible, otherwise False.
    """
    # If all numbers are even, we can keep every number unchanged.
    if all(number % 2 == 0 for number in nums1):
        return True

    # If there is at least one odd number, use it as the subtrahend
    # for every even number. Even - odd results in an odd number.
    has_odd_number = any(number % 2 != 0 for number in nums1)

    return has_odd_number
```

if **name** == "**main**":
solution = Solution()

```
print(solution.uniformArray([2, 3]))
print(solution.uniformArray([4, 6]))
```
