"""Solution for toggling light bulbs based on repeated occurrences."""

# The class and method names are required by the task interface.

# pylint: disable=invalid-name,too-few-public-methods

class Solution:
"""Provide a solution for the light bulb toggling problem."""

```
def toggleLightBulbs(self, bulbs):
    """
    Toggle bulbs on or off for each occurrence in the input list.

    :type bulbs: List[int]
    :rtype: List[int]
    """
    active_bulbs = set()

    for bulb in bulbs:
        if bulb in active_bulbs:
            active_bulbs.remove(bulb)
        else:
            active_bulbs.add(bulb)

    return sorted(active_bulbs)
```
