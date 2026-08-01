class Solution(object):

    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_set = set('aeiou')
        
        # 1. Alle Vokale aus dem String extrahieren und ihre Positionen merken
        extracted_vowels = []
        first_occurrence = {} # Speichert die erste Position jedes Vokals
        counts = {}           # Speichert die Häufigkeit jedes Vokals
        
        for i, char in enumerate(s):
            if char in vowels_set:
                extracted_vowels.append(char)
                counts[char] = counts.get(char, 0) + 1
                if char not in first_occurrence:
                    first_occurrence[char] = i
        
        # 2. Die extrahierten Vokale nach den Regeln sortieren:
        # Regel A: Nicht-steigende Häufigkeit (descending frequency) -> -counts[x]
        # Regel B: Position des ersten Vorkommens (ascending index) -> first_occurrence[x]
        sorted_vowels = sorted(
            extracted_vowels, 
            key=lambda x: (-counts[x], first_occurrence[x])
        )
        
        # 3. Den ursprünglichen String rekonstruieren
        # Wir ersetzen nur die Stellen, an denen Vokale waren, durch die sortierten Vokale
        res = list(s)
        vowel_ptr = 0
        for i in range(len(res)):
            if res[i] in vowels_set:
                res[i] = sorted_vowels[vowel_ptr]
                vowel_ptr += 1
                
        return "".join(res)
