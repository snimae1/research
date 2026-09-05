"""Solution for the minimum operations required to sort a string."""

# pylint: disable=too-few-public-methods

class Solution:
"""Provide the solution required by the online judge."""

```
# pylint: disable=invalid-name
def minOperations(self, s):
    """
    Return the minimum number of substring-sorting operations.

    A selected substring must not be the entire string.

    :type s: str
    :rtype: int
    """
    # Check whether the string is already sorted.
    is_sorted = all(
        s[index] <= s[index + 1]
        for index in range(len(s) - 1)
    )

    if is_sorted:
        return 0

    # For a string of length two, the only substring containing both
    # characters is the entire string and therefore cannot be selected.
    if len(s) == 2:
        return -1

    minimum_char = min(s)
    maximum_char = max(s)

    # If the minimum character is already at the beginning, we can sort
    # everything except the first character in one operation.
    #
    # Likewise, if the maximum character is already at the end, we can
    # sort everything except the last character in one operation.
    if s[0] == minimum_char or s[-1] == maximum_char:
        return 1

    # A minimum or maximum character in the middle can first be moved to
    # the required boundary. Afterwards, the remaining substring can be
    # sorted in a second operation.
    for char in s[1:-1]:
        if char == minimum_char or char == maximum_char:
            return 2

    # Otherwise, three operations are necessary and sufficient.
    return 3
```
