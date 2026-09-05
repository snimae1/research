"""Solution for mapping word weights to reverse alphabetical characters."""

# Pylint names are intentionally kept to match the required platform interface.

# pylint: disable=invalid-name,too-few-public-methods

class Solution:
"""Provide the solution for the word weight mapping problem."""

```
def mapWordWeights(self, words, weights):
    """
    Calculate each word's weight and map it to a reverse alphabet letter.

    Args:
        words: A list of lowercase English words.
        weights: A list containing the weights of letters from 'a' to 'z'.

    Returns:
        A string containing the mapped character for each word.
    """
    result = []

    for word in words:
        word_weight = sum(
            weights[ord(character) - ord("a")]
            for character in word
        )

        mapped_value = word_weight % 26
        mapped_character = chr(ord("z") - mapped_value)
        result.append(mapped_character)

    return "".join(result)
```

