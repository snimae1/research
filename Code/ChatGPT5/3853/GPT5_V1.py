class Solution(object):
    def minDistinctFreqPair(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}

        # Häufigkeiten zählen
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Verschiedene Werte sortieren
        values = sorted(freq.keys())

        # Kleinste gültige Paarung suchen
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if freq[values[i]] != freq[values[j]]:
                    return [values[i], values[j]]

        return [-1, -1]
