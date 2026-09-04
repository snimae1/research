"""Solution for reversing letters and special characters independently."""

class Solution:
"""Provide a solution for reversing characters by their type."""

```
def reverseByType(self, s):
    """Reverse letters and special characters within their original positions."""
    letters = [character for character in s if character.isalpha()]
    special_characters = [
        character for character in s if not character.isalpha()
    ]

    letters.reverse()
    special_characters.reverse()

    result = []
    letter_index = 0
    special_index = 0

    for character in s:
        if character.isalpha():
            result.append(letters[letter_index])
            letter_index += 1
        else:
            result.append(special_characters[special_index])
            special_index += 1

    return "".join(result)
```
