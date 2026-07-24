class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Wir wandeln den String in eine Liste um, da Strings in Python unveränderlich sind
        chars = list(s)
        
        # Extrahiere alle Buchstaben und Sonderzeichen in separate Listen
        letters = [c for c in chars if c.islower()]
        specials = [c for c in chars if not c.islower()]
        
        # Kehre beide Listen um (In-place)
        letters.reverse()
        specials.reverse()
        
        # Zeiger für die aktuellen Elemente aus den umgedrehten Listen
        l_idx = 0
        s_idx = 0
        
        result = []
        for c in chars:
            if c.islower():
                # Wenn an dieser Stelle ein Buchstabe war, nimm den nächsten aus der reversed-Liste
                result.append(letters[l_idx])
                l_idx += 1
            else:
                # Wenn an dieser Stelle ein Sonderzeichen war, nimm das nächste aus der reversed-Liste
                result.append(specials[s_idx])
                s_idx += 1
                
        return "".join(result)
