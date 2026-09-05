"""
Modul zur Verwaltung von Events mit Prioritäten.
Implementiert eine EventManager-Klasse, die das Event mit der höchsten
Priorität effizient zurückgibt.
"""
import heapq

class EventManager:
    """
    Verwaltet eine Liste von Events. Ermöglicht das Aktualisieren von
    Prioritäten und das Abrufen des Events mit der höchsten Priorität.
    """

    def __init__(self, events):
        """
        Initialisiert den EventManager mit einer Liste von Events.

        :param events: Liste von Listen, wobei jedes Element [eventId, priority] ist.
        :type events: List[List[int]]
        """
        # self.priorities speichert {eventId: current_priority}
        self.priorities = {}
        # self.heap speichert (-priority, eventId)
        # Wir nutzen -priority, um aus dem Min-Heap einen Max-Heap zu machen.
        self.heap = []

        for event_id, priority in events:
            self.priorities[event_id] = priority
            heapq.heappush(self.heap, (-priority, event_id))

    def updatePriority(self, eventId, newPriority): # pylint: disable=invalid-name
        """
        Aktualisiert die Priorität eines aktiven Events.

        :param eventId: Die ID des zu aktualisierenden Events.
        :param newPriority: Die neue Priorität.
        :type eventId: int
        :type newPriority: int
        :rtype: None
        """
        self.priorities[eventId] = newPriority
        # Lazy Update: Wir fügen die neue Priorität einfach hinzu.
        # Die alte Priorität bleibt im Heap, wird aber in pollHighest ignoriert.
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self): # pylint: disable=invalid-name
        """
        Entfernt und gibt die eventId des Events mit der höchsten Priorität zurück.
        Bei Gleichstand wird die kleinste eventId zurückgegeben.

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

# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
