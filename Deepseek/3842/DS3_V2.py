# pylint: disable=invalid-name, too-few-public-methods
"""
Module for toggling light bulbs based on given indices.
"""

class Solution:
    """Solution class for the light bulb toggling problem."""

    def toggleLightBulbs(self, bulbs):
        """
        Toggles light bulbs according to the given list of bulb numbers.

        Args:
            bulbs (List[int]): List of bulb indices (1‑based) to toggle.

        Returns:
            List[int]: Sorted list of bulbs that are on after all toggles.
                       Empty list if none are on.
        """
        on = set()
        for bulb in bulbs:
            if bulb in on:
                on.remove(bulb)
            else:
                on.add(bulb)
        return sorted(on)
