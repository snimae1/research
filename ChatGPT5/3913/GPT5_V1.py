class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiou")
        
        # Frequenzen und erste Positionen der Vokale speichern
        freq = {}
        first_pos = {}
        
        for i, char in enumerate(s):
            if char in vowels:
                if char not in freq:
                    freq[char] = 0
                    first_pos[char] = i
                freq[char] += 1
        
        # Vokale nach:
        # 1. absteigender Häufigkeit
        # 2. aufsteigender erster Position
        sorted_vowels = sorted(
            freq.keys(),
            key=lambda x: (-freq[x], first_pos[x])
        )
        
        # Alle Vokale in der richtigen Reihenfolge sammeln
        ordered_vowels = []
        for v in sorted_vowels:
            ordered_vowels.extend([v] * freq[v])
        
        # Vokale wieder an ihre ursprünglichen Stellen einsetzen
        result = list(s)
        index = 0
        
        for i, char in enumerate(result):
            if char in vowels:
                result[i] = ordered_vowels[index]
                index += 1
        
        return "".join(result)
