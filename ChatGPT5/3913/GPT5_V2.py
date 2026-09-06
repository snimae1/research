"""Rearrange vowels by decreasing frequency."""

class Solution(object):
"""Solution for sorting vowels by their frequency."""

```
def sortVowels(self, s):
    """
    Rearrange vowels by decreasing frequency.

    If frequencies are equal, preserve the order of
    their first occurrence.

    :param s: Input string consisting of lowercase letters.
    :return: String with vowels rearranged.
    """
    vowels = "aeiou"
    frequency = {}
    first_position = {}

    # Count each vowel and remember its first occurrence.
    for position, character in enumerate(s):
        if character in vowels:
            frequency[character] = frequency.get(character, 0) + 1
            if character not in first_position:
                first_position[character] = position

    # Sort vowels by frequency and then by first occurrence.
    sorted_vowels = sorted(
        frequency,
        key=lambda vowel: (-frequency[vowel], first_position[vowel])
    )

    # Create the sequence that will replace the original vowels.
    ordered_vowels = []
    for vowel in sorted_vowels:
        ordered_vowels.extend([vowel] * frequency[vowel])

    # Replace vowels while keeping all consonants unchanged.
    result = list(s)
    vowel_index = 0

    for position, character in enumerate(result):
        if character in vowels:
            result[position] = ordered_vowels[vowel_index]
            vowel_index += 1

    return "".join(result)
```
