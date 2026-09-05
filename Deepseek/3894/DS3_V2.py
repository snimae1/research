"""
Solution for the traffic signal problem.

This module provides a class with a method to determine the current
state of a traffic signal based on the remaining time.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """Provides a method to determine the traffic signal state."""

    # pylint: disable=invalid-name
    def trafficSignal(self, timer):
        """
        Return the current state of the traffic signal.

        Args:
            timer (int): Remaining time in seconds.

        Returns:
            str: "Green", "Orange", "Red", or "Invalid".
        """
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 30 < timer <= 90:
            return "Red"
        return "Invalid"
