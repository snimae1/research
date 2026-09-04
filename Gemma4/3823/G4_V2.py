"""
Dieses Modul bietet eine Lösung zur getrennten Umkehrung von Buchstaben
und Sonderzeichen innerhalb eines Strings.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Manipulation von Strings basierend auf Zeichentypen.
    """

    def reverseByType(self, s):
        """
        Kehrt Buchstaben und Sonderzeichen unabhängig voneinander um,
        während ihre ursprünglichen Positionstypen beibehalten werden.

        :type s: str
        :rtype: str
        """
        # pylint: disable=invalid-name
        # Umwandlung des Strings in eine Liste, da Strings in Python immutable sind
        chars = list(s)

        # Extrahiere alle Buchstaben und Sonderzeichen in separate Listen
        letters = [c for c in chars if c.islower()]
        specials = [c for c in chars if not c.islower()]

        # Kehre beide Listen um (In-place Operation)
        letters.reverse()
        specials.reverse()

        # Indizes zur Verfolgung der aktuellen Position in den reversed-Listen
        l_idx = 0
        s_idx = 0

        result = []
        for c in chars:
            if c.islower():
                # Setze den nächsten verfügbaren Buchstaben aus der umgekehrten Liste ein
                result.append(letters[l_idx])
                l_idx += 1
            else:
                # Setze das nächste Sonderzeichen aus der umgekehrten Liste ein
                result.append(specials[s_idx])
                s_idx += 1

        return "".join(result)
