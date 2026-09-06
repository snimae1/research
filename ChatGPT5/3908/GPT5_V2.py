"""Lösung zur Überprüfung, ob eine Zahl eine bestimmte Ziffer enthält."""

# pylint: disable=invalid-name,too-few-public-methods,useless-object-inheritance


class Solution(object):
    """Enthält die Lösung für die Validierungsaufgabe."""

    def validDigit(self, n, x):
        """
        Überprüft, ob n die Ziffer x enthält, ohne mit x zu beginnen.

        :param n: Zu überprüfende ganze Zahl.
        :param x: Gesuchte Ziffer.
        :return: True, wenn n gültig ist, andernfalls False.
        """
        number = str(n)
        digit = str(x)

        # Die Zahl darf nicht mit der gesuchten Ziffer beginnen.
        if number[0] == digit:
            return False

        # Die gesuchte Ziffer muss mindestens einmal vorkommen.
        return digit in number
