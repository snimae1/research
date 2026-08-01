class Solution(object):

    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Hilfsfunktion zur Primzahlprüfung
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Ziffern umkehren
        r = int(str(n)[::-1])

        # Bereichsgrenzen festlegen
        start = min(n, r)
        end = max(n, r)

        # Summe der Primzahlen im Bereich berechnen
        prime_sum = 0
        for num in range(start, end + 1):
            if is_prime(num):
                prime_sum += num

        return prime_sum
