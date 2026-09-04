class Solution:
    """Lösung für das LeetCode-Problem: Buchstaben und Sonderzeichen getrennt umkehren."""
    
    def reverseByType(self, s):
        """
        Kehrt Buchstaben und Sonderzeichen unabhängig voneinander um,
        während die ursprünglichen Positionen erhalten bleiben.

        :param s: Eingabestring mit Kleinbuchstaben und Sonderzeichen
        :type s: str
        :return: String nach getrennter Umkehrung von Buchstaben und Sonderzeichen
        :rtype: str
        """
        # Buchstaben und Sonderzeichen getrennt sammeln
        letters = [ch for ch in s if ch.isalpha()]
        specials = [ch for ch in s if not ch.isalpha()]
        
        # Beide Listen umdrehen
        letters.reverse()
        specials.reverse()
        
        # Ergebnis zusammensetzen
        result = []
        letter_idx = 0
        special_idx = 0
        
        for ch in s:
            if ch.isalpha():
                result.append(letters[letter_idx])
                letter_idx += 1
            else:
                result.append(specials[special_idx])
                special_idx += 1
                
        return ''.join(result)
