"""
EventManager class for managing events with priorities.
Supports updating priorities and polling the highest priority event.
"""
import heapq

# The API requires camelCase method and parameter names as specified in the problem.
# pylint: disable=invalid-name

class EventManager:
    """
    Manages a collection of active events, each with a unique id and priority.
    Supports priority updates and removal of the highest priority event.
    """

    def __init__(self, events):
        """
        Initializes the manager with the given events.

        :param events: List of [eventId, priority] pairs.
        :type events: List[List[int]]
        """
        # Map from eventId to its current priority for quick lookup.
        self.priorities = {}
        # Max-heap simulated using negative priorities.
        self.heap = []

        for event_id, priority in events:
            self.priorities[event_id] = priority
            heapq.heappush(self.heap, (-priority, event_id))

    def updatePriority(self, eventId, newPriority):
        """
        Updates the priority of an active event.

        :param eventId: The id of the event to update.
        :type eventId: int
        :param newPriority: The new priority value.
        :type newPriority: int
        """
        # Record the new priority (old heap entries will be ignored later).
        self.priorities[eventId] = newPriority
        # Push the new priority onto the heap.
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self):
        """
        Removes and returns the eventId with the highest priority.
        If multiple events share the highest priority, the smallest id is returned.
        Returns -1 if there are no active events.

        :return: The eventId of the highest priority event, or -1.
        :rtype: int
        """
        # Keep popping until we find a valid entry or the heap is empty.
        while self.heap:
            neg_pri, event_id = heapq.heappop(self.heap)
            # Check if this entry is still active and has the current priority.
            if event_id in self.priorities and self.priorities[event_id] == -neg_pri:
                # Valid event found; remove it and return its id.
                del self.priorities[event_id]
                return event_id
            # Otherwise, this is a stale entry and we skip it.

        # No active events remain.
        return -1
