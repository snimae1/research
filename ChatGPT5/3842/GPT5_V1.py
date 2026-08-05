class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        on_bulbs = set()

        for bulb in bulbs:
            if bulb in on_bulbs:
                on_bulbs.remove(bulb)
            else:
                on_bulbs.add(bulb)

        return sorted(on_bulbs)
