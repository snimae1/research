"""Lösung zum Finden der ersten einzigartigen geraden Zahl."""

# Die Namen Solution und firstUniqueEven sind durch die Aufgabenplattform vorgegeben.

# pylint: disable=invalid-name,too-few-public-methods

class Solution:
"""Enthält die Lösung für die gestellte Array-Aufgabe."""

```
def firstUniqueEven(self, nums):
    """
    Findet die erste gerade Zahl, die im Array genau einmal vorkommt.

    :type nums: List[int]
    :rtype: int
    """
    frequencies = {}

    # Zuerst wird gezählt, wie häufig jede Zahl vorkommt.
    for number in nums:
        frequencies[number] = frequencies.get(number, 0) + 1

    # Anschließend wird die erste einzigartige gerade Zahl gesucht.
    for number in nums:
        if number % 2 == 0 and frequencies[number] == 1:
            return number

    return -1
```
