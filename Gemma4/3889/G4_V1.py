from collections import Counter

class Solution(object):

    def mirrorFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. Häufigkeit aller Zeichen im String zählen
        freq = Counter(s)
        
        total_diff = 0
        
        # 2. Definition der Buchstaben-Paare (a-z)
        # Wir gehen nur bis zur Hälfte des Alphabets, um jedes Paar nur einmal zu zählen
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(13): # Index 0 bis 12
            char_c = alphabet[i]
            char_m = alphabet[25 - i]
            # Absolute Differenz der Häufigkeiten berechnen
            total_diff += abs(freq[char_c] - freq[char_m])
            
        # 3. Definition der Ziffern-Paare (0-9)
        # Wir gehen nur bis zur Hälfte der Ziffern (0-4)
        digits = "0123456789"
        for i in range(5): # Index 0 bis 4
            char_c = digits[i]
            char_m = digits[9 - i]
            # Absolute Differenz der Häufigkeiten berechnen
            total_diff += abs(freq[char_c] - freq[char_m])
            
        return total_diff
