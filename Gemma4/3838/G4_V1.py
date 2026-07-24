class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        
        for word in words:
            # 1. Berechne das Gesamtgewicht des Wortes
            word_weight = 0
            for char in word:
                # Ermittle den Index des Buchstabens (a=0, b=1, ..., z=25)
                index = ord(char) - ord('a')
                word_weight += weights[index]
            
            # 2. Berechne das Gewicht modulo 26
            mod_val = word_weight % 26
            
            # 3. Mapping in umgekehrter alphabetischer Reihenfolge:
            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            # Da ord('z') den höchsten Wert hat, ziehen wir mod_val davon ab.
            mapped_char = chr(ord('z') - mod_val)
            result.append(mapped_char)
        
        # Verbinde alle Zeichen zu einem finalen String
        return "".join(result)
