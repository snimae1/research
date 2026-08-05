class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}

        # Häufigkeiten aller Zahlen zählen
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Erste gerade Zahl mit Häufigkeit 1 finden
        for num in nums:
            if num % 2 == 0 and count[num] == 1:
                return num

        return -1
