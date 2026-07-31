class Solution(object):

    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        # Schritt 1: Prüfen, ob der String bereits sortiert ist
        if list(s) == sorted(s):
            return 0
        
        n = len(s)
        min_char = min(s)
        max_char = max(s)
        
        # Schritt 2: Prüfen, ob es in einer Operation möglich ist.
        # Dies ist möglich, wenn entweder das erste Zeichen bereits das globale Minimum ist
        # (dann sortieren wir den Rest von Index 1 bis n-1) oder das letzte Zeichen 
        # bereits das globale Maximum ist (dann sortieren wir von Index 0 bis n-2).
        if s[0] == min_char or s[n-1] == max_char:
            return 1
        
        # Schritt 3: Prüfen, ob es unmöglich ist.
        # Wenn das erste Zeichen das globale Maximum IST UND das letzte Zeichen 
        # das globale Minimum IST, können wir die beiden niemals an ihre richtige
        # Position bringen, da jede Operation einen Teilstring ausschließt (entweder 
        # den ersten oder den letzten Buchstaben).
        if s[0] == max_char and s[n-1] == min_char:
            return -1
        
        # Schritt 4: In allen anderen Fällen sind genau 2 Operationen nötig.
        # Wir können erst einen Teilstring sortieren, um entweder das Minimum nach vorne
        # oder das Maximum nach hinten zu bringen, und dann den restlichen String sortieren.
        return 2
