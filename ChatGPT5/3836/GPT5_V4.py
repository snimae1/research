"""Lösung für die Berechnung der maximalen Punktzahl aus k geordneten Paaren."""

from functools import lru_cache


class Solution:
    """Berechnet die maximale Punktzahl für k geordnet ausgewählte Indexpaarungen."""

    def maxScore(self, nums1, nums2, k):  # pylint: disable=invalid-name
        """
        Berechnet die maximal erreichbare Summe aus genau k Produkten.
        """
        length1 = len(nums1)
        length2 = len(nums2)
        negative_infinity = float("-inf")

        @lru_cache(maxsize=None)
        def find_max_score(index1, index2, pairs_remaining):
            """
            Berechnet die beste Punktzahl ab den aktuellen Array-Positionen.
            """
            # Alle benötigten Paare wurden ausgewählt.
            if pairs_remaining == 0:
                return 0

            # Es sind nicht genügend Elemente für die restlichen Paare vorhanden.
            if (
                length1 - index1 < pairs_remaining
                or length2 - index2 < pairs_remaining
            ):
                return negative_infinity

            # Möglichkeit 1: Element aus nums1 überspringen.
            best_score = find_max_score(
                index1 + 1,
                index2,
                pairs_remaining,
            )

            # Möglichkeit 2: Element aus nums2 überspringen.
            best_score = max(
                best_score,
                find_max_score(
                    index1,
                    index2 + 1,
                    pairs_remaining,
                ),
            )

            # Möglichkeit 3: Aktuelle Elemente miteinander paaren.
            pair_score = (
                nums1[index1] * nums2[index2]
                + find_max_score(
                    index1 + 1,
                    index2 + 1,
                    pairs_remaining - 1,
                )
            )

            return max(best_score, pair_score)

        return find_max_score(0, 0, k)
