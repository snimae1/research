class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        for word in words:
            # Sum the weights of the characters in the word
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]
            # Modulo 26 and map to reverse alphabetical order: 0->z, 1->y, ..., 25->a
            mapped_char = chr(ord('z') - (total % 26))
            result.append(mapped_char)
        return ''.join(result)
