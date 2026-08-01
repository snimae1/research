import heapq

class EventManager(object):

    def __init__(self, events):
        """
        :type events: List[List[int]]
        """
        # self.priorities speichert {eventId: current_priority}
        self.priorities = {}
        # self.heap speichert (-priority, eventId) 
        # Wir nutzen -priority, um aus dem Min-Heap einen Max-Heap zu machen.
        # Bei gleicher Priorität sorgt die eventId (als zweites Element im Tuple)
        # automatisch dafür, dass die kleinste ID zuerst kommt.
        self.heap = []
        
        for event_id, priority in events:
            self.priorities[event_id] = priority
            heapq.heappush(self.heap, (-priority, event_id))

    def updatePriority(self, eventId, newPriority):
        """
        :type eventId: int
        :type newPriority: int
        :rtype: None
        """
        # Aktualisiere die aktuelle Priorität im Dictionary
        self.priorities[eventId] = newPriority
        # Füge den neuen Zustand in den Heap ein (Lazy Update)
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self):
        """
        :rtype: int
        """
        while self.heap:
            neg_prio, event_id = heapq.heappop(self.heap)
            prio = -neg_prio
            
            # Prüfen, ob das Event noch aktiv ist und die Priorität aktuell ist
            if event_id in self.priorities and self.priorities[event_id] == prio:
                # Entferne das Event aus den aktiven Events
                del self.priorities[event_id]
                return event_id
        
        # Keine aktiven Events mehr vorhanden
        return -1
