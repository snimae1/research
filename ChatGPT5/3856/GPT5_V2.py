"""Solution for removing trailing vowels from a string."""

class Solution:
"""Provides a method for removing trailing vowels."""

```
def trimTrailingVowels(self, s):
    """
    Remove all vowels from the end of the given string.

    :param s: A string containing lowercase English letters.
    :return: The string without trailing vowels.
    """
    vowels = "aeiou"
    end = len(s)

    # Move the end position backwards while the last character is a vowel.
    while end > 0 and s[end - 1] in vowels:
        end -= 1

    # Return the string up to the last non-vowel character.
    return s[:end]
```
