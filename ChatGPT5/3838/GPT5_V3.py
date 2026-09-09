"""Map word weights to letters in reverse alphabetical order."""


class Solution(object):  # pylint: disable=too-few-public-methods
    """Provide the solution for mapping weighted words to characters."""

    def mapWordWeights(self, words, weights):  # pylint: disable=invalid-name
        """
        Calculate each word's weight and map it to a lowercase letter.

        The character weights are summed for every word. The sum modulo 26
        determines a letter in reverse alphabetical order:
        0 maps to 'z', 1 maps to 'y', and 25 maps to 'a'.

        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        mapped_characters = []

        for word in words:
            word_weight = sum(
                weights[ord(character) - ord("a")]
                for character in word
            )

            letter_index = word_weight % 26
            mapped_character = chr(ord("z") - letter_index)
            mapped_characters.append(mapped_character)

        return "".join(mapped_characters)
