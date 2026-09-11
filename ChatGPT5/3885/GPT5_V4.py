"""Effiziente Verwaltung von Events nach ihrer Priorität."""

import heapq


class EventManager:
    """Verwaltet aktive Events nach ihrer Priorität."""

    def __init__(self, events):
        """
        Initialisiert den EventManager.

        :type events: List[List[int]]
        """
        self._heap = []
        self._priorities = {}

        for event_id, priority in events:
            self._priorities[event_id] = priority
            heapq.heappush(self._heap, (-priority, event_id))

    def updatePriority(self, event_id, new_priority):  # pylint: disable=invalid-name
        """
        Aktualisiert die Priorität eines aktiven Events.

        :type event_id: int
        :type new_priority: int
        :rtype: None
        """
        self._priorities[event_id] = new_priority
        heapq.heappush(self._heap, (-new_priority, event_id))

    def pollHighest(self):  # pylint: disable=invalid-name
        """
        Entfernt und liefert das Event mit der höchsten Priorität.

        Bei gleicher Priorität wird die kleinere Event-ID zurückgegeben.

        :rtype: int
        """
        while self._heap:
            negative_priority, event_id = heapq.heappop(self._heap)

            current_priority = self._priorities.get(event_id)

            # Veraltete oder bereits entfernte Einträge überspringen.
            if current_priority is None:
                continue

            if current_priority != -negative_priority:
                continue

            del self._priorities[event_id]
            return event_id

        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId, newPriority)
# param_2 = obj.pollHighest()
