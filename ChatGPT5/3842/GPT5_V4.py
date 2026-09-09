"""Solution for the light bulb toggling problem."""


# Class and method names are required by the task.
# pylint: disable=invalid-name,too-few-public-methods
class Solution:
    """Provide a solution for toggling light bulbs."""

    def toggleLightBulbs(self, bulbs):
        """
        Toggle each bulb and return all bulbs that are on.

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
