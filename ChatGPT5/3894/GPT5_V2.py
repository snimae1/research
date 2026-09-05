```python
"""Determine the current state of a traffic signal."""


class Solution:
    """Provide the traffic signal state for a given timer."""

    def trafficSignal(self, timer):
        """
        Return the current traffic signal state.

        :param timer: Remaining time in seconds.
        :return: Current traffic signal state.
        """
        if timer == 0:
            return "Green"

        if timer == 30:
            return "Orange"

        if 30 < timer <= 90:
            return "Red"

        return "Invalid"
```
