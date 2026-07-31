class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Häufigkeit jedes Wertes zählen
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Zählen, wie oft jede Häufigkeit vorkommt
        freq_count = {}
        for f in freq.values():
            freq_count[f] = freq_count.get(f, 0) + 1

        # Erstes Element von links mit eindeutiger Häufigkeit zurückgeben
        for num in nums:
            if freq_count[freq[num]] == 1:
                return num

        return -1
