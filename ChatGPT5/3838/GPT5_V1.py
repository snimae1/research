class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []

        for word in words:
            total_weight = 0

            for ch in word:
                total_weight += weights[ord(ch) - ord('a')]

            mod = total_weight % 26
            # Reverse alphabet mapping:
            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            result.append(chr(ord('z') - mod))

        return "".join(result)
