"""
Dieses Modul bietet eine Lösung, um Vokale am Ende eines Strings zu entfernen.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Bearbeitung von Zeichenketten.
    """

    def trim_trailing_vowels(self, s):
        """
        Entfernt alle Vokale ('a', 'e', 'i', 'o', 'u') vom rechten Ende des Strings.

        :type s: str
        :rtype: str
        """
        return s.rstrip('aeiou')
