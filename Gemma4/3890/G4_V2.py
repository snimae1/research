"""
Dieses Modul enthält die Lösung zur Suche nach 'guten Zahlen' (Taxicab-Zahlen),
die als Summe von zwei verschiedenen Kubikzahlenpaaren dargestellt werden können.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Berechnung von guten Ganzzahlen bis zu einer Obergrenze n.
    """

    def find_good_integers(self, n):
        """
        Findet alle positiven Ganzzahlen x <= n, für die es mindestens zwei
        verschiedene Paare (a, b) gibt, sodass x = a^3 + b^3 und a <= b.

        :param n: Die Obergrenze der zu suchenden Zahlen.
        :type n: int
        :return: Eine aufsteigend sortierte Liste aller guten Ganzzahlen.
        :rtype: List[int]
        """
        # Dictionary, um zu zählen, wie oft eine Summe von zwei Kubikzahlen vorkommt
        counts = {}

        # Die maximale Grenze für a und b ist die Kubikwurzel von n.
        # +2 als Sicherheitspuffer für Rundungsfehler bei der Potenzrechnung.
        limit = int(n**(1/3)) + 2

        for a in range(1, limit):
            a_cubed = a**3
            if a_cubed >= n:
                break

            for b in range(a, limit):
                val = a_cubed + b**3

                # Wenn die Summe das Limit überschreitet, können wir für dieses 'a'
                # aufhören, da weitere b-Werte die Summe nur noch erhöhen.
                if val > n:
                    break

                # Zähle die Vorkommen der Summe x = a^3 + b^3
                counts[val] = counts.get(val, 0) + 1

        # Filter: Behalte nur Zahlen, die mindestens zwei verschiedene Paare haben.
        good_integers = [x for x, count in counts.items() if count >= 2]

        # Die Ergebnisse müssen aufsteigend sortiert zurückgegeben werden.
        good_integers.sort()

        return good_integers
