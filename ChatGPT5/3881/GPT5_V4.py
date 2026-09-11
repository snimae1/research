"""Lösung zur Berechnung der möglichen Sichtbarkeitskonfigurationen."""


# pylint: disable=too-few-public-methods
class Solution:
    """Berechnet die Anzahl der gültigen Richtungszuweisungen."""

    # Der Methodenname ist durch die Aufgabenstellung vorgegeben.
    # pylint: disable=invalid-name
    def countVisiblePeople(self, n, pos, k):
        """
        Berechnet die Anzahl der Richtungszuweisungen mit genau k sichtbaren Personen.

        :param n: Anzahl der Personen.
        :param pos: Position der betrachteten Person.
        :param k: Gewünschte Anzahl sichtbarer Personen.
        :return: Anzahl der möglichen Zuweisungen modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        # Die Person an Position pos kann unabhängig 'L' oder 'R' wählen.
        own_choices = 2

        # Es gibt n - 1 andere Personen. Genau k davon müssen sichtbar sein.
        if k < 0 or k > n - 1:
            return 0

        # Fakultäten für die Berechnung von C(n - 1, k).
        factorial = [1] * n

        for index in range(1, n):
            factorial[index] = factorial[index - 1] * index % mod

        # Inverse Fakultäten mittels Fermats kleinem Satz.
        inverse_factorial = [1] * n
        inverse_factorial[n - 1] = pow(
            factorial[n - 1],
            mod - 2,
            mod
        )

        for index in range(n - 1, 0, -1):
            inverse_factorial[index - 1] = (
                inverse_factorial[index] * index
            ) % mod

        # C(n - 1, k) = (n - 1)! / (k! * (n - 1 - k)!).
        combinations = (
            factorial[n - 1]
            * inverse_factorial[k]
            % mod
            * inverse_factorial[n - 1 - k]
            % mod
        )

        # Die Person an pos hat zwei unabhängige Möglichkeiten.
        return own_choices * combinations % mod
