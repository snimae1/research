import heapq

class EventManager(object):

    def __init__(self, events):
        """
        :type events: List[List[int]]
        """
        self.heap = []
        self.priority = {}

        for eventId, p in events:
            self.priority[eventId] = p
            heapq.heappush(self.heap, (-p, eventId))

    def updatePriority(self, eventId, newPriority):
        """
        :type eventId: int
        :type newPriority: int
        :rtype: None
        """
        self.priority[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self):
        """
        :rtype: int
        """
        while self.heap:
            negPriority, eventId = heapq.heappop(self.heap)
            current = self.priority.get(eventId)

            # Event wurde bereits entfernt
            if current is None:
                continue

            # Veralteter Heap-Eintrag
            if current != -negPriority:
                continue

            # Gültiges Event entfernen
            del self.priority[eventId]
            return eventId

        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId, newPriority)
# param_2 = obj.pollHighest()
