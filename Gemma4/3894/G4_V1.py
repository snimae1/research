class Solution(object):

    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """
        # Prüfung auf Green (timer == 0)
        if timer == 0:
            return "Green"
        
        # Prüfung auf Orange (timer == 30)
        elif timer == 30:
            return "Orange"
        
        # Prüfung auf Red (30 < timer <= 90)
        elif 30 < timer <= 90:
            return "Red"
        
        # Falls keine der Bedingungen zutrifft
        else:
            return "Invalid"
