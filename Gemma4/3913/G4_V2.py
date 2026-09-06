"""
Dieses Modul bietet eine Lösung zur Sortierung von Vokalen in einem String
basierend auf ihrer Häufigkeit und ihrer ersten Position.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Implementierung der Vokal-Sortierungslogik.
    """

    def sort_vowels(self, s):
        """
        Sortiert die Vokale im String s in nicht-steigender Reihenfolge
        ihrer Häufigkeit. Bei Gleichstand wird die Position des ersten
        Vorkommens verwendet.

        :type s: str
        :rtype: str
        """
        vowels_set = set('aeiou')

        # 1. Alle Vokale extrahieren und Metadaten sammeln
        extracted_vowels = []
        first_occurrence = {}  # Speichert die erste Position jedes Vokals
        counts = {}            # Speichert die Häufigkeit jedes Vokals

        for i, char in enumerate(s):
            if char in vowels_set:
                extracted_vowels.append(char)
                counts[char] = counts.get(char, 0) + 1
                if char not in first_occurrence:
                    first_occurrence[char] = i

        # 2. Die Vokale nach den definierten Regeln sortieren:
        # -counts[x] für absteigende Häufigkeit
        # first_occurrence[x] für aufsteigenden ersten Index
        sorted_vowels = sorted(
            extracted_vowels,
            key=lambda x: (-counts[x], first_occurrence[x])
        )

        # 3. Den ursprünglichen String unter Beibehaltung der Konsonanten rekonstruieren
        res = list(s)
        vowel_ptr = 0
        for i, char in enumerate(res):
            if char in vowels_set:
                res[i] = sorted_vowels[vowel_ptr]
                vowel_ptr += 1

        return "".join(res)
