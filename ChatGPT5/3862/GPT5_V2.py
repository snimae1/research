"""Solution for finding the smallest balanced index in an integer array."""

class Solution:  # pylint: disable=too-few-public-methods
"""Provide a solution for finding the smallest balanced index."""

```
def smallestBalancedIndex(self, nums):  # pylint: disable=invalid-name
    """
    Return the smallest index where the left sum equals the right product.

    The sum of an empty left side is defined as 0, while the product
    of an empty right side is defined as 1.

    :type nums: List[int]
    :rtype: int
    """
    right_product = 1

    # Calculate the product of all elements. This initially represents
    # the product containing the current element and everything to its right.
    for number in nums:
        right_product *= number

    left_sum = 0

    # Check each index from left to right so the first valid index
    # is automatically the smallest balanced index.
    for index, number in enumerate(nums):
        # Remove the current element to obtain the product strictly
        # to the right of the current index.
        right_product //= number

        if left_sum == right_product:
            return index

        # Add the current element after checking, because left_sum
        # represents only elements strictly to the left.
        left_sum += number

    return -1
```
