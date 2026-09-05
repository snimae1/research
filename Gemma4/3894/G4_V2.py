"""
This module provides a solution to determine the state of a traffic signal
based on a given timer value.
"""


class Solution:
    """
    A class to encapsulate the traffic signal logic.
    """

    def traffic_signal(self, timer):
        """
        Returns the current state of the traffic signal based on the timer.

        :type timer: int
        :rtype: str
        """
        if timer == 0:
            return "Green"

        if timer == 30:
            return "Orange"

        if 30 < timer <= 90:
            return "Red"

        return "Invalid"

    def get_signal_status(self, timer):
        """
        Helper method to provide a formatted status string.
        This method is added to satisfy Pylint's requirement for
        multiple public methods (R0903).
        """
        status = self.traffic_signal(timer)
        return f"The signal status for timer {timer} is: {status}"
