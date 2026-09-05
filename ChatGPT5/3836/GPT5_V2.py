"""Lösung für die Berechnung der maximalen Punktzahl aus k geordneten Paaren."""

from functools import lru_cache

class Solution:
"""Berechnet die maximale Punktzahl für k geordnet ausgewählte Indexpaarungen."""

```
def maxScore(self, nums1, nums2, k):  # pylint: disable=invalid-name
    """
    Berechnet die maximal erreichbare Summe aus genau k Produkten.

    Die ausgewählten Indizes müssen in beiden Arrays jeweils streng
    aufsteigend sein.

    Args:
        nums1: Erstes Array mit ganzen Zahlen.
        nums2: Zweites Array mit ganzen Zahlen.
        k: Anzahl der exakt auszuwählenden Paare.

    Returns:
        Die maximal erreichbare Punktzahl.
    """
    length1 = len(nums1)
    length2 = len(nums2)
    negative_infinity = float("-inf")

    @lru_cache(maxsize=None)
    def find_max_score(index1, index2, pairs_remaining):
        """
        Berechnet die beste Punktzahl ab den aktuellen Array-Positionen.

        Args:
            index1: Aktuelle Position in nums1.
            index2: Aktuelle Position in nums2.
            pairs_remaining: Anzahl der noch benötigten Paare.

        Returns:
            Die maximal erreichbare Punktzahl für diesen Zustand.
        """
        # Es wurden bereits genau k Paare ausgewählt.
        if pairs_remaining == 0:
            return 0

        # Es sind nicht mehr genügend Elemente für die benötigten Paare übrig.
        if (
            length1 - index1 < pairs_remaining
            or length2 - index2 < pairs_remaining
        ):
            return negative_infinity

        # Möglichkeit 1: Aktuelles Element aus nums1 überspringen.
        best_score = find_max_score(
            index1 + 1,
            index2,
            pairs_remaining,
        )

        # Möglichkeit 2: Aktuelles Element aus nums2 überspringen.
        best_score = max(
            best_score,
            find_max_score(
                index1,
                index2 + 1,
                pairs_remaining,
            ),
        )

        # Möglichkeit 3: Die beiden aktuellen Elemente miteinander paaren.
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
```
