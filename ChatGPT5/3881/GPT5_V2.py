```python
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

        # Die Person an Position pos selbst beeinflusst die Sichtbarkeit
        # nicht und kann daher unabhängig 'L' oder 'R' wählen.
        own_choices = 2

        # Alle Personen außer der betrachteten Person können entweder
        # sichtbar oder unsichtbar sein. Entscheidend ist nur, welche
        # k der insgesamt n - 1 anderen Personen sichtbar sind.
        #
        # Für jede Auswahl von k Personen gibt es genau eine passende
        # Richtungswahl für diese Personen. Die übrigen n - 1 - k
        # Personen müssen die jeweils andere Richtung wählen.
        #
        # Daher entspricht die Anzahl der Möglichkeiten:
        #
        #     2 * C(n - 1, k)
        #
        # Die Position pos spielt für das Ergebnis somit keine Rolle.
        if k < 0 or k > n - 1:
            return 0

        # Fakultäten werden für die Berechnung des Binomialkoeffizienten
        # modulo mod benötigt:
        #
        # C(n, k) = n! / (k! * (n-k)!)
        #
        # Division wird modulo einer Primzahl durch Multiplikation mit
        # dem modularen Inversen durchgeführt.
        factorial = [1] * n

        for index in range(1, n):
            factorial[index] = factorial[index - 1] * index % mod

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

        combinations = (
            factorial[n - 1]
            * inverse_factorial[k]
            % mod
            * inverse_factorial[n - 1 - k]
            % mod
        )

        return own_choices * combinations % mod
```
