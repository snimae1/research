class Solution(object):
    def reverseByType(self, s):
        letters = []
        specials = []
        
        # Trenne Buchstaben und Sonderzeichen
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                specials.append(ch)
        
        # Beide Listen umdrehen
        letters.reverse()
        specials.reverse()
        
        result = []
        i = 0  # Zeiger für letters
        j = 0  # Zeiger für specials
        
        # String neu aufbauen
        for ch in s:
            if ch.isalpha():
                result.append(letters[i])
                i += 1
            else:
                result.append(specials[j])
                j += 1
        
        return "".join(result)
