class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiou')
        # Indices of all vowels in the original string
        vowel_indices = [i for i, ch in enumerate(s) if ch in vowels]
        
        # If no vowels, return the original string
        if not vowel_indices:
            return s
        
        # Extract the vowel characters in order of appearance
        vowel_chars = [s[i] for i in vowel_indices]
        
        # Count frequencies and find first occurrence of each distinct vowel
        unique_vowels = set(vowel_chars)
        vowel_info = []
        for v in unique_vowels:
            freq = s.count(v)            # total occurrences in s
            first_pos = s.find(v)        # first index in s
            vowel_info.append((v, freq, first_pos))
        
        # Sort by frequency descending, then by first occurrence ascending
        vowel_info.sort(key=lambda x: (-x[1], x[2]))
        
        # Build the sorted list of all vowels
        sorted_vowels = []
        for v, freq, _ in vowel_info:
            sorted_vowels.extend([v] * freq)
        
        # Place the sorted vowels back into the original vowel positions
        result = list(s)
        for idx, ch in zip(vowel_indices, sorted_vowels):
            result[idx] = ch
            
        return "".join(result)
