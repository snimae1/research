import heapq

class EventManager(object):

    def __init__(self, events):
        """
        :type events: List[List[int]]
        """
        # priority map: eventId -> current priority for active events
        self.priorities = {}
        # max-heap simulated with negative priorities
        self.heap = []

        for eventId, priority in events:
            self.priorities[eventId] = priority
            heapq.heappush(self.heap, (-priority, eventId))

    def updatePriority(self, eventId, newPriority):
        """
        :type eventId: int
        :type newPriority: int
        :rtype: None
        """
        # Update the known priority for this active event.
        self.priorities[eventId] = newPriority
        # Push the new priority entry; old entries will be lazily ignored.
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self):
        """
        :rtype: int
        """
        # Keep popping until we find a valid entry or the heap is empty.
        while self.heap:
            neg_pri, eventId = heapq.heappop(self.heap)
            # Check if this event is still active and has the correct priority.
            if eventId in self.priorities and self.priorities[eventId] == -neg_pri:
                # Valid highest-priority event found – remove it and return.
                del self.priorities[eventId]
                return eventId
            # Otherwise, this is a stale entry and we ignore it.

        # No active events remain.
        return -1
