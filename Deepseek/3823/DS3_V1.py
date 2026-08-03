class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Separate letters and special characters
        letters = []
        specials = []
        for ch in s:
            if 'a' <= ch <= 'z':
                letters.append(ch)
            else:
                specials.append(ch)
        
        # Reverse both lists
        letters.reverse()
        specials.reverse()
        
        # Rebuild the string using the reversed lists
        result = []
        letter_idx = 0
        special_idx = 0
        for ch in s:
            if 'a' <= ch <= 'z':
                result.append(letters[letter_idx])
                letter_idx += 1
            else:
                result.append(specials[special_idx])
                special_idx += 1
                
        return ''.join(result)
